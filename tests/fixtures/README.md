# DX Fixture Governance
Status: Normative
Owner: Fixture representation and evidence governance
Scope: Fixture classes, provenance, representation, byte identity, expected artifacts, updates, validation, and relationship to specifications and tests
Maturity: Accepted

## Purpose and authority boundary
Fixtures provide stable represented inputs and expected artifacts for continuing conformance, regression, compatibility characterization, architecture verification, and machine-boundary validation. Specifications and architecture govern expected meaning. Fixtures represent evidence and MUST NOT redefine product semantics.

The governing direction is specification to fixture or test to implementation to verification result. Captured implementation output does not create expected behavior.

## Fixture classes
- **Conformance fixtures** derive from Accepted specifications and verify required positive and negative behavior.
- **Regression fixtures** preserve an accepted correction and identify the governing rule and defect history.
- **Compatibility-characterization fixtures** preserve observed historical evidence without making it normative.
- **Architecture-test inputs** represent dependency, capability, or side-effect conditions when a stable represented input is useful.

A fixture has one primary evidence class. Related uses may be recorded, but compatibility evidence MUST NOT be relabeled as conformance without an accepted semantic decision.

## Representation
Fixtures use deterministic family directories and descriptive lowercase hyphenated names. Ordinary files and directories are preferred. Source bytes and expected decoded bytes are stored as exact bytes. Comparisons that claim preservation use exact byte length and SHA-256 and compare bytes directly.

Newline-sensitive text MUST preserve its intended terminal newline count. Binary content remains binary and MUST NOT be rewritten through text APIs. Logical carrier paths are represented separately from host paths. Workspace trees distinguish logical coordinates, physical entries, and expected observations.

Positive fixtures represent admitted valid behavior. Negative fixtures isolate one invalid, unsupported, conflict, or failure condition where practical and identify the expected semantic category without copying arbitrary implementation prose.

## Filesystem safety
Symlinks and special objects are created only by bounded test setup on an explicitly supported environment. Repository fixtures MUST NOT contain deceptive substitutes that are later treated as real links or devices. Inspection MUST use no-follow observation and MUST NOT open FIFOs, sockets, devices, or unknown objects as regular files. Hazardous fixtures use isolated temporary workspaces, explicit cleanup, and capability checks. Absence of a required capability produces an explicit unsupported or skipped test condition, never silent semantic substitution.

## Expected artifacts
Expected carrier bytes, decoded bytes, hashes, machine results, workspace observations, differences, effects, and diagnostics are owned by their governing specifications. Expected artifacts MUST be reviewed independently from the implementation under test. Regenerating expected output from that implementation and accepting it without specification comparison is prohibited.

Machine-result fixtures are admitted as a family now, but encoding-specific fixture artifacts wait until machine serialization encoding and a concrete schema are admitted. Once admitted, machine fixtures undergo schema validation and semantic agreement checks.

## Provenance
Every fixture family README or directly associated test metadata identifies:
- primary evidence class;
- governing specification paths and stable headings or named rules;
- origin of source bytes or observations;
- expected-result owner;
- environment assumptions and capability requirements;
- whether content is authored, historically captured, or generated independently from a specification.

Per-fixture metadata is required only when family-level provenance is insufficient. Universal requirement identifiers are not required.

## Manifest decision
No machine-validated fixture manifest is admitted in this pass. Deterministic directory structure, family governance, test-local declarations, and family-level provenance are sufficient. No present producer-consumer boundary requires one common structured registry of paths, digests, evidence classes, governing references, and relationships. A future manifest requires demonstrated cross-tool validation value and an accepted representation before a schema is created.

## Initial fixture-family inventory
The admitted families and purposes are:
- `carrier/framing-attributes`: headers, blocks, directives, attributes, and structural invalidity;
- `carrier/payload-preservation`: text, terminal newlines, escaping, base64, empty and arbitrary bytes;
- `carrier/logical-paths`: valid paths, rejected forms, Unicode, case distinction, and duplicates;
- `workspace/mapping-containment`: mapping, containment, collisions, and environment boundaries;
- `workspace/symlinks-special-objects`: bounded no-follow and unsupported-object safety;
- `selection/candidates-rules`: candidate sources, scope, selectors, exclusions, ignore facts, Git facts, override, provenance, and empty outcomes;
- `operations/creation-sinks`: loading, freezing, serialization, filesystem and non-filesystem delivery outcomes;
- `operations/inspection-verification`: projections, malformed carriers, supported structural claims, and trust limits;
- `operations/comparison`: identical, missing, different, workspace-only, conflict, unsupported, and observation relations;
- `operations/application-effects`: create, replace, satisfied, skip, read-only, parents, changed preconditions, deterministic order, and partial failure;
- `diagnostics/agreement`: identifiers, kinds, resources, blockers, ordering, uncertainty, and human/machine semantic agreement;
- `cli-process/streams-results`: request validation, stdin, stdout, stderr, terminal safety, machine purity, delivery failure, and numeric values;
- `machine-result/structure`: reserved as an admitted family, with content withheld until encoding and a concrete schema are admitted;
- `compatibility/characterization`: historical evidence kept distinct from conformance.

This inventory authorizes governed families, not placeholder payloads. A family directory is created only with a real verification artifact.

## Update and review
A fixture update identifies its evidence class, governing authority, reason, affected expected results, and compatibility implications. Conformance fixture changes require proof that Accepted semantics changed or the prior fixture was defective. Regression fixtures retain the correction rationale. Compatibility captures retain provenance and are not normalized into desired output.

Review verifies exact bytes where claimed, deterministic naming, safe filesystem handling, distinction among evidence classes, independent expected-result derivation, and absence of implementation-private material.

## Required verification
Fixture-governance conformance verifies:
- exact-byte round trips and digest calculations;
- newline-sensitive and binary preservation;
- safe logical-path and workspace-tree representation;
- bounded symlink and special-object setup without unsafe reads;
- positive and negative classification;
- provenance and expected-result ownership;
- distinguishable evidence classes;
- schema validation for machine fixtures when a concrete schema exists;
- no implementation-generated expectation treated as authority;
- no placeholder family content;
- no undeclared manifest or registry dependency.

## Authority boundaries
Accepted specifications own observable behavior. `docs/schema/README.md` owns machine-schema governance and any admitted concrete schema owns structure only. Architecture owns dependency and capability invariants. Tests execute verification. This document owns fixture representation, provenance, evidence classification, update discipline, and byte-comparison conventions only.
