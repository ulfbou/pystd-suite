#!/usr/bin/env python3
"""AI planning-context supplier for GitHub-backed repositories.

Produces one deterministic JSON snapshot of local Git state and bounded GitHub
state. Factual fields contain measured values only. Remote provenance records
fresh/cached/absent/unavailable state, the served data timestamp, served reason,
and any refresh error. Sensitive local paths are counted, never emitted or read.

Standard library only. Python 3.9+.
Exit codes: 0 complete, 1 fatal, 2 degraded but usable.
"""
import argparse
import datetime as dt
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

EXIT_SUCCESS, EXIT_FATAL, EXIT_DEGRADED = 0, 1, 2
SCHEMA_VERSION, SCRIPT_VERSION = "2.3.0", "2.1.0"
API_BASE, LIST_PAGE, HTTP_TIMEOUT = "https://api.github.com", 100, 30
SENSITIVE_PATH_PATTERNS = [
    ".env", ".env.*", "*.env", "*.pem", "*.key", "*.pfx", "*.p12",
    "*.jks", "*.keystore", "id_rsa*", "id_ed25519*", "id_ecdsa*",
    "id_dsa*", "*credential*", "*secret*", ".npmrc", ".netrc",
]
AUTHORITY_FILES = [
    "CONTRIBUTING.md", "ROADMAP.md", "ARCHITECTURE.md", "SECURITY.md",
    "VISION.md", "GOVERNANCE.md", "CODEOWNERS",
]
BLOCKER_PATTERNS = [
    re.compile(r"blocked[ -]by\s*#(\d+)", re.I),
    re.compile(r"depends[ -]?on\s*#(\d+)", re.I),
]
PEM_KEY_RE = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")
GITHUB_SLUG_RE = re.compile(
    r"github\.com[:/]([A-Za-z0-9_.\-]+)/([A-Za-z0-9_.\-]+?)(?:\.git)?/?$"
)

def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)

def iso_now() -> str:
    return utcnow().isoformat()

def parse_iso(value: Optional[str]) -> Optional[dt.datetime]:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None

def run_git(args: List[str], cwd: Path, binary: bool = False):
    try:
        p = subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                           text=not binary, check=False,
                           **({} if binary else {"encoding": "utf-8", "errors": "surrogateescape"}))
        if binary:
            return p.returncode, p.stdout, p.stderr
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except OSError as exc:
        empty = b"" if binary else ""
        error = str(exc).encode() if binary else str(exc)
        return 127, empty, error

def is_sensitive_path(path: str) -> bool:
    parts = Path(path.strip().strip('"')).parts
    return any(fnmatch.fnmatch(part, pattern)
               for pattern in SENSITIVE_PATH_PATTERNS for part in parts)

def parse_github_slug(url: Optional[str]) -> Optional[str]:
    match = GITHUB_SLUG_RE.search((url or "").strip())
    return f"{match.group(1)}/{match.group(2)}" if match else None

def sanitize_remote_url(url: Optional[str]) -> Optional[str]:
    if not url:
        return None
    value = url.strip()
    if "://" not in value:
        return value
    try:
        parsed = urllib.parse.urlsplit(value)
        if not parsed.hostname:
            return None
        host = parsed.hostname + (f":{parsed.port}" if parsed.port else "")
        return urllib.parse.urlunsplit(
            (parsed.scheme, host, parsed.path, parsed.query, parsed.fragment)
        )
    except (ValueError, TypeError):
        return None

def label_names(raw: Dict[str, Any]) -> List[str]:
    return sorted(x.get("name") for x in raw.get("labels") or []
                  if isinstance(x, dict) and x.get("name"))

def logins(entries: Optional[List[Any]]) -> List[str]:
    return sorted(x.get("login") for x in entries or []
                  if isinstance(x, dict) and x.get("login"))

def provenance(state: str, fetched: Optional[str], error: Optional[str], reason: str):
    return {"source_state": state, "fetched_at": fetched,
            "error_class": error, "served_reason": reason}

