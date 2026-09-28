# DX Implementation Plan

Status: Development planning
Owner: Ordered implementation outcomes and implementation-carrier boundaries
Scope: Independently verifiable vertical outcomes from architecture realization through canonical executable exposure

## Planning rules

This plan sequences implementation outcomes, not file batches. Each outcome consumes Accepted authority, produces one coherent executable result, includes real tests and fixtures where applicable, and stops on failed boundary evidence. Internal file and package names remain replaceable unless a later consequential decision requires an ADR.

No outcome may select a machine encoding, expose internal plans, treat historical code as target structure, or make support and release claims beyond evidence.

## Outcome 1: Carrier semantic kernel and architecture harness

**Authorities:** `docs/ARCHITECTURE.md`; ADRs 0001 and 0003; `docs/spec/dx-carrier.md`; `tests/fixtures/README.md`.

**Prerequisites:** this implementation architecture and verification strategy; a bounded Python test command selected and recorded in the implementation change.

**Implementation result:** an importable, CLI-independent carrier semantic boundary that represents immutable logical paths, attributes, entries, and carriers; decodes bytes into syntax and validated content; rejects invalid or unsupported input through typed results; and deterministically serializes valid explicit content. A minimal composition seam and architecture checks make the boundary executable without filesystem, Git, process, presentation, or mutation dependencies.

**Tests and real fixtures:** architecture dependency tests; positive and negative framing and attribute fixtures; text, empty, terminal-LF, escaped terminator, base64, binary, and invalid payload fixtures; valid and rejected logical paths; duplicates; decoded-byte round trips; deterministic entry and attribute ordering. Exact bytes, lengths, and SHA-256 are recorded where preservation is claimed.

**Verification and stop conditions:** repeated serialization matches byte-for-byte in the declared test environment; recovered bytes equal intended bytes; carrier semantics import no prohibited integration; structural success makes no stronger claim. Stop on any ambiguous grammar interpretation, implementation-derived expected carrier, hidden environment input, or need for a public representation not already Accepted.

**Historical evidence:** characterize useful v2 parser and serializer cases from `dx.py` and `dxlib`, but derive expectations from `docs/spec/dx-carrier.md`. Historical v1.3.1 acceptance remains unspecified and is excluded.

**First implementation carrier:** implement only this outcome, including the minimum test harness, architecture checks, and real carrier fixtures required to prove it. Do not add CLI, workspace mapping, selection, mutation, packaging, machine encoding, or compatibility shims.

## Outcome 2: Workspace context and no-follow observation

**Authorities:** architecture; ADR 0003; `docs/spec/workspace-paths.md`; `SECURITY.md`.

**Prerequisites:** carrier logical-path values from Outcome 1.

**Implementation result:** explicit workspace context, logical-to-physical mapping semantics, typed no-follow observations, containment and collision decisions, and a read-only filesystem observer. Semantic mapping remains testable from supplied facts.

**Tests and fixtures:** mapping and containment fixtures; final, broken, and ancestor links; directories; missing parents; supported special objects; permission and observation failures; case and Unicode collisions where the environment supports them. Bounded temporary-workspace security tests classify objects without unsafe reads.

**Verification and stop conditions:** no link following, no out-of-root access, no mutation capability, explicit unsupported environment. Stop if the adapter cannot preserve semantic independence or a support claim lacks environment evidence.

## Outcome 3: Candidate discovery and pure selection

**Authorities:** architecture; ADRs 0001 and 0004; `docs/spec/selection.md`; workspace source-link rules.

**Prerequisites:** workspace observation boundary and logical-path values.

**Implementation result:** bounded filesystem candidate discovery, explicit candidate facts, optional separate Git fact adapters, and a pure reference selection implementation retaining decisive outcome and provenance.

**Tests and fixtures:** candidate-source, scope, selector, exclusion, ignore, override, `.git` protection, unavailable and unsupported source, deterministic union and ordering, optional Git absence and failure, and enumeration-order independence.

**Verification and stop conditions:** selection runs without filesystem, subprocess, environment, Git, output sink, process, or presentation access. Stop on implicit ignore or Git activation, hidden default exclusion, or content loading inside selection.

**Historical evidence:** characterize current discovery, ignore, pattern, and Git behaviors only under their accepted compatibility classifications.

## Outcome 4: Operation values and immutable planning foundation

**Authorities:** architecture; ADR 0002; `docs/spec/operations.md`; `docs/spec/diagnostics.md`.

**Prerequisites:** carrier, workspace, and selection values.

**Implementation result:** typed operation results, findings, effects, provenance, preconditions, uncertainty, distinct creation and application plan values, and narrow read and write protocols. No executor is implemented yet.

**Tests and fixtures:** immutability, deterministic ordering, plan non-serialization, result/finding consistency, capability construction, and no-mutation planning compositions.

**Verification and stop conditions:** read and plan boundaries have no write access; plans remain operation-specific and private. Stop if values require machine-field decisions or a generic plan.

## Outcome 5: Inspection and structural verification

**Authorities:** carrier, operations, diagnostics, and architecture specifications.

**Prerequisites:** Outcomes 1 and 4 plus carrier-byte acquisition boundary.

**Implementation result:** read-only inspection projections and bounded structural verification results with retained findings and trust limits.

**Tests and fixtures:** summary facts, paths, read-only entries, hashes, exact entry bytes, missing entry, malformed and unsupported carriers, acquisition failure, and no side effects.

**Verification and stop conditions:** no workspace or write dependency; structural success is not authenticity or integrity. Stop on presentation-driven semantics.

