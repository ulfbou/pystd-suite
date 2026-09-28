# Security Policy

Status: Policy
Owner: Repository security reporting and security expectations
Scope: Security-relevant DX trust boundaries, vulnerability handling, safe reproduction, remediation evidence, and supported-environment limits

## Purpose

DX processes untrusted carrier bytes and relates untrusted requests, paths, workspace state, filesystem objects, streams, optional Git facts, and environmental inputs to inspection, planning, carrier delivery, and workspace mutation. Security work MUST preserve the Accepted product, architecture, carrier, workspace, selection, operation, diagnostic, CLI/process, compatibility, schema-governance, and fixture-governance boundaries.

This policy governs security reporting and security expectations. It does not redefine observable semantics, contributor mechanics, roadmap priority, release procedure, response timelines, severity levels, cryptographic guarantees, signing, or platform support.

## Reporting security issues

A suspected vulnerability MUST use the repository's available private security-reporting mechanism. It MUST NOT be disclosed publicly before remediation when premature disclosure could increase risk.

A report SHOULD include a concise impact statement, affected operation or trust boundary, minimal safe reproduction, relevant carrier or workspace facts, observed result, expected safety property, environment details, and whether mutation or partial effects occurred. Reports MUST minimize sensitive data and MUST NOT include secrets, unrelated private content, or unsafe live-system instructions.

No response timeline, severity SLA, bounty, public reporting address, hosted portal, or vendor-specific reporting feature is promised by this repository policy.

## Security scope

Security-relevant categories include:

- carrier parsing or structural-validation bypass;
- logical-path traversal, absolute-path interpretation, or containment escape;
- unsafe carrier-to-workspace mapping;
- source, ancestor, destination, or output symlink following;
- opening FIFOs, sockets, devices, or unknown objects as ordinary files;
- unsafe overwrite, replacement, parent creation, or mutation authority;
- selected-set or output-sink confusion that changes intended content;
- changed-precondition, race, or identity handling that permits unintended effects;
- partial failure that conceals completed, untouched, failed, or uncertain effects;
- malformed input causing uncontrolled resource consumption or unbounded diagnostics;
- terminal byte-stream exposure or machine-output contamination;
- diagnostic disclosure of secrets, irrelevant host state, stack traces, or unsafe environmental details;
- dependency or external-capability compromise that crosses an admitted boundary;
- silent fallback from requested security-relevant capability or environmental validation;
- unsupported environment behavior presented as verified safety.

Incorrect behavior without a plausible confidentiality, integrity, availability, containment, or mutation-safety impact may remain a normal defect, but it MUST still be assessed against the accepted safety boundaries.

## Trust boundaries and untrusted inputs

The following are untrusted unless independently established otherwise:

- carrier bytes, directives, attributes, payloads, declared versions, logical paths, and NOTE content;
- command arguments, path operands, patterns, ignore rules, replacement authority, parent-creation authority, and stream selection;
- source and destination workspace contents;
- filesystem enumeration, object types, links, permissions, identities, case behavior, Unicode behavior, and state changes;
- standard input, standard output sinks, terminal capabilities, and interrupted or incomplete delivery;
- Git executable availability, repository facts, status output, ignore facts, and configuration context;
- environment, locale, current directory, platform, filesystem, process encoding, and external interruption;
- generated evidence, captured implementation output, and supplied reproduction artifacts.

Semantic logic MUST consume validated explicit facts. Environmental and external-capability behavior MUST be resolved at the applicable boundary, retained where relevant, and never converted into silent authority.

## Carrier and path safety

Carrier parsing MUST reject unsupported or malformed framing, attributes, payload representation, duplicate logical paths, invalid paths, and prohibited trailing content without guessing intent. Carrier validity MUST NOT be treated as proof of authenticity, trusted integrity, safe workspace applicability, or harmless content.

Logical carrier paths are not physical paths. Mapping to a workspace requires an explicit workspace root and applicable filesystem observations. Processing MUST prevent absolute, drive-like, UNC-like, traversal, separator-confused, empty-component, control-character, and out-of-root interpretations admitted by neither the carrier nor workspace contracts.

Lexical and physical containment MUST hold. Distinct logical paths MUST NOT be silently merged by case or Unicode behavior. An unsupported or unverified mapping environment MUST produce an explicit unsupported or inapplicable result rather than a best-effort mutation.

## Symlinks and special objects

Source symlinks, destination symlinks, carrier-output symlinks, and ancestor symlinks MUST NOT be followed for payload access, comparison, or mutation. This includes broken links and links resolving within the workspace.

FIFOs, sockets, block devices, character devices, and unknown objects MUST be classified without opening them as regular files. Bounded tests MAY create links or special objects only in isolated temporary workspaces with capability checks and cleanup.

Replacement or force authority MUST NOT override link, containment, directory, collision, unsupported-object, or parent-safety constraints.

## Mutation, changed preconditions, and partial failure

Workspace mutation and carrier-output mutation are separate capabilities. Read and planning operations MUST have no write capability. Mutation MUST consume validated planned intent and MUST NOT rediscover, reselect, silently broaden scope, change policy, or substitute changed content.

Safety- and conflict-relevant preconditions MUST be revalidated before mutation and before affected effects where required. A changed target, parent, link, identity, containment relationship, content observation, permission, or sink state MUST stop or reject mutation according to the owning semantics. Silent replanning is prohibited.

Whole-workspace rollback is not assumed. Partial failure evidence MUST preserve completed, failed, untouched, and uncertain effects and MUST NOT imply rollback. Security fixes affecting mutation MUST test failures before the first effect, after completed effects, during interruption, and under changed preconditions where applicable.