class Cache:
    def __init__(self, path: Path):
        self.path, self.data = path, {}
        try:
            loaded = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
            if isinstance(loaded, dict):
                self.data = loaded
        except (OSError, ValueError):
            pass
    def entry(self, key: str):
        value = self.data.get(key)
        return value if isinstance(value, dict) else None
    def put(self, key: str, etag: Optional[str], fetched: str, payload: Any):
        self.data[key] = {"etag": etag, "fetched_at": fetched, "payload": payload}
        self.flush()
    def flush(self):
        temporary = None
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=self.path.parent,
                                             prefix=f".{self.path.name}.", delete=False) as out:
                json.dump(self.data, out, sort_keys=True, ensure_ascii=False)
                out.flush(); os.fsync(out.fileno()); temporary = Path(out.name)
            os.replace(temporary, self.path)
        except OSError:
            pass
        finally:
            if temporary:
                try: temporary.unlink(missing_ok=True)
                except OSError: pass

class RateLimit:
    def __init__(self):
        self.remaining, self.reset_at = None, None
    def observe(self, headers: Any):
        remaining, reset = headers.get("X-RateLimit-Remaining"), headers.get("X-RateLimit-Reset")
        if remaining and remaining.isdigit(): self.remaining = int(remaining)
        if reset and reset.isdigit():
            self.reset_at = dt.datetime.fromtimestamp(int(reset), dt.timezone.utc).isoformat()

def api_fetch(endpoint: str, token: Optional[str], cache: Cache, max_age: int,
              rate: RateLimit) -> Tuple[Any, str, Optional[str], Optional[str], str]:
    key, entry = hashlib.sha256(endpoint.encode()).hexdigest(), None
    entry = cache.entry(key)
    if max_age > 0 and entry:
        stamp = parse_iso(entry.get("fetched_at"))
        if stamp and (utcnow() - stamp).total_seconds() < max_age:
            return entry.get("payload"), "cached", None, entry.get("fetched_at"), "ttl_hit"
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": f"frontier-context-supplier/{SCRIPT_VERSION}",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token: headers["Authorization"] = f"Bearer {token}"
    if entry and entry.get("etag"): headers["If-None-Match"] = entry["etag"]
    try:
        with urllib.request.urlopen(urllib.request.Request(API_BASE + endpoint, headers=headers),
                                    timeout=HTTP_TIMEOUT) as response:
            rate.observe(response.headers)
            payload, fetched = json.loads(response.read().decode("utf-8")), iso_now()
            cache.put(key, response.headers.get("ETag"), fetched, payload)
            return payload, "fresh", None, fetched, "network_fetch"
    except urllib.error.HTTPError as exc:
        rate.observe(exc.headers)
        if exc.code == 304 and entry:
            return entry.get("payload"), "cached", None, entry.get("fetched_at"), "etag_validated"
        error = ("auth_failure_401" if exc.code == 401 else
                 "rate_limited_403" if exc.code == 403 and rate.remaining == 0 else
                 "forbidden_403" if exc.code == 403 else
                 "not_found_404" if exc.code == 404 else
                 f"server_error_{exc.code}" if exc.code >= 500 else f"http_error_{exc.code}")
    except (ValueError, urllib.error.URLError, OSError) as exc:
        error = f"network_or_parse_error_{type(exc).__name__}"
    if entry:
        return entry.get("payload"), "cached", error, entry.get("fetched_at"), "stale_fallback"
    return None, "unavailable", error, None, "fetch_failed"

def fetch(endpoint, name, slug, token, cache, max_age, rate, sections, unknowns):
    if not slug:
        sections[name] = provenance("unavailable", None, "no_github_origin", "not_attempted")
        unknowns.append(f"{name}: no GitHub remote on origin")
        return None
    payload, state, error, fetched, reason = api_fetch(endpoint, token, cache, max_age, rate)
    sections[name] = provenance(state, fetched, error, reason)
    if error: unknowns.append(f"{name}: {error}")
    return payload

