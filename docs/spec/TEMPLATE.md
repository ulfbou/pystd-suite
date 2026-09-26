# Specification title

Status: Normative
Owner: Observable concern owned by this specification
Scope: Boundary within which this specification is authoritative
Maturity: Draft

## Purpose

State why this specification exists and which observable concern it owns.

## Scope

### In scope

Identify the inputs, outputs, operations, artifacts, or observable relationships governed here.

### Out of scope

Identify nearby concerns owned by product authority, architecture, ADRs, other specifications, schemas, workflow, or implementation.

## Observable behavior

Define the behavior precisely enough to determine conformance. Use **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** when their special strength improves clarity.

Do not prescribe replaceable modules, classes, functions, adapters, internal plans, exception types, algorithms, or storage layouts.

## Validation

Define applicable validity conditions and when invalidity becomes observable.

## Results and errors

Define observable success, negative results, failures, unsupported conditions, conflicts, or differences within this specification's scope. Do not assign process-level representation unless this specification owns it.

## Required verification

State the conformance evidence required for important normative rules. Reference stable headings or named semantic rules by default. Add requirement identifiers only when demonstrated complexity makes section-level traceability insufficient.

## Authority boundary

State what this specification owns and which adjacent concerns remain owned elsewhere.

---

## Conditional sections

Include the sections below only when they have content relevant to this specification. Remove unused sections rather than retaining empty ceremony.

## Terminology

Define only terms needed to interpret this specification. Terminology must not conceal undefined behavior.

## Inputs

Describe observable input forms and their interpretation.

## Outputs

Describe observable output forms and their interpretation.

## Determinism and environmental inputs

Identify environmental inputs that affect results and state how they are declared, resolved, eliminated, or reported.

## Safety properties

Define observable safety requirements and prohibited effects without prescribing replaceable mechanisms.

## Compatibility

Reference the applicable accepted compatibility classification. Define current behavior in this specification rather than duplicating it from compatibility authority.

If compatibility has not been decided, state that explicitly while the specification remains Draft.

## Applicable schemas

Name each admitted schema and its validation boundary, or state:

```text
None. This specification has no schema-governed boundary.
```

Prose owns semantics. A schema owns only its assigned machine-enforced structure.

## Examples

Examples are informative. Each example must conform to normative prose and must not introduce otherwise undefined behavior.

## Open decisions

Use only while `Maturity: Draft`. List decisions that block acceptance or explicitly bound work deferred beyond the current scope.

Remove this section, or resolve every conformance-blocking item, before changing maturity to Accepted.

## Specification use

Core sections are:

- Purpose;
- Scope, including in-scope and out-of-scope boundaries;
- Observable behavior;
- Validation;
- Results and errors;
- Required verification;
- Authority boundary.

A Draft specification is reviewable work, not an accepted behavioral contract. An Accepted specification is authoritative within its scope and contains no unresolved question that prevents conformance determination for that boundary.
