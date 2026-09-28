# Contributing to pystd-suite

Status: Policy
Owner: Contributor workflow, evidence, review, and acceptance gates
Scope: Repository contribution mechanics for documentation, architecture, specifications, schemas, fixtures, implementation, and tests

## Purpose

Contributions advance pystd-suite through focused, evidence-backed changes that preserve the repository's authority boundaries. Accepted specifications remain the authority for observable DX behavior, architecture remains the authority for dependency and capability boundaries, and compatibility authority remains the owner of historical relationships.

This document governs how changes are prepared, verified, reviewed, and accepted. It does not define security reporting, roadmap priority, release procedure, versioning, package layout, continuous-integration vendor configuration, hosting workflow, or implementation planning.

## Authority relationships

Contributors MUST identify the authority that owns each affected concern before changing it.

- `docs/VISION.md` owns product identity, scope, users, principles, and non-goals.
- `docs/ARCHITECTURE.md` owns responsibility boundaries, dependency direction, capability separation, environmental boundaries, and architectural invariants.
- `docs/adr/` records consequential architectural decisions and their rationale.
- `docs/spec/README.md` governs specifications, and each Accepted domain specification owns observable behavior within its scope.
- `docs/spec/compatibility.md` owns admitted historical classifications and migration obligations.
- `docs/schema/README.md` governs public machine-schema admission and structural validation.
- `tests/fixtures/README.md` governs fixture representation, provenance, and evidence classes.
- `SECURITY.md` owns repository security reporting and security expectations.
- `ROADMAP.md` owns sequencing and readiness, not behavioral authority.

A lower-level artifact MUST NOT silently redefine an owning authority. Implementation, tests, fixtures, schemas, examples, and generated output are evidence or realizations of accepted authority, not substitutes for it.

## Specification-first workflow

A contribution that changes observable behavior MUST begin with the owning specification and compatibility review where applicable. The required order is:

1. identify the owning authority and affected boundaries;
2. classify the change;
3. update or establish accepted authority before relying on implementation behavior;
4. update dependent schemas, fixtures, tests, examples, and implementation as applicable;
5. run the required verification and retain reproducible evidence;
6. review the complete change for boundary, compatibility, safety, and documentation consistency.

Implementation-first discovery MAY provide evidence, but observed implementation behavior does not become normative without an accepted semantic decision.

## Change classification

Every contribution MUST be classified as one or more of:

- clarification;
- compatible semantic extension;
- intentional behavioral change;
- compatibility-affecting change;
- specification correction;
- removal or deprecation;
- architectural change;
- implementation-only conformance work;
- test, fixture, or verification correction;
- security correction;
- documentation-policy change.

The classification determines the authorities, compatibility review, evidence, and acceptance gates that apply. A change presented as implementation-only MUST NOT alter observable behavior, public structure, compatibility commitments, safety properties, or supported-environment claims.

## Focused changes

A contribution MUST have one coherent purpose and the smallest complete set of dependent changes needed to preserve repository consistency. Unrelated cleanup, speculative abstraction, opportunistic renaming, and formatting churn MUST be excluded.

The contribution description MUST identify:

- the problem or accepted outcome;
- the owning authorities;
- the change classification;
- affected observable or architectural boundaries;
- compatibility and security impact;
- verification performed and evidence retained;
- known limitations or unsupported environments.

A focused contribution may span several files when those files form one necessary authority-to-evidence chain.

## Responsibility by artifact type

### Architecture and ADRs

Architectural changes MUST preserve product authority and distinguish continuing architecture from historical rationale. A consequential decision with credible alternatives, substantial future constraint, and meaningful reversal cost requires an ADR. Accepted architectural consequences MUST be integrated into `docs/ARCHITECTURE.md`.

Architecture changes MUST identify affected dependency checks, capability-isolation checks, side-effect checks, and component boundaries. They MUST NOT define observable semantics that belong to specifications.

### Specifications

Specification changes MUST follow `docs/spec/README.md`, preserve one semantic owner per rule, and state behavior precisely enough for conformance determination. Accepted specifications MUST contain no unresolved question that prevents conformance within their accepted scope.

A change to observable behavior MUST update the owning specification before dependent implementation expectations are accepted. Duplicated normative rules MUST be consolidated under one owner and replaced elsewhere by references.

### Compatibility

Compatibility review is required when a change affects an established invocation, carrier, process result, machine result, selection rule, workspace behavior, diagnostic identifier, stream contract, schema boundary, migration obligation, or historically evidenced workflow.

Review MUST determine whether the historical relationship is retained, intentionally replaced, migrated, or left unspecified. Migration requires a complete transition boundary. Current semantics remain in their domain specification and MUST NOT be duplicated in compatibility authority.

### Schemas

A schema contribution MUST satisfy `docs/schema/README.md`. It requires an admitted public validation boundary, accepted encoding and structure, identified producers and consumers or validators, standards-based structural validation, and semantic conformance against owning prose.

Schemas MUST NOT invent semantic meaning, expose internal plans, or classify compatibility. Generated schema derivatives do not replace the authoritative schema source.

### Fixtures

Fixture contributions MUST follow `tests/fixtures/README.md`. Each fixture has a primary evidence class, governing authority, provenance, expected-result owner, environment assumptions, and exact representation requirements.

Expected artifacts MUST be derived independently from accepted authority. Regenerating expectations from the implementation under test and accepting them without specification comparison is prohibited. Placeholder fixture families are prohibited.