def collect_local(repo: Path):
    state, unknowns = {}, []
    code, branch, _ = run_git(["symbolic-ref", "--short", "HEAD"], repo)
    detached = code != 0
    if detached:
        c, sha, _ = run_git(["rev-parse", "HEAD"], repo)
        state["current_branch"] = f"detached@{sha[:7]}" if c == 0 else None
        unknowns.append("current_branch: detached HEAD")
    else: state["current_branch"] = branch
    state["detached_head"] = detached
    code, out, _ = run_git(["log", "-1", "--format=%H%n%an%n%aI%n%s"], repo)
    if code == 0 and out:
        fields = out.split("\n")
        c, names, _ = run_git(["show", "--name-only", "--format=", fields[0]], repo)
        all_names = [x for x in names.split("\n") if x] if c == 0 else []
        visible = [x for x in all_names if not is_sensitive_path(x)]
        state["last_commit"] = {
            "sha": fields[0], "author": fields[1] if len(fields) > 1 else None,
            "committed_at": fields[2] if len(fields) > 2 else None,
            "message": fields[3] if len(fields) > 3 else None,
            "files_touched_count": len(all_names), "files_touched": visible[:50],
            "files_touched_truncated": len(visible) > 50,
            "redacted_paths": len(all_names) - len(visible),
        }
    else:
        state["last_commit"] = None; unknowns.append("last_commit: unavailable")
    code, raw, _ = run_git(["status", "--porcelain=v1", "-z", "--untracked-files=all"], repo, True)
    counts = {"modified": 0, "added": 0, "deleted": 0, "renamed": 0, "untracked": 0}
    redacted = 0
    if code == 0:
        records, i = raw.split(b"\0"), 0
        while i < len(records):
            record, i = records[i], i + 1
            if not record: continue
            if len(record) < 4 or record[2:3] != b" ":
                unknowns.append("working_tree: malformed status record"); continue
            xy, path = record[:2].decode("ascii", "replace"), record[3:].decode("utf-8", "surrogateescape")
            if "R" in xy or "C" in xy:
                if i >= len(records) or not records[i]:
                    unknowns.append("working_tree: malformed rename record"); continue
                path, i = records[i].decode("utf-8", "surrogateescape"), i + 1
            if is_sensitive_path(path): redacted += 1; continue
            if xy == "??": counts["untracked"] += 1
            elif "A" in xy: counts["added"] += 1
            elif "D" in xy: counts["deleted"] += 1
            elif "R" in xy: counts["renamed"] += 1
            else: counts["modified"] += 1
    else: unknowns.append("working_tree: git status failed")
    state["working_tree"] = {"dirty": sum(counts.values()) + redacted > 0,
                             "change_summary": counts, "redacted_paths": redacted,
                             "note": "sensitive paths are counted, never named or read"}
    code, out, _ = run_git(["rev-list", "--left-right", "--count", "@{upstream}...HEAD"], repo)
    parts = out.split()
    state["ahead_behind"] = ({"behind": int(parts[0]), "ahead": int(parts[1])}
                               if code == 0 and len(parts) == 2 else None)
    if state["ahead_behind"] is None: unknowns.append("ahead_behind: unavailable or no upstream")
    code, out, _ = run_git(["ls-files"], repo)
    tracked = set(out.splitlines()) if code == 0 else set()
    authority = {}
    for name in AUTHORITY_FILES:
        for candidate in (name, f"docs/{name}", f".github/{name}"):
            if candidate in tracked: authority[name] = candidate; break
    adr_dirs = sorted({"/".join(p.split("/")[:-1]) for p in tracked
                       if len(p.split("/")) > 1 and re.fullmatch(r"[^/]*adrs?", p.split("/")[-2], re.I)})
    state["authority_pointers"] = {"files": authority, "adr_directories": adr_dirs,
        "note": "presence only; consult before behavioral proposals; ADR directories use a name heuristic"}
    return state, unknowns

