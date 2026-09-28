# Release Policy

Status: Policy
Owner: Release eligibility, release evidence, artifact verification, and release records
Scope: Evidence and gates required to make a pystd-suite release claim

## Purpose

A release is an evidence-backed claim that identified artifacts satisfy the Accepted authorities and declared support boundary. This policy determines release eligibility, blocking conditions, required evidence, artifact verification, release records, and failed-gate handling.

Accepted specifications continue to own observable behavior. `docs/ARCHITECTURE.md` owns dependency and capability boundaries. `docs/spec/compatibility.md` owns historical relationships and migration obligations. `SECURITY.md` owns security expectations. `CONTRIBUTING.md` owns contribution mechanics. `ROADMAP.md` owns sequencing. This policy does not create or modify those authorities.

## Release candidate identity

Every release evaluation MUST identify one immutable candidate state and the complete artifact set produced from it. The candidate record MUST include:

- the repository revision or other immutable source-state identifier;
- the proposed public version identifier, without deriving it from an unstated versioning scheme;
- the complete admitted change set since the preceding released state, when one exists;
- the authority changes, compatibility classifications, security implications, and known limitations associated with that change set;
- the supported environment claims being evaluated;
- the reproducible artifact-generation procedure and declared environment;
- the evidence set used by every applicable gate.

This policy does not prescribe semantic versioning, a numbering form, a release cadence, or a publication destination. A version identifier is acceptable only when it is explicit, unique within the project's release records, present consistently in applicable artifacts and documentation, and supported by retained change evidence.

## Release eligibility

A candidate is release-eligible only when all applicable gates in this policy pass against the same identified candidate state and artifact set.

Eligibility requires:

1. all observable behavior claimed by the release is owned by Accepted specifications;
2. architecture realization conforms to current architecture and Accepted ADR consequences;
3. every compatibility-affecting change is classified and every applicable migration boundary is implemented and verified;
4. security-relevant trust boundaries and regression obligations are satisfied;
5. required conformance, fixture, deterministic, safety, exact-byte, process, and environment evidence passes;
6. release artifacts are generated reproducibly for the declared environment and verified after generation;
7. installation and public executable exposure are verified for every environment claimed by the release;
8. machine output is validated structurally when a concrete schema is active and semantically against owning prose;
9. public documentation matches the candidate's actual behavior, availability, support, compatibility, and limitations;
10. the release record is complete and traceable to retained evidence.

Eligibility is not equivalent to publication. Publication mechanics and destinations may be established separately, but they MUST NOT weaken these gates.

## Blocking conditions

A candidate is blocked when any of the following applies:

- an applicable specification is Draft, unresolved, contradictory, or absent;
- implementation behavior conflicts with an Accepted specification;
- an architectural invariant or required dependency or capability boundary is violated;
- a compatibility trigger lacks classification, a migration obligation lacks a complete transition boundary, or a required transition is unverified;
- a known security defect affects the claimed release boundary without an accepted disposition consistent with `SECURITY.md`;
- required conformance, regression, safety, deterministic, exact-byte, packaging, installation, or environment evidence is missing, failing, irreproducible, or tied to a different candidate state;
- a concrete machine schema exists but applicable output fails structural or prose-semantic validation;
- fixtures or expected results were generated from the implementation under test without independent authority-based review;
- an artifact is missing, unverifiable, incomplete, unexpectedly different, or not traceable to the identified source state;
- public claims exceed retained evidence, including implementation completeness, compatibility, security, portability, support, installation, or release readiness;
- known limitations are omitted, understated, or contradicted by public documentation;
- placeholders, skipped mandatory checks, unexplained exceptions, or unresolved action items remain;
- implementation output, tests, fixtures, schemas, generated files, or historical code are treated as authority;
- required documentation is inconsistent or not synchronized with the candidate;
- the release record is incomplete.

A waiver MUST NOT convert a failed mandatory gate into a passing release claim. The underlying authority or this policy must be changed through its normal review process before the candidate can be reevaluated.

## Required authority evidence

### Specifications

Evidence MUST show that every claimed operation, carrier behavior, workspace relationship, selection rule, diagnostic meaning, invocation and process result, compatibility relationship, and machine boundary is governed by its owning Accepted authority.

Required checks MUST demonstrate conformance rather than merely cite document presence. No Draft specification, implementation observation, example, or captured output may support a release claim as if it were Accepted semantics.

### Architecture

Evidence MUST demonstrate applicable architectural invariants, including semantic independence from CLI and presentation, explicit environmental facts, read-only operations without write capability, operation-specific plan-mediated mutation, separate workspace and carrier-output capabilities, carrier/workspace path separation, optional Git boundaries, execution/explanation agreement, and reference behavior over optimization.

