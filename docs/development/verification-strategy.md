# DX Verification Strategy

Status: Development planning
Owner: Implementation verification design and evidence composition
Scope: Evidence classes, executable test boundaries, and progression from architecture realization to release evidence

## Relationship to authority

This strategy maps Accepted obligations to executable evidence. It does not restate or replace normative rules. Tests reference owning paths and stable headings or named rules. Fixture representation, provenance, and updates remain governed by `tests/fixtures/README.md`; release sufficiency remains governed by `RELEASE.md`.

## Evidence classes

- **Architecture tests** protect dependency direction, capability isolation, composition, and side-effect invariants.
- **Semantic component tests** exercise pure carrier, workspace/path, selection, result, and planning behavior from explicit values.
- **Conformance tests** prove observable results against Accepted specifications using independently derived expectations.
- **Regression tests** preserve an accepted correction and identify the defect and governing rule.
- **Compatibility-characterization tests** preserve historical evidence without asserting desired behavior.
- **Compatibility-transition tests** verify an Accepted retain, replacement, or migration boundary end to end.
- **Security tests** target containment, no-follow behavior, unsafe objects, mutation authority, changed preconditions, resource bounds, streams, and disclosure boundaries.
- **Environment-support tests** prove claims for a declared platform, Python runtime, filesystem, terminal, and optional capability context.
- **Process and installed-artifact tests** verify public invocation, streams, numeric results, clean installation, and generated artifacts when packaging is admitted.
- **Property or generated tests** cover broad valid and invalid spaces where an independent invariant or reference model exists.
- **Reference-equivalence tests** compare future optimized behavior with correctness-first reference behavior.

A test has one primary evidence class. Historical characterization never becomes conformance merely because the current implementation passes it.

## Minimum executable harness

The first implementation slice needs only:

1. the repository's selected Python test runner or standard-library runner, recorded by the implementation carrier;
2. a test composition root able to instantiate semantic components without CLI, presentation, real filesystem, Git, or write capability;
3. a dependency-boundary check over the initial implementation surface;
4. independently authored in-memory cases and the first real fixture family admitted by fixture governance;
5. a bounded command that reports failures and skips explicitly.

No empty test directories, placeholder fixtures, fixture manifest, concrete machine encoding, or schema is created in the planning pass. Runner selection is implementation tooling, not product authority.

## Authority references in tests

Each test module or fixture family identifies its primary evidence class and governing authority path plus stable heading or named rule. Test names describe the verified outcome, not an implementation function. When one case supports several authorities, one remains primary and the others are referenced as dependencies.

Expected semantic results are authored from Accepted prose or an independent reference procedure. Directly captured implementation output is never the sole expected result. Byte-preservation cases retain source bytes, expected bytes, byte length, and SHA-256 where useful.

## Boundary verification

### Carrier exact bytes

Verify decoding, validation, encoding, ordering, escaping, text terminal-LF restoration, base64, invalid attributes, logical paths, duplicates, and logical end handling. Preservation claims compare bytes directly after decode and round trip. Repeated normative serialization is compared byte-for-byte in each claimed environment.

Generated malformed cases are appropriate only when the generator is independent of the parser under test and preserves the intended invalid condition.

### Logical paths and workspace observation

Test carrier logical-path validity without physical paths. Separately test workspace mapping from explicit context and typed observations. Integration tests use isolated temporary workspaces and no-follow observation for final and ancestor links, broken links, directories, permissions, collisions, and supported special objects. Special objects are capability-gated and never opened as regular files.

Unsupported environments or unavailable setup capabilities produce explicit unsupported or skipped evidence with a reason. A skipped test does not support a claim.

### Selection

Exercise the reference procedure using supplied candidate and rule facts. Verify deterministic membership, decisive outcome, all contributing provenance, stable ordering, enumeration-order independence, explicit optional Git facts, and no output-sink influence. Architecture tests prove that selection has no filesystem, environment, subprocess, Git-adapter, process, or presentation dependency.

### Read-only operations