def pool_item(kind, raw, now):
    updated, milestone = parse_iso(raw.get("updated_at")), raw.get("milestone") or {}
    item = {"id": raw.get("number"), "type": kind,
            "string_id": f"{kind}:{raw.get('number')}", "title": raw.get("title"),
            "html_url": raw.get("html_url"), "labels": label_names(raw),
            "assignees": logins(raw.get("assignees")), "created_at": raw.get("created_at"),
            "updated_at": raw.get("updated_at"),
            "staleness_days": max(0, (now - updated).days) if updated else None,
            "comments_count": raw.get("comments"), "milestone": milestone.get("title"),
            "milestone_due": milestone.get("due_on"), "blockers": []}
    if kind == "pull_request":
        item.update(draft=raw.get("draft"), mergeable_state=raw.get("mergeable_state"),
                    review_comments_count=raw.get("review_comments"),
                    requested_reviewers=logins(raw.get("requested_reviewers")))
    due, stale = (item["milestone_due"] or "9999-99-99")[:10], min(item["staleness_days"] or 0, 99999)
    item["sort_key"] = f"{due}|{99999-stale:05d}|{(item['id'] or 0):08d}"
    return item

def blocker_refs(body):
    refs: Set[int] = set()
    for pattern in BLOCKER_PATTERNS:
        refs.update(int(x) for x in pattern.findall(body or ""))
    return refs

def find_cycles(nodes, edges):
    adjacency = {x: [] for x in nodes}
    for a, b in edges:
        if a in adjacency and b in adjacency: adjacency[a].append(b)
    cycles, seen = [], set()
    def visit(node, stack, active, done):
        active.add(node); stack.append(node)
        for child in adjacency[node]:
            if child in active:
                group = tuple(sorted(stack[stack.index(child):]))
                if group not in seen: seen.add(group); cycles.append(list(group))
            elif child not in done: visit(child, stack, active, done)
        stack.pop(); active.remove(node); done.add(node)
    done = set()
    for node in nodes:
        if node not in done: visit(node, [], set(), done)
    return sorted(cycles)

def build_pool(slug, token, cache, max_age, rate, sections, unknowns):
    issues = fetch(f"/repos/{slug}/issues?state=open&per_page={LIST_PAGE}&sort=updated&direction=desc" if slug else "",
                   "open_issues", slug, token, cache, max_age, rate, sections, unknowns) or []
    pulls = fetch(f"/repos/{slug}/pulls?state=open&per_page={LIST_PAGE}&sort=updated&direction=desc" if slug else "",
                  "open_pulls", slug, token, cache, max_age, rate, sections, unknowns) or []
    now, items, bodies, labels = utcnow(), [], {}, {}
    for raw in issues:
        if isinstance(raw, dict) and "pull_request" not in raw:
            item = pool_item("issue", raw, now); items.append(item); bodies[item["string_id"]] = raw.get("body")
            for name in label_names(raw): labels[name] = labels.get(name, 0) + 1
    for raw in pulls:
        if isinstance(raw, dict):
            item = pool_item("pull_request", raw, now); items.append(item); bodies[item["string_id"]] = raw.get("body")
    by_number = {item["id"]: item["string_id"] for item in items}
    edges = []
    for item in items:
        refs = blocker_refs(bodies[item["string_id"]])
        item["blockers"] = sorted(by_number[n] for n in refs if n in by_number)
        item["unverified_blocker_numbers"] = sorted(n for n in refs if n not in by_number)
        edges.extend((item["string_id"], blocker) for blocker in item["blockers"])
    cycles = find_cycles([x["string_id"] for x in items], edges)
    cycle_members = {x for group in cycles for x in group}
    ready, blocked, unverified = [], [], []
    for item in items:
        if item["unverified_blocker_numbers"]: unverified.append(item)
        elif item["blockers"] or item["string_id"] in cycle_members: blocked.append(item)
        else: ready.append(item)
    for queue in (ready, blocked, unverified): queue.sort(key=lambda x: x["sort_key"])
    truncation = {"open_issues": {"at_least": len(issues), "truncated": len(issues) >= LIST_PAGE},
                  "open_pulls": {"at_least": len(pulls), "truncated": len(pulls) >= LIST_PAGE}}
    return {"selection_policy": "Ready has no detected or unverified blockers; queues sort by milestone due, staleness descending, id.",
            "blocker_rule": "Only explicit 'blocked by #N' and 'depends on #N' body references are recognized.",
            "ready_queue": ready, "blocked_queue": blocked, "unverified_queue": unverified,
            "circular_dependency_groups": cycles,
            "counts": {"ready": len(ready), "blocked": len(blocked), "unverified": len(unverified),
                       "circular_members": len(cycle_members)}, "truncation": truncation,
            "detail_available_via": "frontier.py --detail <type>:<id>"}, labels

