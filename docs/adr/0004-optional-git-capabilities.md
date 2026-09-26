# ADR 0004: Git as optional explicit external capabilities

Status: Accepted
Owner: Architectural decision record
Scope: Architectural role of Git-derived repository, candidate, status, and ignore facts

## Context

Existing DX implementation evidence uses Git for repository discovery, worktree candidate discovery, and ignore decisions. The product does not make Git an unconditional prerequisite, and core carrier and workspace operations must remain usable outside Git repositories.

Implicit use of Git when available would make results depend on executable availability and ambient configuration. Excluding Git entirely would prevent compatibility investigation of established Git-aware workflows.

## Decision

Git is not part of core DX semantics. It provides optional, independently requested external capabilities that translate Git results into explicit adapter facts.

Potential capabilities include repository-root information, worktree candidate facts, status facts, and ignore-decision facts. Selection remains functional without Git and consumes any accepted Git-derived facts as explicit input.

Git executable discovery, subprocess execution, output decoding, and allowed configuration context remain inside the Git integration boundary. Absence of Git is represented explicitly and never triggers silent fallback semantics.

Ambient global Git configuration does not influence selection unless a later compatibility authority explicitly accepts and reports it.

## Alternatives considered

### Require Git

Rejected because Git is not an unconditional product prerequisite and non-Git workspaces must remain usable.

### Use Git implicitly when available

Rejected because executable availability and ambient configuration would become hidden semantic inputs.

### One all-purpose Git provider

Rejected because repository, status, candidate, and ignore facts are distinct capabilities and need not be requested together.

### Separate optional Git capabilities

Accepted because it supports compatible Git-aware behavior without coupling core semantics to Git.

### Exclude Git entirely

Rejected because existing behavior demonstrates relevant compatibility and user-workflow pressure that must be investigated deliberately.

## Consequences

- Carrier processing and explicit filesystem-based selection work without Git.
- Requested Git capability has explicit availability and failure behavior.
- Git-derived compatibility requires separate evidence and specification.
- Semantic tests use adapter facts rather than Git subprocesses.
- The integration boundary must control configuration and output decoding deliberately.

## Verification impact

- Core selection and carrier tests run in environments without Git.
- Adapter contract tests cover each accepted Git capability independently.
- Absence and failure tests verify explicit outcomes without silent fallback.
- Configuration-isolation tests protect against undeclared ambient Git influence.
- Agreement tests ensure selection explanations identify relevant Git-derived input without rerunning Git.

## Supersession conditions

Supersession requires an accepted product requirement making Git universally necessary, or verified evidence that required compatibility cannot be delivered through explicit optional capabilities.

## Affected authorities

- `docs/ARCHITECTURE.md` integrates Git as an optional boundary.
- Future selection and compatibility specifications decide which Git-derived behaviors are accepted.
- Future CLI and process specifications define how requested capability and unavailability are exposed.
