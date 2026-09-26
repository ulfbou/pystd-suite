# ADR 0002: Plan-mediated explicit mutation

Status: Accepted
Owner: Architectural decision record
Scope: Relationship between preview, carrier creation, workspace application, and explicit mutation capability

## Context

The product requires inspection and preview before mutation. Carrier creation and workspace application affect different resources and have different safety concerns. A preview that simulates an operation separately from execution can disagree with what execution later attempts. Direct execution from raw requests can also repeat selection or conflict decisions after the user reviewed them.

The architecture therefore needs a stable relationship between intended effects, preview, and mutation while acknowledging that filesystem preconditions can change.

## Decision

Carrier creation and workspace application consume immutable, validated, operation-specific plans.

A carrier-creation plan and a workspace-application plan are distinct conceptual forms. Preview renders the applicable plan. Execution consumes the accepted plan through an explicit resource-specific write capability.

Execution may revalidate safety preconditions that can change after planning. It must not silently recompute different selection, destination, read-only, or conflict semantics.

Plans are ephemeral internal values. They are not public artifacts, schemas, compatibility formats, or extension points.

## Alternatives considered

### Direct execution from raw requests

Rejected because mutation would combine interpretation and side effects and could not guarantee agreement with preview.

### Independently simulated preview

Rejected because preview and execution could implement different decisions or drift over time.

### One generic plan

Rejected because carrier creation and workspace application have different resources, preconditions, effects, and safety boundaries.

### Operation-specific immutable plans

Accepted because preview and execution share intended effects while retaining separate mutation capabilities.

## Consequences

- Preview and execution derive from the same semantic facts.
- Mutation executors remain narrow and do not perform discovery or selection.
- Planning must record relevant findings and preconditions.
- Execution must report changed preconditions rather than silently adapting the plan.
- Partial-failure and race behavior still require later specification.
- Public machine output may expose selected plan facts without exposing internal representation.

## Verification impact

- Executor boundaries accept validated plans rather than raw carrier or selection requests.
- Tests verify that mutation does not rediscover candidates, reselect content, or change conflict policy.
- Preview and execution agreement tests compare planned intent with attempted effects.
- Side-effect tests confirm that planning performs no product mutation.
- Race and changed-precondition tests are required when detailed semantics are accepted.

## Supersession conditions

Supersession requires an alternative that proves equal or stronger preview/execution agreement, read/write capability isolation, conflict visibility, and changed-precondition handling with lower complexity.

## Affected authorities

- `docs/ARCHITECTURE.md` integrates the read, plan, and write model.
- Future operation specifications define observable preview, conflict, partial-failure, and execution behavior.
- Future workflow and conformance authorities must verify preview and execution agreement.
