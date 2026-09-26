# DX Specification System

Status: Normative
Owner: Specification system
Scope: Governance, ownership, interpretation, change, and verification of DX observable-behavior specifications

## Purpose

DX specifications define externally observable behavior precisely enough to determine whether an implementation conforms. They state what inputs, outputs, results, effects, failures, preservation guarantees, compatibility commitments, and process behavior apply without prescribing replaceable implementation structure.

This document governs the specification system. It does not define DX carrier grammar, path behavior, selection semantics, operation behavior, diagnostics, CLI syntax, process values, or machine-output fields.

## Authority relationships

Concern ownership determines authority.

- `docs/VISION.md` owns product identity, scope, users, product principles, and non-goals.
- `docs/ARCHITECTURE.md` owns responsibility boundaries, dependency direction, capability separation, environmental boundaries, and architectural invariants.
- `docs/adr/` records consequential architectural decisions and their rationale.
- This document owns specification governance.
- Domain specifications own continuing observable behavior within their declared scopes.
- A future `docs/schema/README.md` will govern schemas only when schema-governed interfaces exist.
- A future `tests/fixtures/README.md` will govern fixture representation, not product semantics.

A specification must respect product and architecture authority. Product or architecture authority does not substitute for a behavioral specification.

## What belongs in a specification

A statement belongs in a specification when it determines externally observable conformance, including questions such as:

- What input is valid or invalid?
- What output or result is observable?
- What does an operation mean?
- What is preserved?
- What is selected, rejected, skipped, or compared?
- What effects occur?
- What failure or negative result is observable?
- What environmental input affects the result?
- What compatibility is promised?
- What process behavior is exposed?

Architecture instead owns questions such as:

- Which responsibility evaluates a rule?
- Which dependencies are permitted?
- Which capability may perform I/O?
- Where is environmental state resolved?
- Which boundary may mutate?
- Which invariant constrains dependency direction?

Specifications must not name internal modules, classes, dataclasses, functions, adapters, plans, or exception types unless an item has independently become part of a public contract. Internal plans remain non-public architecture artifacts.

## Specification ownership

The admitted specification concerns are:

- `docs/spec/COMMON.md`: demonstrably shared observable behavior, when ready;
- `docs/spec/dx-carrier.md`: carrier-format and preservation semantics;
- `docs/spec/workspace-paths.md`: workspace-relative path and filesystem-boundary semantics;
- `docs/spec/selection.md`: packing selection semantics;
- `docs/spec/operations.md`: inspection, verification, comparison, creation, planning, and application semantics;
- `docs/spec/diagnostics.md`: human and machine diagnostic semantics;
- `docs/spec/cli-process.md`: invocation, streams, and process behavior;
- `docs/spec/compatibility.md`: accepted compatibility classifications.

These paths identify admitted future authorities. Their presence here does not imply that their behavior has been decided or that the files are ready to draft.

Each rule has one semantic owner. A document may summarize or reference another specification, but it must not duplicate that specification's normative rule.

## Shared behavior and COMMON.md

A rule belongs in `docs/spec/COMMON.md` only when all of the following are true:

- it is already accepted observable behavior;
- it applies identically to more than one specification domain;
- central ownership removes real duplication;
- central ownership does not erase meaningful domain differences.

Expected future reuse is insufficient. Domain specifications initially own their behavior. A later semantic refactoring may move a proven shared rule into `COMMON.md` while preserving references and verification traceability.

## Normative language

The keywords below provide concise conformance language:

- **MUST** and **MUST NOT** express mandatory conformance requirements.
- **SHOULD** and **SHOULD NOT** express strong defaults. A deviation is valid only when its reason and consequences are documented within the applicable authority or accepted exception.
- **MAY** expresses permitted behavior or capability.

Uppercase keywords are used when their special strength improves precision. A statement in a normative specification can remain binding through the document's owner and scope even when ordinary declarative wording is clearer. Not every normative sentence needs a keyword.

## Metadata and maturity

Every normative Markdown specification includes:

```text
Status: Normative
Owner: <owned observable concern>
Scope: <boundary of authority>
Maturity: Draft | Accepted
```

- **Status** identifies the document as normative authority by category.
- **Owner** names the concern owned by the document, not a person.
- **Scope** bounds the document's authority.
- **Maturity** distinguishes work under development from accepted conformance authority.

A Draft specification is reviewable work but is not an accepted behavioral contract. It may contain explicit open decisions and must not be used to make release or compatibility claims.

An Accepted specification is the current behavioral authority within its scope. It contains no unresolved question that prevents conformance determination for its accepted boundary.

`Supersedes:` and `Superseded by:` may be added only when an actual lifecycle transition requires them.

## Architecture and ADR boundaries

Specifications define continuing observable behavior. ADRs record consequential architectural choices, their alternatives, consequences, verification impact, and supersession conditions.

If an ADR motivates observable behavior, the applicable specification owns the behavior. It may reference the ADR for rationale without leaving the requirement solely in the ADR.

Specifications must preserve the accepted architecture, including:

- semantic independence from CLI and presentation;
- read-only operations without write capability;
- plan-mediated mutation without exposing internal plans as public contracts;
- separation of carrier paths from physical workspace paths;
- explicit environmental inputs;
- optional Git capabilities external to core selection semantics;
- explanations derived from the same semantic decisions as execution;
- reference behavior as semantic authority over optimizations.

## Implementation evidence

Existing `dx.py` and future implementations are evidence. They may reveal current behavior, edge cases, compatibility pressure, ambiguities, failure modes, and missing requirements.

Code and tests do not become normative merely because they exhibit behavior. When implementation and an Accepted specification disagree, the discrepancy must be classified and resolved. Either the implementation is corrected, or the specification is changed through the accepted semantic-change process. The specification is not silently reinterpreted to match code.

