# ADR 0001: Semantic core and explicit boundary dependency model

Status: Accepted
Owner: Architectural decision record
Scope: Dependency direction between DX semantics, orchestration, presentation, filesystem integration, and optional external capabilities

## Context

DX must provide deterministic carrier, workspace, selection, planning, and comparison semantics while interacting with filesystems, process streams, and optional Git capabilities. Existing implementation evidence combines these concerns, but that organization is not architectural authority.

A CLI-centered design or domain logic that performs direct I/O would make environmental inputs implicit, couple semantics to presentation and subprocess behavior, and weaken read-only guarantees and component verification.

## Decision

Separate carrier, workspace/path, selection, and operation semantics from process presentation and concrete filesystem or Git integrations.

Dependencies point from process and presentation through operation orchestration toward semantic domains. Filesystem and Git integrations enter orchestration through explicit boundaries. Semantic domains consume explicit values and narrow boundary contracts rather than concrete environment, process, or presentation facilities.

Mutation integrations are available only to mutation execution. Read-only operations receive observation capability only.

## Alternatives considered

### CLI-centered semantics

Keep parsing, semantic decisions, diagnostics, and I/O in command handlers. Rejected because invocation mechanics would define behavior and semantic tests would require process-level execution.

### Domain objects with direct I/O

Allow semantic objects to read filesystems, environment variables, or Git directly. Rejected because inputs would be hidden and read/write capability would be difficult to constrain.

### Generic service and repository layers

Introduce broad service abstractions intended for future tools. Rejected because DX does not justify a generic platform or speculative reuse boundary.

### Semantic core with explicit boundaries

Accepted because it keeps product decisions testable, environmental dependencies visible, and mutation authority narrow without promising a generic framework.

## Consequences

- Semantic behavior can be tested without CLI parsing, terminal formatting, a real filesystem, or Git.
- Environmental facts require explicit translation into semantic inputs.
- Orchestration must coordinate adapters and semantic values deliberately.
- Boundary values and typed outcomes add design work but make dependencies and failures visible.
- Human and machine presentation remain replaceable without redefining semantics.

## Verification impact

- Dependency checks prevent semantic domains from importing CLI parsers, presentation renderers, environment access, subprocess execution, or concrete mutation services.
- Component tests exercise carrier, workspace/path, selection, and operation semantics from explicit values.
- Composition tests verify that read-only operations receive no write boundaries.
- Human and machine rendering tests consume the same typed outcomes.

## Supersession conditions

Supersession requires a demonstrated alternative that preserves semantic determinism, explicit environmental inputs, read/write capability isolation, independent verification, and presentation independence with materially lower complexity.

## Affected authorities

- `docs/ARCHITECTURE.md` integrates this dependency model.
- Future specifications define observable behavior without prescribing these internal boundaries.
- Future workflow policy must enforce applicable dependency and component checks.