Dependency checks, component tests, composition tests, and side-effect checks MUST cover the realized architecture. Internal package or module organization is not release authority.

### Compatibility

Every release change MUST be assessed for compatibility triggers. Evidence MUST map each affected historical relationship to `docs/spec/compatibility.md` and verify applicable retain, intentionally replace, migrate, or unspecified treatment.

Retained behavior requires conformance evidence. Intentional replacement requires evidence that the current contract is implemented without accidental historical fallback. Migration requires end-to-end verification of the complete transition boundary, including deprecation behavior and removal constraints where stated. Unspecified behavior MUST NOT be presented as compatible.

### Security

Security evidence MUST cover changed trust boundaries and the applicable expectations in `SECURITY.md`. It MUST include regression evidence for corrected vulnerabilities and safety-sensitive behavior, plus adjacent bypass and changed-precondition cases where applicable.

A release record MUST disclose security-relevant known limitations without exposing secrets or unnecessary exploit detail. This policy creates no response timeline, severity SLA, signing system, attestation system, bounty, cryptographic guarantee, or rollback guarantee.

## Conformance evidence

The release evidence set MUST include all tests and independent checks required by the Accepted authorities for the candidate's claimed boundary. At minimum, applicable evidence covers:

- valid and invalid carrier framing, attributes, payloads, paths, versions, and decoded-byte round trips;
- workspace mapping, containment, links, special objects, collisions, permissions, and changed preconditions;
- deterministic selection, retained decision provenance, explicit inputs, and empty outcomes;
- creation, inspection, structural verification, comparison, planning, application, no-op, delivery, and partial-failure behavior;
- diagnostic identifiers, required context, ordering, uncertainty, and human/machine agreement;
- invocation grammar, streams, terminal safety, machine purity, incomplete delivery, and numeric process results;
- architecture dependency and capability boundaries;
- compatibility-transition behavior;
- security-sensitive negative cases;
- every supported-environment claim.

A passing count alone is insufficient. Evidence MUST identify the candidate state, commands or procedures, declared environment, results, failures or skips, and retained outputs needed to reproduce the claim. A mandatory check that was skipped or could not execute blocks the affected claim.

## Fixture and test evidence

Fixture use MUST comply with `tests/fixtures/README.md`. The evidence set MUST distinguish conformance, regression, compatibility-characterization, architecture, security, and environment-support purposes.

Expected artifacts MUST derive independently from Accepted authority. Captured implementation output MUST NOT become expected conformance behavior through approval alone. Exact-byte fixtures MUST be compared as bytes, and newline-sensitive or binary data MUST not be normalized through text handling.

Fixture provenance, governing authority, environment requirements, and expected-result ownership MUST be reviewable. Placeholder fixture families and unverifiable generated expectations block release.

## Machine-schema evidence

When no concrete machine schema is active, prose semantics remain the release authority and no encoding-specific schema claim may be made.

When a concrete schema is active, release evidence MUST include:

- validation of the schema against its accepted schema language and applicable meta-schema;
- positive and negative structural fixtures;
- validation of produced machine representations against the schema;
- semantic conformance against the owning operation, diagnostic, and CLI/process specifications;
- human, machine, and numeric-process agreement;
- compatibility review for structural or semantic changes;
- proof that internal plans and implementation-private types are absent.

Schema validity alone does not establish semantic conformance.

## Packaging and installation evidence

A release that claims installable artifacts or executable exposure MUST verify the actual generated artifacts rather than repository source alone.

Evidence MUST identify:

- the declared generation environment and reproducible procedure;
- the complete artifact inventory;
- artifact byte sizes and SHA-256 values;
- artifact contents and absence of unintended files, secrets, temporary data, local plans, caches, and development-only material;
- dependency inventory and applicable security review;
- installation into a clean declared environment;
- invocation through the claimed public executable identity;
- version output agreement with the release record;
- execution of representative and required conformance checks against the installed artifact;
- uninstall or replacement behavior only when such behavior is actually claimed and verified.

This policy does not select a package format, build backend, registry, publishing destination, hosting provider, or CI vendor.

## Artifact generation and verification

Artifacts MUST be generated from the identified candidate state by a documented, repeatable procedure using declared inputs and an identified environment. Generated artifacts MUST NOT be edited after generation.

For every release artifact, the release record MUST retain:

- exact filename or artifact identity;
- byte size;
- SHA-256 digest;
- generation input state;
- generation procedure and environment;
- verification procedure and result;
- relationship to the claimed public version and supported environments.

Where an artifact contract promises deterministic bytes for identical complete inputs in a declared environment, repeated generation MUST be compared byte-for-byte. Where byte identity is not promised, semantic equivalence MUST be verified under the owning authority and no byte-reproducibility claim may be made.

A digest calculated after generation supports identity evidence. It does not establish authenticity, trusted integrity, provenance, signing, or attestation without a separately accepted trust mechanism.

