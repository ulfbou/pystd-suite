# Frontier roadmap

## Product boundary

`frontier.py` is a bounded, read-only context supplier for planning consumers. It is not a GitHub synchronization engine, project-management authority, secret scanner, or autonomous prioritization service. The standard-library-only constraint remains in force until measured needs justify changing it.

## Current release: 2.1.0 / schema 2.3.0

### Completed trust-boundary corrections

- Sanitize emitted HTTP(S) remote URLs so embedded user information cannot reach JSON output.
- Apply sensitive-path filtering to last-commit file names while retaining measured totals and redaction counts.
- Parse worktree status with NUL-delimited porcelain records, including rename/copy records.
- Use atomic cache replacement inside `.git`.
- Record `source_state`, `fetched_at`, `served_reason`, and `error_class` per remote section.
- Return degraded exit status when stale cache is served after a refresh failure.
- Keep cache TTL hits and successful ETag validation usable without declaring degradation.
- Split dependency candidates into ready, blocked, and unverified queues.
- Keep explicit, predictable blocker syntax rather than natural-language inference.
- Preserve bounded page behavior and disclose boundary truncation.
- Sort emitted labels, milestones, workflow summaries, and candidate queues deterministically.

## Acceptance checks for the current release

- [ ] `python -m py_compile frontier.py` passes.
- [ ] Running outside a Git repository returns exit code 1 and a JSON fatal diagnostic on stderr.
- [ ] A repository with an HTTPS remote containing user information emits a sanitized remote URL.
- [ ] Sensitive paths touched by the last commit increase `redacted_paths` and never appear in `files_touched`.
- [ ] Sensitive dirty paths increase worktree `redacted_paths` and never appear in output.
- [ ] Legal Git filenames and rename/copy status records do not corrupt status counts.
- [ ] A fresh successful remote fetch records `network_fetch`.
- [ ] A live TTL cache hit records `ttl_hit`.
- [ ] HTTP 304 cache validation records `etag_validated`.
- [ ] Failed refresh with cached payload records `stale_fallback`, retains the error class, and exits 2.
- [ ] Failed fetch without cache records `unavailable` and exits 2.
- [ ] Confirmed absence of a latest release records `absent`, not `unavailable`.
- [ ] An item with no recognized blocker is ready.
- [ ] An item blocked by a fetched open item is blocked.
- [ ] An item referring to a blocker outside the bounded pool is unverified, not ready or asserted blocked.
- [ ] Circular dependency members are never ready.
- [ ] Repeated execution over identical local and cached inputs produces deterministic ordering.

## Near-term hardening, only when repository tests are added

### P1: Contract tests

- Add fixture repositories covering detached HEAD, unborn branch, no upstream, rename/copy status, unusual UTF-8 names, and sensitive names.
- Add mocked HTTP fixtures for 200, 304, 401, 403 rate limit, 404, 5xx, invalid JSON, timeout, and stale fallback.
- Assert exit-code semantics independently from JSON content.
- Assert schema-required fields and nullable factual fields.
- Assert stable output ordering after removing collection timestamps.
- Add regression tests proving request authorization headers and raw remote URLs never enter cache or output.

### P1: Blocker precision

- Resolve explicitly referenced blockers on demand only when unverified items materially affect planning.
- Cache referenced-item lookups through the existing cache abstraction.
- Preserve `unverified` when lookup fails or permission prevents resolution.
- Never infer dependencies from arbitrary prose.
- Consider repository-qualified references only when a concrete cross-repository use case is accepted.

### P1: Provenance completeness

- Capture pagination evidence from GitHub `Link` headers so page-boundary completeness is measured rather than inferred from `len == 100`.
- Record the endpoint class and bounded page size without storing authorization material.
- Add an output-level `completeness` summary derived only from section evidence.

### P2: Planning usefulness

- Add branch-protection and required-check summaries only if planning decisions demonstrably need them.
- Add release distance only with explicit local-tag provenance and clear handling of missing tags.
- Add authority-document content only as a separate opt-in mode with byte and file limits; default mode remains presence-only.
- Add GitHub Projects support only after defining which project version and fields are authoritative.
- Add organization-level aggregation only as a separate command and schema.

### P2: Privacy controls

- Add an opt-in policy for suppressing commit-author identity when snapshots cross trust boundaries.
- Add configurable sensitive-path patterns without weakening the built-in denylist.
- Consider body omission or bounded body output in detail mode based on an explicit consumer requirement.
- Do not present private-key recognition as general secret detection.

## Explicit deferrals

The following are intentionally not planned without measured evidence:

- Async networking or concurrency.
- Third-party runtime dependencies.
- Full pagination by default.
- GraphQL migration.
- General secret scanning.
- Natural-language dependency inference.
- Database-backed cache.
- Plugin architecture.
- Autonomous prioritization or mutation of GitHub state.
- Automatic reading of repository authority documents in the default snapshot.

## Decision triggers

Adopt a deferred feature only when at least one condition is demonstrated:

1. The bounded snapshot repeatedly omits information required for a real planning decision.
2. API latency or quota use is measured and the proposed change improves it without weakening provenance.
3. A privacy or correctness incident proves the existing boundary insufficient.
4. A stable consumer contract requires data not representable in schema 2.3.0.
5. Repository tests can mechanically protect the new behavior.

## Versioning policy

- Patch script version for implementation corrections that preserve JSON meaning.
- Minor script version for new optional behavior or fields.
- Minor schema version for backward-compatible fields or queue categories.
- Major schema version for renamed, removed, or semantically changed fields.
- Every schema change requires fixtures, migration notes, and deterministic-output tests.

## Definition of done for the next release

- All current acceptance checks are automated.
- No raw credential-bearing remote is emitted or cached.
- Sensitive filenames are absent from every output section.
- Every remote section has explicit provenance and truthful degraded behavior.
- Candidate classification has no false-ready result from an unresolved explicit blocker.
- Output ordering is deterministic from identical payloads.
- Documentation states boundedness and non-goals.
- The carrier containing changes is DX v2.0.0, verifies with the authoritative codec, and includes only complete changed files.
