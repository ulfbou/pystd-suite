# DX Machine-Schema Governance
Status: Normative
Owner: Machine-schema governance
Scope: Admission, ownership, validation boundaries, evolution, compatibility, and the relationship between DX machine schemas and prose
Maturity: Accepted

## Purpose
DX machine mode crosses a public validation boundary from the process producer to automation consumers, conformance tests, compatibility migration checks, and release verification. This authority governs structural validation at that boundary while preserving prose as the sole owner of semantic meaning.

## Admitted boundary
The admitted producer is DX machine-mode presentation. Admitted consumers and validators are automation invoking admitted machine-mode operations, conformance tests validating emitted structure, compatibility migration checks for historical machine output, and release verification when machine-contract conformance is claimed.

The present boundary admits schema governance but not a concrete schema artifact. `docs/spec/cli-process.md` deliberately leaves machine serialization encoding unspecified. Until an encoding is accepted, no `.schema.json` or other encoding-specific schema can truthfully define the public representation.

## Ownership
`docs/spec/operations.md` owns semantic results, effects, completion, satisfaction, uncertainty, and partial failure. `docs/spec/diagnostics.md` owns required machine-semantic information, identifiers, kinds, blocking status, typed resources, ordering, and human/machine agreement. `docs/spec/cli-process.md` owns machine-mode eligibility, purity, streams, delivery, and numeric process results.

A schema owns only admitted structure: field presence, primitive representation, object or sequence shape, structural constraints, and machine-enforceable syntax. Schema validity never establishes semantic validity unless Accepted prose explicitly says so. Schemas MUST NOT become alternate semantic authorities.

## Structural and semantic validation
Structural validation checks an emitted machine representation against the concrete schema admitted for its accepted encoding. Semantic validation checks the representation against the owning prose, including result meaning, required findings, effects, uncertainty, ordering, and process agreement. Conformance requires both when a concrete schema exists.

## Naming and location
Governance is `docs/schema/README.md`. A concrete DX machine-result schema, when admitted, uses `docs/schema/dx-machine-result` plus the conventional suffix for its accepted schema language and encoding. Schema identifiers MUST be stable, globally unambiguous identifiers appropriate to that schema language and MUST identify the public contract rather than a repository checkout path.

## Evolution
A concrete schema declares an explicit contract version through the mechanism accepted for its schema language and representation. Additive structural changes require review of producer, consumers, optionality, and semantic owners. A required field, removed field, narrowed accepted value, changed type, changed nesting, or changed interpretation is breaking unless all accepted consumers remain conforming by construction.

Any change affecting stable diagnostic identifiers, semantic results, required resources, effects, uncertainty, ordering, process agreement, or historical machine output triggers review under the owning prose and compatibility authorities. Schema evolution MUST NOT silently classify historical compatibility.

## Validation requirements
Before a concrete schema becomes active authority:
- serialization encoding and schema language MUST be Accepted;
- one complete interoperable public structure MUST be determined from Accepted prose;
- the schema MUST pass syntax and meta-schema validation using a standards-based validator;
- positive and negative conformance fixtures MUST demonstrate the boundary;
- producer output MUST be validated structurally and semantically;
- human and machine agreement and process-result agreement MUST be tested;
- internal plans and implementation details MUST be absent.

Release claims concerning the machine contract require the applicable schema validation and prose-conformance evidence.

## Fixtures and tests
Machine-result fixtures derive from Accepted prose and, when present, the concrete schema. Positive fixtures demonstrate structurally and semantically valid results. Negative fixtures isolate rejected structural forms or prose-semantic contradictions. Captured implementation output is evidence only and MUST NOT become expected conformance behavior without specification-first review.

## Prohibitions
No public schema may serialize internal plans, implementation exception names, Python types, module names, adapter identities, stack traces, arbitrary operating-system prose, presentation layout, or terminal formatting. A schema MUST NOT invent semantic enums, defaults, optionality, fields, or relationships unsupported by Accepted prose.

## Later-schema admission
Any later schema requires a structured public validation boundary, concrete producer and consumers or validators, present validation value, clear semantic owners, structural-only scope, and an evolution model that does not expose internal plans. Hypothetical reuse or an empty namespace is insufficient.

## Authority boundary
This document owns governance of the admitted DX machine structural-validation boundary. It does not select serialization encoding, define a concrete machine object, own semantic meaning, classify compatibility, define process behavior, or expose implementation structure.