def main():
    parser = argparse.ArgumentParser(description="Machine-readable Git and GitHub planning context")
    parser.add_argument("--repo-path", default=".")
    parser.add_argument("--max-age", type=int, default=3600)
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument("--detail", metavar="TYPE:ID")
    args = parser.parse_args()
    start = Path(args.repo_path).resolve()
    code, top, _ = run_git(["rev-parse", "--show-toplevel"], start)
    if code != 0:
        print(json.dumps({"fatal": "not inside a git repository", "path": str(start)}, indent=2), file=sys.stderr)
        return EXIT_FATAL
    repo = Path(top).resolve(); cache = Cache(repo / ".git" / "frontier-cache.json"); rate = RateLimit()
    token, max_age = os.environ.get("GITHUB_TOKEN"), 0 if args.no_cache else max(0, args.max_age)
    code, raw_origin, _ = run_git(["remote", "get-url", "origin"], repo)
    raw_origin = raw_origin if code == 0 else None
    slug, sections, unknowns = parse_github_slug(raw_origin), {}, []
    if not token: unknowns.append("github_token: absent; anonymous API limits apply")
    if args.detail:
        match = re.fullmatch(r"(issue|pr):(\d+)", args.detail.lower())
        if not match or not slug:
            print(json.dumps({"error": "detail requires issue:N or pr:N and a GitHub origin"}, indent=2)); return EXIT_FATAL
        number = int(match.group(2))
        payload, state, error, fetched, reason = api_fetch(f"/repos/{slug}/issues/{number}", token, cache, 0, rate)
        if not isinstance(payload, dict):
            print(json.dumps({"error": error or "unavailable", "source_state": state}, indent=2)); return EXIT_FATAL
        body = payload.get("body") or ""; redacted = bool(PEM_KEY_RE.search(body))
        doc = {"schema_version": SCHEMA_VERSION, "script_version": SCRIPT_VERSION, "collected_at": iso_now(),
               "source_state": state, "fetched_at": fetched, "served_reason": reason, "error_class": error,
               "id": number, "type": "pull_request" if "pull_request" in payload else "issue",
               "title": payload.get("title"), "html_url": payload.get("html_url"), "state": payload.get("state"),
               "created_at": payload.get("created_at"), "updated_at": payload.get("updated_at"),
               "closed_at": payload.get("closed_at"), "labels": label_names(payload),
               "assignees": logins(payload.get("assignees")), "comments_count": payload.get("comments"),
               "milestone": (payload.get("milestone") or {}).get("title"),
               "body": "[REDACTED: PRIVATE KEY BLOCK]" if redacted else body, "body_redacted": redacted}
        print(json.dumps(doc, sort_keys=True, indent=2, ensure_ascii=False))
        return EXIT_DEGRADED if error else EXIT_SUCCESS
    local, local_unknowns = collect_local(repo); unknowns.extend(local_unknowns)
    meta = fetch(f"/repos/{slug}" if slug else "", "repo_metadata", slug, token, cache, max_age, rate, sections, unknowns)
    meta = meta if isinstance(meta, dict) else {}
    pool, label_counts = build_pool(slug, token, cache, max_age, rate, sections, unknowns)
    labels_raw = fetch(f"/repos/{slug}/labels?per_page={LIST_PAGE}" if slug else "", "labels", slug, token, cache, max_age, rate, sections, unknowns)
    labels = None if not isinstance(labels_raw, list) else {"items": sorted([
        {"name": x.get("name"), "description": x.get("description"), "color": x.get("color"),
         "fetched_open_issue_count": label_counts.get(x.get("name"), 0),
         "count_basis": "open issues in fetched, possibly truncated pool"}
        for x in labels_raw if isinstance(x, dict)], key=lambda x: (x["name"] or "").casefold()),
        "truncation": {"at_least": len(labels_raw), "truncated": len(labels_raw) >= LIST_PAGE}}
    milestones_raw = fetch(f"/repos/{slug}/milestones?state=open&per_page={LIST_PAGE}" if slug else "", "open_milestones", slug, token, cache, max_age, rate, sections, unknowns)
    milestones_raw = milestones_raw if isinstance(milestones_raw, list) else []
    milestones = sorted([{"number": x.get("number"), "title": x.get("title"), "due_on": x.get("due_on"),
                          "open_issues": x.get("open_issues"), "closed_issues": x.get("closed_issues"),
                          "html_url": x.get("html_url")} for x in milestones_raw if isinstance(x, dict)],
                        key=lambda x: (x["due_on"] or "9999", x["number"] or 0))
    runs = fetch(f"/repos/{slug}/actions/runs?per_page=30" if slug else "", "workflow_health", slug, token, cache, max_age, rate, sections, unknowns)
    latest = {}
    if isinstance(runs, dict):
        for run in runs.get("workflow_runs") or []:
            if isinstance(run, dict) and run.get("name") not in latest:
                latest[run.get("name")] = {k: run.get(k) for k in ("name", "status", "conclusion", "created_at", "head_branch", "event", "html_url")}
    release = fetch(f"/repos/{slug}/releases/latest" if slug else "", "release_state", slug, token, cache, max_age, rate, sections, unknowns)
    if sections.get("release_state", {}).get("error_class") == "not_found_404":
        sections["release_state"].update(source_state="absent", error_class=None, served_reason="confirmed_absent")
    degraded = any(x.get("source_state") == "unavailable" or x.get("error_class") for x in sections.values())
    cached = any(x.get("source_state") == "cached" for x in sections.values())
    envelope = {"schema_version": SCHEMA_VERSION, "script_version": SCRIPT_VERSION, "collected_at": iso_now(),
        "execution_metadata": {"cached": cached, "degraded_mode": degraded, "token_present": bool(token),
            "rate_limit": {"remaining": rate.remaining, "reset_at": rate.reset_at}, "provenance": {"sections": sections}},
        "unknowns": unknowns,
        "repository": {"identity": {"origin_url": sanitize_remote_url(raw_origin), "owner_repo_slug": slug,
            "default_branch": meta.get("default_branch"), "description": meta.get("description"), "topics": meta.get("topics") or []}, **local},
        "labels": labels,
        "milestones": {"open": milestones, "open_truncation": {"at_least": len(milestones_raw), "truncated": len(milestones_raw) >= LIST_PAGE}},
        "candidate_pool": pool,
        "planning_context": {"workflow_health": {"latest_runs": sorted(latest.values(), key=lambda x: x["name"] or ""),
            "basis": "latest run per workflow name from 30 most recent runs"} if latest else None,
            "release_state": {"latest_tag": release.get("tag_name"), "published_at": release.get("published_at"),
                              "url": release.get("html_url")} if isinstance(release, dict) else None}}
    print(json.dumps(envelope, sort_keys=True, indent=2, ensure_ascii=False))
    return EXIT_DEGRADED if degraded else EXIT_SUCCESS

if __name__ == "__main__":
    raise SystemExit(main())