## Malformed input and resource exhaustion

Malformed carrier, CLI, pattern, ignore, Git, filesystem, and machine-boundary inputs MUST fail through bounded public error handling. They MUST NOT expose uncontrolled tracebacks as normal product output or trigger unbounded recursion, indefinite reads, unsafe special-object access, or accidental mutation.

Implementations SHOULD bound resource use according to the admitted operation and available evidence, including carrier size, physical-line length, entry count, decoded payload size, nesting or traversal work, diagnostic volume, comparison scope, and machine-output construction. A limit MUST NOT silently truncate semantic input or report success for incomplete processing. When a portable limit has not been accepted, exhaustion or inability to complete MUST remain an explicit environmental, unsupported, or failure result rather than an invented guarantee.

## Stream, terminal, and machine-output safety

Carrier bytes and exact decoded entry bytes MUST be refused on an interactive terminal unless explicit terminal-output authority is present. Human diagnostics MUST NOT contaminate carrier bytes, exact entry bytes, or machine-readable standard output.

Incomplete carrier or machine delivery MUST NOT be reported as success. Broken pipes and uncertain accepted prefixes remain process-boundary failures with uncertainty preserved where applicable.

Machine output MUST use the same semantic result and retained findings as human output. It MUST NOT expose internal plans, implementation exception names as stable identifiers, stack traces, secrets, arbitrary host state, or presentation-only details as semantic contract.

## Diagnostic disclosure

Diagnostics MUST provide enough bounded context to identify the operation, semantic category, affected typed resource, and relevant boundary cause. They SHOULD minimize physical host details when those details are unnecessary, unsafe to disclose, or harmful to portability.

Secrets, unrelated file contents, credentials, tokens, private carrier payloads, environment dumps, command histories, and full stack traces MUST NOT appear in normal diagnostics or public security reports. Optional debug evidence MUST be separated from the stable public contract and handled as sensitive when it contains host or workspace detail.

## Dependencies and external capabilities

Core runtime behavior is standard-library-first. Any third-party runtime dependency requires an explicit need, narrow boundary, review of the standard-library alternative, and verified security, compatibility, portability, and packaging consequences.

Git is an optional external capability, not trusted core semantics. Requested Git capabilities require explicit availability, invocation, output-decoding, and configuration-context handling. Absence or failure MUST NOT trigger silent fallback. Unrequested Git availability MUST NOT affect results.

Dependency updates and external-capability changes MUST identify affected trust boundaries, newly reachable input, privilege or filesystem implications, transitive exposure, and required regression evidence. A dependency MUST NOT acquire workspace-write or carrier-output capability merely for convenience.

## Safe reproduction and evidence handling

Security reproductions MUST use the smallest safe artifact that demonstrates the affected boundary. Prefer isolated temporary workspaces, synthetic non-sensitive payloads, explicit roots, no-follow observation, bounded sizes, and dry-run or planning behavior before mutation.

A reproduction involving mutation MUST declare intended effects, cleanup expectations, supported environment, and possible partial state. It MUST NOT target production, shared, privileged, or unrelated repositories. Special objects, malicious carriers, and resource-exhaustion inputs MUST be handled as sensitive test artifacts and MUST not be opened or executed outside the bounded test design.

Private reports and evidence MUST retain exact bytes when byte identity matters. Hashes MAY support evidence handling, but a calculated hash without a trusted expected value does not establish integrity or authenticity.

## Security fixes and regression evidence

A security fix is acceptable only when it:

- identifies the violated trust boundary or safety property;
- updates the owning specification or architecture only when accepted authority must change;
- preserves unrelated accepted semantics;
- includes a safe negative reproduction and regression evidence;
- verifies the corrected result and absence of prohibited effects;
- covers adjacent bypass forms and changed-precondition cases where applicable;
- preserves deterministic, exact-byte, diagnostic, stream, and process agreement requirements;
- records supported environment and capability assumptions;
- avoids publishing exploit detail before remediation when that detail materially increases risk.

Captured vulnerable output is compatibility or defect evidence, not desired conformance behavior. Security corrections MUST NOT normalize unsafe historical behavior into authority without an explicit compatibility decision.

## Current support limits

Security claims are bounded by verified platform and filesystem evidence. The controlling specifications currently verify Linux, Python 3.12, and overlayfs for the stated workspace and carrier boundaries. Other platforms, filesystems, case behavior, Unicode normalization behavior, permission models, terminals, and Python versions remain unverified unless later evidence expands support.

Portable design does not constitute a security guarantee for an unverified environment. This repository makes no cryptographic authenticity, carrier signing, supply-chain attestation, sandboxing, whole-workspace transaction, rollback, crash-recovery, or unrestricted platform claim.

## Disclosure expectations

Reporters and maintainers SHOULD coordinate privately until a correction and regression evidence are ready or the risk of continued private handling outweighs disclosure risk. Public disclosure SHOULD describe affected versions or states, impact, remediation, and remaining limits without exposing secrets or unnecessary exploit detail.

The repository does not promise a response deadline, remediation deadline, severity SLA, bounty, embargo duration, or universal support commitment.

## Authority boundary

This document owns security reporting expectations, trust-boundary security interpretation, safe reproduction, remediation evidence, and limits on security claims. Accepted specifications continue to own observable DX semantics. Architecture continues to own dependency and capability boundaries. Compatibility authority continues to own historical relationships. Contributor mechanics are owned by `CONTRIBUTING.md`, and sequencing is owned by `ROADMAP.md`.