Carrier artifacts MUST be reparsed and structurally verified with the applicable authoritative codec, cleanly decoded or applied as appropriate, and compared byte-for-byte with intended source or decoded files where preservation is claimed.

## Supported-environment evidence

Every supported platform, Python version, filesystem, terminal, Git capability, installation context, and packaging claim requires reproducible evidence for the affected boundary.

Evidence MUST identify the actual environment and cover applicable case, Unicode, path, containment, symlink, special-object, permission, replacement, stream, process, installation, dependency, and external-capability behavior. Portable design or success in a different environment is insufficient.

Unverified environments MUST remain explicitly unverified. A release MAY support a bounded environment set. It MUST NOT imply broader support through omission or general wording.

## Known limitations

Every release record and public release-facing documentation MUST identify limitations material to safe or correct use, including:

- unverified or unsupported environments;
- intentionally unspecified behavior;
- incomplete optional capabilities;
- compatibility replacements and active migration obligations;
- absent concrete machine schema where relevant;
- security, filesystem, stream, packaging, or recovery boundaries;
- any accepted non-goal that a reasonable user could otherwise mistake for current capability.

A known limitation MUST identify its owning authority or evidence boundary. Limitations MUST NOT be phrased as hidden future promises or used to excuse a failed mandatory gate inside the claimed release boundary.

## Documentation synchronization

Before release eligibility is asserted, permanent public and contributor documentation MUST match the candidate state.

Synchronization includes:

- `README.md` status, availability, capability, support, compatibility, and development guidance;
- Accepted specifications and architecture references;
- `CONTRIBUTING.md`, `SECURITY.md`, `ROADMAP.md`, and this policy;
- schema and fixture governance and any admitted artifacts;
- version and change evidence;
- installation or usage guidance only when verified artifacts make it truthful;
- known limitations and supported-environment claims.

The README remains an entry point and MUST NOT reproduce release gates or semantic rules. Historical `dx.py` or `dxlib` implementation structure MUST NOT be presented as the released redesigned product unless separately proven by the candidate evidence.

## Release record

A complete release record MUST contain:

- public version identifier;
- immutable source-state identifier;
- release artifact inventory with filenames or identities, sizes, and SHA-256 digests;
- artifact-generation procedure and declared environment;
- change evidence since the preceding release, when one exists;
- specification and architecture conformance results;
- security review result and applicable regression evidence;
- compatibility classifications affected and transition-verification results;
- fixture and test evidence summary with failures and skips explicitly reported;
- machine-schema validation evidence when a concrete schema exists;
- packaging, clean-installation, executable, and version-agreement evidence when claimed;
- supported environment matrix bounded to verified claims;
- known limitations;
- documentation synchronization result;
- final gate result and any blocking conditions.

The record MUST link or identify retained evidence precisely enough for independent reproduction. It MUST NOT contain placeholders, silently omitted failed checks, unsupported claims, or unverifiable artifact references.

## Failed-gate handling

A failed gate produces a blocked candidate. The candidate MUST NOT be described as released, release-ready, conforming within the failed boundary, or supported for the affected environment.

Resolution requires one of:

- correcting implementation or artifacts to satisfy existing authority;
- correcting defective tests, fixtures, documentation, or evidence while preserving Accepted semantics;
- changing an owning authority through the applicable accepted process, followed by complete dependent updates and reevaluation;
- narrowing the proposed release claim so that the excluded capability or environment is not implied, provided the remaining release boundary is coherent and all its gates pass.

After any candidate or authority change, affected evidence MUST be regenerated. Evidence from a different byte state MUST NOT be reused as proof without demonstrating continued applicability. Failed checks, unresolved blockers, and superseded evidence remain visible in the evaluation record until replaced by a complete passing evaluation.

## Prohibitions

A release MUST NOT:

- claim unsupported behavior, compatibility, security, portability, environment coverage, installation, packaging, or readiness;
- contain placeholders or unverifiable artifacts;
- treat implementation behavior, generated output, tests, fixtures, schemas, or historical code as semantic authority;
- report structural verification as authenticity or trusted integrity;
- imply signing, attestation, rollback, transactionality, crash recovery, or publication guarantees not established elsewhere;
- invent a versioning scheme, release cadence, package format, publication destination, or provider-specific process;
- omit known blockers, failed required checks, partial state, uncertainty, or relevant limitations;
- mix evidence from different candidate states without explicit, verified traceability.

## Authority boundary

This document is the sole authority for release eligibility, release blockers, release evidence, artifact verification, release records, and failed-gate handling.

It does not own observable DX behavior, architecture, historical classifications, security expectations, contributor mechanics, project sequencing, implementation planning, package layout, machine encoding, publication infrastructure, or version-number policy.