## Compatibility relationship

The specification system distinguishes:

1. **Compatibility evidence:** observed carriers, workflows, process behavior, machine output, tests, and implementation behavior.
2. **Compatibility decision:** retain, intentionally replace, migrate, or leave unspecified.
3. **Current domain semantics:** the behavior owned by the applicable domain specification.

Compatibility evidence is informative until accepted by `docs/spec/compatibility.md`.

Once a compatibility decision is accepted:

- `docs/spec/compatibility.md` records the relationship to the observed behavior;
- the applicable domain specification defines the resulting current semantics;
- the semantic rule is not duplicated in both documents.

For example, compatibility authority may record that existing carrier behavior is retained, while `docs/spec/dx-carrier.md` owns what the current retained behavior means.

## Prose and schemas

Prose owns semantics.

A machine schema may be admitted only when:

- structured data crosses a real validation boundary;
- an identified producer and consumer or validator exist;
- stable structural constraints provide value;
- prose semantics have a clear owning specification.

A schema may own object shape, field presence, primitive types, structural constraints, and machine-enforceable syntax assigned to it.

The applicable prose specification owns meaning, lifecycle, side effects, invariants, semantic relationships, errors, and compatibility semantics. Schema validity alone does not establish semantic validity unless the applicable specification explicitly makes that claim.

The absence of a schema is not a specification defect when no justified schema boundary exists.

## Examples

Examples embedded in normative specifications are informative.

- Examples MUST conform to normative rules.
- Examples MUST NOT introduce requirements.
- Edge-case behavior must be stated normatively before an example is relied upon as conformance evidence.
- If an example conflicts with normative prose, the prose governs and the example is corrected.
- An unexplained discrepancy between an example and its governing rule is a documentation defect.

## Fixtures and tests

The governing direction is:

```text
specification
    -> fixture or test
    -> implementation
    -> verification result
```

It is not:

```text
implementation
    -> captured output
    -> expected behavior
```

Tests may serve distinct purposes:

- conformance tests verify Accepted specifications;
- regression tests protect accepted corrections;
- compatibility-characterization tests record existing evidence before acceptance;
- architecture tests protect dependency and capability invariants.

These purposes must remain distinguishable. A compatibility-characterization test is not automatically a normative conformance test. Fixture organization and byte-comparison rules belong to the future `tests/fixtures/README.md`.

## Traceability

Traceability is lightweight by default.

Important normative rules use stable section headings or named semantic rules. Verification may reference specification paths, headings, and rule names. Universal requirement identifiers are not required because no demonstrated traceability problem currently justifies their maintenance cost.

A domain may introduce requirement identifiers later when its complexity makes section-level references insufficient. Such identifiers must have a continuing verification purpose and must not be added ceremonially.

Every important Accepted rule must be verifiable in principle. The applicable specification identifies required verification without prescribing replaceable test implementation.

## Unresolved and unspecified behavior

**Unresolved** means that a decision is still required before the applicable behavior can become Accepted normative behavior.

**Unspecified** means that the product deliberately makes no behavioral or compatibility guarantee within a clearly bounded area.

A Draft specification may contain an `Open decisions` section. An Accepted specification may not retain an unresolved question that prevents conformance determination within its accepted scope.

When behavior materially affects conformance, the specification must define it, mark it unresolved while Draft, or bound it explicitly as unspecified. Silence must not be used ambiguously. "Implementation-defined" is not a general escape hatch and requires a specific, justified boundary if ever admitted.

## Semantic change

Specification changes are classified as:

- **Clarification:** Improves wording without changing accepted semantics.
- **Compatible semantic extension:** Adds behavior without invalidating previously conforming use within the stated compatibility boundary.
- **Intentional behavioral change:** Changes accepted semantics deliberately.
- **Compatibility-affecting change:** Alters an accepted compatibility relationship or established usage expectation.
- **Specification correction:** Repairs an error in the specification and identifies affected implementation and evidence.
- **Removal or deprecation:** Withdraws or phases out accepted behavior when such lifecycle treatment has been established.

A semantic change considers:

- product authority;
- architectural constraints and affected ADRs;
- compatibility authority;
- applicable fixtures and tests;
- schemas, when present;
- examples;
- release implications.

Repository mechanics for proposing, reviewing, and applying changes belong to future contribution policy.

## Conflict resolution

Resolve conflict by concern ownership, not by a universal precedence list.

If two specification documents appear to define the same semantic rule:

1. identify the intended owner;
2. consolidate the rule in that document;
3. replace duplication elsewhere with a reference;
4. treat unresolved dual ownership as a documentation defect.

If architecture and a specification appear to conflict, determine whether the disputed statement is architectural or behavioral. The authority owning that concern governs, and the document that crossed its boundary is corrected.

If an example, test, schema, implementation, or compatibility observation conflicts with an Accepted semantic rule, it does not silently override the specification.

## Specification admission

A new normative specification document earns a place only when:

- it owns a distinct observable concern;
- the concern cannot be owned cleanly by an existing specification;
- enough behavior is accepted to justify permanent authority;
- its scope and dependencies are explicit;
- it has a continuing verification or maintenance purpose.

An architectural domain does not automatically require a specification file. A file is not created merely to reserve a future authority.

## Authority boundary

This document governs how DX behavioral specifications are owned, interpreted, changed, and verified.

It does not define actual carrier grammar, path semantics, selection behavior, operation semantics, diagnostic categories, CLI syntax, process values, machine-output fields, contributor mechanics, release procedure, or roadmap sequencing. Those concerns require their admitted owning authorities and sufficient evidence.