### Implementation

Implementation MUST conform to Accepted specifications and architecture. Internal organization, algorithms, and optimizations are replaceable unless separately accepted as public behavior or architecture.

Implementation changes MUST preserve read-only boundaries, explicit environmental inputs, plan-mediated mutation, separation of carrier and workspace paths, separate workspace and carrier-output capabilities, optional external capabilities, and execution/explanation agreement.

An optimization MUST demonstrate equivalence with accepted reference semantics. Historical `dx.py` or `dxlib` organization is evidence only and MUST NOT be treated as the target architecture.

### Tests

Tests MUST state which authority and behavior they verify. Conformance, regression, compatibility-characterization, architecture, security, and environment-support tests MUST remain distinguishable.

Tests MUST NOT establish expected behavior from captured implementation output alone. Negative tests SHOULD isolate one rejected condition where practical. Tests involving links, special objects, mutation, streams, or partial failure MUST use bounded setup and preserve safety evidence.

## Verification and evidence

Verification MUST be proportionate to affected authority and risk. Applicable evidence includes:

- specification and authority consistency checks;
- parser, serializer, and exact-byte round trips;
- byte lengths and SHA-256 values where preservation is claimed;
- deterministic repeated execution from identical declared inputs;
- positive and negative conformance tests;
- reference-equivalence and generated tests for optimized semantics;
- no-follow link and unsupported-object checks;
- containment, collision, replacement, changed-precondition, and partial-failure checks;
- human, machine, and process-result agreement;
- dependency and capability-boundary checks;
- proof that read and planning operations perform no product mutation;
- schema syntax, meta-schema, structural, and prose-semantic validation when a concrete schema exists.

Evidence MUST be reproducible from repository-controlled inputs and declared environmental facts. A verification claim MUST identify the command or procedure, relevant inputs, environment, result, and retained artifact when applicable. Unsupported or skipped capability MUST remain explicit.

## Determinism, safety, and exact bytes

Changes affecting selection, carrier representation, serialization, path mapping, comparison, planning, mutation, diagnostics, machine output, or process behavior MUST verify applicable deterministic and safety properties.

Exact-byte claims require direct byte comparison. Text rendering, decoded previews, line-oriented diffs, and normalized output are insufficient for byte-preservation claims. Newline-sensitive and binary fixtures MUST be handled through byte-preserving operations.

Safety-sensitive verification MUST cover the actual boundary being changed and MUST NOT follow symlinks, open special objects as regular files, broaden mutation authority, conceal changed preconditions, imply rollback, or report incomplete output as success.

## Supported-environment claims

A platform, filesystem, Python version, terminal behavior, external capability, or portability claim may be added only with reproducible conformance evidence for the claimed boundary. Design intent is not support evidence.

Evidence MUST identify relevant platform and filesystem facts and cover affected case, Unicode, path, link, permission, replacement, stream, process, and external-capability behavior. Unverified environments remain unverified and MUST NOT be described as supported by implication.

## Documentation synchronization

A contribution MUST update every directly affected authority, reference, example, fixture-governance statement, and verification description needed to keep the repository coherent. It MUST NOT perform unrelated documentation cleanup.

Changes to headings or paths used for traceability require inbound-reference review. Deleted or superseded authorities require removal or correction of active references. Documentation MUST distinguish current authority, historical evidence, future work, and implementation detail.

## Generated artifacts

A generated artifact MUST identify its authoritative source and reproducible generation boundary. Generated output MUST NOT be edited as an alternate authority when its source controls the result.

A contribution that changes generated output MUST include the controlling source change and verification that regeneration is deterministic for the claimed environment. Generated expectations MUST still be reviewed against the applicable specification and MUST NOT be accepted solely because a generator produced them.

Generated files, caches, local plans, temporary evidence, and build output MUST NOT be committed unless an admitted repository authority gives them a continuing purpose.

## Review and acceptance gates

A contribution is acceptable only when all applicable gates pass:

1. **Scope:** the change is focused and contains no unrelated modifications.
2. **Authority:** every rule has one owner and authority boundaries remain intact.
3. **Specification:** observable behavior is governed by Accepted prose before implementation expectations are accepted.
4. **Architecture:** dependency, capability, read/write, and environmental boundaries are preserved.
5. **Compatibility:** every triggered historical relationship is reviewed and any migration boundary is complete.
6. **Security:** safety-sensitive effects and reporting obligations comply with `SECURITY.md`.
7. **Evidence:** required positive, negative, deterministic, exact-byte, and environment-specific checks pass.
8. **Synchronization:** directly affected documentation, schemas, fixtures, tests, and implementation agree without duplicated authority.
9. **Claims:** support, conformance, compatibility, and readiness claims do not exceed retained evidence.
10. **Completeness:** no placeholders, hidden unresolved decisions, implementation-generated authority, or unexplained verification gaps remain.

Review rejection is required when a contribution silently changes semantics, weakens a safety invariant, invents authority in a schema or fixture, relies on unsupported environment assumptions, or cannot provide the evidence needed for its claims.

## Authority boundary

This document owns contributor mechanics, evidence expectations, review requirements, and acceptance gates. It does not own DX observable semantics, architecture, historical classifications, security reporting, roadmap sequencing, release procedure, versioning, packaging, hosting workflow, CI-vendor configuration, or implementation planning.