Inspection, structural verification, and comparison are composed without write protocols. Side-effect tests snapshot relevant temporary roots and outputs before and after execution and verify no product mutation. Structural verification tests also prove that success is not elevated to authenticity, workspace agreement, or safe applicability.

### Immutable planning

Creation and application planning receive frozen semantic inputs and typed observations. Tests verify deterministic intended effects, findings, preconditions, and provenance; planning performs no mutation; and no public serializer exposes a plan. Mutation after source observation must be represented as changed input or precondition rather than silently substituted content.

### Preview and execution agreement

Preview renders facts from the exact accepted plan. Executors accept that plan and cannot discover, select, remap policy, or reinterpret read-only status. Agreement tests compare previewed intended effects with attempted effects, allowing only specified precondition revalidation and resulting changed-precondition or partial-failure evidence.

### Separate mutation capabilities

Composition and dependency tests prove that carrier-output execution receives no workspace-write capability and workspace execution receives no carrier-output capability. Negative construction tests demonstrate that read and planning operations cannot be assembled with write access accidentally.

### Changed preconditions and partial failure

Use controlled adapters to vary target, parent, containment, identity, content, permission, or sink observations after planning. Verify full preflight before mutation, per-effect revalidation, deterministic stop point, completed effects, failed effect, not-attempted effects, created parents, and resource-specific uncertainty. Tests must not assert rollback.

### Diagnostics and presentation agreement

Construct diagnostics only from retained semantic results and findings. Test stable symbolic meaning, typed resources, blocking status, effect state, uncertainty, and deterministic ordering. Human and machine presentations consume the same diagnostic interpretation. Agreement is semantic, not textual or structural. No machine encoding or field shape is selected until admitted separately.

### Process agreement

Process tests verify validated requests, streams, terminal refusal, byte-oriented input and output, machine-mode eligibility and purity, help and version isolation, incomplete delivery, and the Accepted numeric mapping. Process adapters are tested against stub semantic operations to prove they do not reevaluate semantics. End-to-end cases later confirm human, machine, and numeric agreement.

### Optional Git

Core tests run with no Git adapter. Adapter contract tests cover each requested capability independently, including unavailable executable, non-repository context, controlled configuration, undecodable or malformed output, and command failure. Integration tests are bounded to isolated repositories. No unrequested Git availability may alter selection.

### Compatibility transitions

For retained behavior, run current conformance through the public boundary. For intentional replacement, verify the Accepted current result and absence of accidental fallback. For migrations, verify the compatibility spelling, canonical semantic mapping, required deprecation finding, and transition boundary. `dx.py`, `unpack`, positional output, and `--json` migrations are scheduled after canonical semantic and process behavior exists.

### Packaging and environments

Packaging and clean-installation tests begin only after packaging is admitted. They verify generated artifact contents, sizes and digests, clean installation, canonical executable exposure, version agreement, dependencies, and representative conformance against installed artifacts.

Each supported-environment claim needs an identified platform, Python runtime, filesystem, terminal, and optional-capability context plus the applicable path, link, permission, stream, process, and installation evidence. Portable design alone is not evidence.

## Fixture progression

Create a fixture family only with the tests that consume real represented evidence. The first implementation slice creates carrier fixtures for framing, attributes, payload preservation, and logical paths sufficient for its vertical result. Later slices add workspace, selection, operation, diagnostic, process, and compatibility families as their executable boundary arrives.

Machine-result fixture content remains withheld until encoding and a concrete schema are Accepted. Historical carrier or output captures reside only under compatibility characterization with provenance.

## Verification gates per implementation carrier

Every implementation carrier must pass:

- focused scope and authority-reference review;
- architecture dependency and capability checks for affected boundaries;
- affected semantic component and conformance tests;
- applicable exact-byte, deterministic, security, regression, and compatibility checks;
- explicit accounting for skips and unsupported capabilities;
- documentation synchronization for changed implementation decisions;
- repository diff, link, placeholder, and generated-artifact checks.

A failing mandatory check, unexplained skip, implementation-derived expectation, or stronger support claim stops the carrier. Historical implementation tests may inform characterization but never establish redesigned-product conformance.