## Outcome 6: Workspace comparison

**Authorities:** workspace-path, operation, diagnostic, and architecture authorities.

**Prerequisites:** Outcomes 1, 2, 4, and 5.

**Implementation result:** read-only comparison over validated carrier content, explicit workspace context, and no-follow observations, including optional explicit workspace-only facts.

**Tests and fixtures:** identical, missing, different, read-only, workspace-only, directory, links, unsupported object, observation failure, containment, and identity collision.

**Verification and stop conditions:** no mutation intent, no link following, no deletion implication, deterministic differences. Stop if comparison reuses historical status letters as semantics.

## Outcome 7: Carrier-creation planning and output execution

**Authorities:** selection, carrier, operation, diagnostic, architecture, and ADR 0002.

**Prerequisites:** Outcomes 1 through 4.

**Implementation result:** selected-content loading, frozen payload facts, immutable creation plans, preview projection, deterministic serialization, separate non-filesystem and filesystem sink adapters, and carrier-output execution.

**Tests and fixtures:** readable and changed sources, arbitrary bytes, empty selection, sink success and incomplete delivery, filesystem conflicts, links, parents, replacement authority, self-reference, frozen payloads, and changed sink preconditions.

**Verification and stop conditions:** output sink cannot alter selection; executor receives no workspace-write capability and cannot rediscover or reload. Stop on incomplete delivery reported as success or hidden output exclusion.

## Outcome 8: Application planning and workspace mutation

**Authorities:** workspace-path, operation, diagnostic, security, architecture, and ADR 0002.

**Prerequisites:** Outcomes 1, 2, and 4; no dependency on carrier-output execution.

**Implementation result:** immutable application plans, preview projection, explicit existing-target and parent authority, full preflight, deterministic workspace executor, per-effect revalidation, and partial-failure evidence.

**Tests and fixtures:** create, satisfied, explicit fail/skip/overwrite, read-only satisfaction and discrepancy, parents, links, unsupported objects, permissions, changed preconditions, first and later write failure, interruption, completed and untouched effects, and uncertainty.

**Verification and stop conditions:** no raw-request execution, selection, silent replanning, link following, or rollback claim. Stop if the workspace executor can write carrier outputs.

## Outcome 9: Diagnostic interpretation and presentation agreement

**Authorities:** `docs/spec/diagnostics.md`; operation results; architecture presentation invariants.

**Prerequisites:** typed results and executable read, planning, and mutation outcomes.

**Implementation result:** presentation-neutral diagnostic interpretation plus human rendering. Machine rendering remains abstract until encoding is decidable; tests may compare semantic projections without selecting a public shape.

**Tests and fixtures:** required finding kinds, stable symbolic meanings, typed resources, ordering, warnings, suggestions, cause bounds, partial-failure reconstruction, and human/machine semantic agreement at the abstract-result level.

**Verification and stop conditions:** diagnostics never rerun semantics; no exception-class identifiers or machine fields become contract. Stop if machine consumers require a concrete encoding, then route that decision through schema governance.

## Outcome 10: CLI and process adaptation

**Authorities:** `docs/spec/cli-process.md`, diagnostics, operations, compatibility, security, and architecture.

**Prerequisites:** canonical semantic operations and diagnostic interpretation.

**Implementation result:** validated `dx` request grammar, stream and terminal boundaries, operation dispatch, help and version isolation, process mapping, and machine-mode adapter boundary without prematurely choosing encoding.

**Tests and fixtures:** commands and options, invalid requests before semantics, stdin, byte sinks, terminal refusal, dry run, output delivery failure, verbosity, process values 0 and 2 through 11, and human/process agreement.

**Verification and stop conditions:** process code owns no semantic decisions; no concrete machine serialization is claimed before its decision. Stop if canonical operation results cannot be represented without an authority change.

## Outcome 11: Compatibility transitions

**Authorities:** `docs/spec/compatibility.md` and each cited current owner.

**Prerequisites:** canonical process and semantic paths for the affected behavior.

**Implementation result:** admitted `dx.py`, `unpack`, positional output, and `--json` transition adapters with required deprecation findings; explicit absence of intentionally replaced behavior; retained stdin convention.

**Tests and fixtures:** one transition-boundary suite per migration; replacement and retained checks; historical characterization kept separate.

**Verification and stop conditions:** migrations map to canonical semantics and cannot bypass safety or planning. Stop on accidental preservation of unspecified v1.3.1 input or historical machine shape.

## Outcome 12: Packaging and canonical executable exposure

**Authorities:** roadmap, release policy, CLI/process specification, contribution and security policies.

**Prerequisites:** required semantic, process, conformance, security, and compatibility evidence; machine encoding decision if packaging claims machine mode.

**Implementation result:** admitted packaging metadata and canonical `dx` exposure selected through evidence current at that time.

**Tests and fixtures:** reproducible artifact generation, inventory, byte size and SHA-256, clean installation, version agreement, installed-artifact conformance, dependency review, and declared environment evidence.

**Verification and stop conditions:** no publication or support claim beyond evidence. Stop on unverifiable artifact, dirty-source dependency, or package-layout choice requiring an unresolved consequential decision.

## Carrier discipline

Each implementation carrier contains one smallest complete vertical outcome or a narrower independently executable subset that preserves the same boundary. It includes implementation, real tests, real fixtures, and any necessary synchronization together. It does not mix unrelated refactoring, pre-create future files, or redeliver unchanged state.
