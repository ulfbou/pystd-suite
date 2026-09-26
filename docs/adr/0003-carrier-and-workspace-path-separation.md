# ADR 0003: Carrier and workspace path separation

Status: Accepted
Owner: Architectural decision record
Scope: Separation between transported carrier paths and physical workspace interpretation

## Context

DX transports logical paths between workspaces, while application and comparison operate against local filesystems with platform-dependent behavior. Treating transported path text as a physical local path would make carrier meaning depend implicitly on the active host and could conflate carrier validity with destination safety.

The product requires platform-neutral carrier paths, workspace-relative interpretation, portability by design, and explicit safety treatment.

## Decision

Carrier paths are logical transported values. Physical workspace interpretation occurs only when an operation relates a validated carrier entry to an explicit workspace context containing resolved filesystem observations.

Carrier representation owns transported path text, payload bytes, attributes, and carrier validity. Workspace interpretation owns physical resolution, containment, links, permissions, conflicts, and replacement conditions.

Carrier validity does not imply safe applicability to every workspace. Workspace unsuitability does not by itself make the carrier malformed.

## Alternatives considered

### Use local path strings directly

Rejected because carrier meaning would inherit host separators, roots, and implicit filesystem behavior.

### Normalize carrier paths according to the active host

Rejected because the same carrier could acquire different validity or identity across environments before an operation intentionally maps it to a workspace.

### Preserve distinct carrier and workspace concepts

Accepted because it separates interchange semantics from local safety and portability concerns.

## Consequences

- Path conversion is explicit and can fail safely.
- Carrier parsing and validation can be tested without a destination workspace.
- Workspace-specific case, Unicode, link, permission, and replacement behavior remains outside carrier syntax.
- Carrier and workspace specifications require a precise relationship without duplicating ownership.
- Comparison and application must supply explicit workspace context.

## Verification impact

- Dependency and type-boundary checks prevent physical path services from entering carrier decoding and validation.
- Carrier fixtures verify transport validity independently of workspace state.
- Workspace mapping tests cover containment, unsupported mappings, and environment-specific observations.
- Cross-platform support claims require verified workspace-context evidence.

## Supersession conditions

Supersession requires a different representation that proves equal or stronger platform neutrality, containment safety, compatibility, carrier independence, and explicit environmental behavior.

## Affected authorities

- `docs/ARCHITECTURE.md` integrates the carrier/workspace boundary.
- Future carrier specifications own transported representation.
- Future workspace-path and operation specifications own local interpretation and observable safety behavior.
