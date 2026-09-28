# DX Implementation Architecture

Status: Development planning
Owner: Internal implementation boundaries and composition for the redesigned DX product
Scope: Realization of the normative architecture and Accepted ADRs without defining observable behavior or public representation

## Relationship to authority

This document realizes `docs/ARCHITECTURE.md` and Accepted ADRs 0001 through 0004. It does not replace them. Observable behavior remains owned by the Accepted specifications. Historical `dx.py` and `dxlib` are characterization evidence, not target structure. Internal values, plans, protocols, and assembly choices are replaceable and are not public artifacts, schemas, or compatibility formats.

## Dependency model

The required dependency direction is:

```text
process and presentation
        -> operation orchestration
        -> carrier, workspace/path, selection, and result semantics

filesystem observation -> orchestration
content loading        -> orchestration
optional Git facts     -> discovery or orchestration input
carrier-output write   <- creation-plan execution only
workspace write        <- application-plan execution only
```

Environmental capabilities enter through explicit boundaries. Semantic code receives values and observations, never ambient filesystem, environment, subprocess, terminal, or Git access.

## Internal boundaries

### Carrier semantics

Own immutable carrier content, logical carrier paths, accepted attributes, decoded payload bytes, syntax-level decoding, structural validation, and deterministic encoding. Decoding and validation remain separable so malformed syntax, unsupported version, and valid content are distinguishable. Encoding produces complete carrier bytes but cannot persist them.

Physical workspace paths, output sinks, process streams, and compatibility aliases do not enter this boundary.

### Workspace and path semantics

Own explicit workspace context, logical-to-physical mapping decisions, containment, path identity, collision detection, and interpretation of supplied no-follow observations. This boundary receives typed observations and resolved environment facts. It does not call filesystem APIs or reinterpret carrier validity.

### Selection semantics

Own pure deterministic selection over supplied candidate, scope, selector, exclusion, ignore, override, availability, unsupported-source, and optional Git-derived facts. It returns immutable per-candidate decisions with decisive outcome and provenance. It performs no discovery, content loading, filesystem access, Git invocation, environment access, process adaptation, or presentation.

### Result and planning values

Own immutable operation results, findings, effects, preconditions, uncertainty, and provenance shared across orchestration, diagnostics, and execution. Carrier-creation plans and workspace-application plans remain distinct operation-specific values. Plans contain only validated intent and facts needed for preview, execution, revalidation, and explanation. They are not serializable public contracts.

### Operation orchestration

Coordinate semantic boundaries and requested adapters for inspection, structural verification, comparison, creation planning, and application planning. Orchestration determines which facts are required, invokes only admitted read capabilities, translates adapter outcomes into semantic inputs, and assembles typed results and plans.

Read-only orchestration receives no write capability. Planning receives observation and loading capabilities but no mutation capability. Execution is invoked separately with an accepted plan and the matching narrow write capability.

### Discovery and content-loading adapters

Discovery enumerates requested candidate sources without following links and emits candidate facts and provenance. Content loading reads exact bytes only for selected paths, using retained observations and no-follow safety. Neither adapter decides selection membership or carrier representation.

### Filesystem observation adapter

Perform bounded no-follow observation and return explicit entry type, identity, containment-relevant, permission, case, Unicode, and capability facts required by workspace semantics. It does not mutate. Unsupported or unavailable observations remain typed and explicit.

### Optional Git capabilities

Expose separately requested repository-root, candidate, status, or ignore facts. Executable discovery, subprocess invocation, controlled configuration, byte decoding, absence, and failure remain inside the adapter. No all-purpose Git service is introduced. Selection sees only explicit facts and functions without Git.

### Carrier-output execution

Accept only a validated carrier-creation plan and a carrier-output capability. Revalidate sink preconditions, encode or consume frozen complete carrier bytes as admitted by the plan, deliver the complete bytes, and retain completed, failed, or uncertain delivery evidence. It cannot write workspace entries, rediscover candidates, reselect paths, or reload payloads.

### Workspace mutation execution

Accept only a validated workspace-application plan and workspace-write capability. Perform complete preflight, deterministic ordered effects, per-effect revalidation, and retained partial-failure evidence. It cannot write carrier outputs, parse CLI requests, rediscover content, reselect paths, or silently replan.

### Diagnostic interpretation

Transform authoritative results and retained findings into presentation-neutral diagnostic meaning. It cannot rerun carrier, selection, mapping, comparison, planning, or mutation decisions. Stable symbolic identifiers and typed resources originate from Accepted diagnostic semantics, not implementation exception classes.

### Human and machine presentation

Render the same semantic result and diagnostic interpretation. Human and machine adapters may differ in representation but cannot strengthen, weaken, or recalculate meaning. No machine encoding or concrete object shape is selected here.

### CLI and process adaptation

Own request parsing, initial-directory resolution, stream acquisition and routing, terminal checks, help and version behavior, machine-mode eligibility, delivery failures, and numeric process mapping. It constructs validated operation requests and maps completed semantic results. It does not own semantic rules.

## Composition boundaries

Use explicit composition roots at executable entry and at tests. The executable composition root resolves process resources, creates concrete adapters, and supplies only the capabilities required by the selected operation. Test composition roots substitute deterministic boundaries and assert capability absence.

Dependency-injection machinery, service containers, registries, plugin systems, and provider frameworks are not goals. Ordinary constructors, callables, immutable values, and narrow structural protocols are sufficient where they directly protect a boundary.

## Values, protocols, and mutability

Immutable semantic values are the default for validated logical paths, carrier entries, carriers, workspace contexts, observations, candidates, decisions, loaded payloads, findings, effects, preconditions, plans, and results. Narrow protocols are justified for carrier-byte acquisition, candidate discovery, content loading, filesystem observation, individual optional Git capabilities, carrier-output delivery, workspace mutation, and process streams.

Localized mutability is permitted only inside bounded parsing, traversal, stream consumption, temporary assembly, operating-system resource management, and executor progress tracking. Mutable state must not escape as semantic authority. Product-affecting module globals, ambient caches, implicit current-directory reads, implicit environment reads, and shared write services are prohibited.

## Prohibited dependency directions

- Semantic domains must not import CLI, presentation, process, filesystem, subprocess, Git, environment, or mutation integrations.
- Carrier semantics must not depend on workspace mapping or physical paths.
- Selection must not depend on discovery, content loading, output sinks, or environmental adapters.
- Diagnostic and presentation code must not invoke semantic evaluators.
- Read and planning components must not depend on either write capability.
- Carrier-output execution and workspace execution must not depend on each other.
- Executors must not accept raw process requests or broad service objects.
- Optional Git adapters must not become prerequisites for carrier, workspace, or selection semantics.
- Internal plans must not enter public machine serialization or schema governance.

## Architecture-test seams

Architecture verification must establish:

- import and dependency direction for semantic, orchestration, adapter, execution, presentation, and process boundaries;
- component construction of carrier, workspace/path, selection, and operation semantics without CLI, presentation, real filesystem, or Git;
- absence of write capability from inspection, verification, comparison, discovery, loading, and both planning operations;
- separate carrier-output and workspace-write protocols and compositions;
- executor acceptance of validated plans rather than raw requests;
- selection execution from explicit values with no I/O-capable dependency;
- diagnostic and presentation consumption of retained results without semantic callbacks;
- explicit Git absence, availability, and failure composition;
- no public serializer for internal plans.

Source inspection tests may protect forbidden imports and composition wiring. Behavioral side-effect tests must additionally prove that read and planning operations create or modify no product artifacts.

## Historical implementation migration

Historical `dx.py` and `dxlib` combine codec, discovery, selection, Git, filesystem access, mutation, diagnostics, presentation, CLI parsing, ambient state, and duplicated code. Characterization may capture evidenced behavior under the compatibility classifications before replacement. Reusable algorithms may be adapted only after their behavior conforms to Accepted authority and their dependencies fit these boundaries.

Migration proceeds by vertical outcomes. New semantic components and adapters are introduced alongside historical evidence, verified independently, and connected through new orchestration. Historical functions, classes, aliases, numeric values, machine shapes, defaults, globals, and file organization do not determine new boundaries. Compatibility tests remain separate from conformance tests.

## Initial implementation-shape decision

No package or module layout is fixed by this plan. The first implementation slice requires a minimal importable semantic boundary, a minimal test location, and a composition seam, but naming those files is an implementation-local choice in that carrier. A package-layout ADR is not currently required because the accepted dependency boundaries can be realized and tested without committing a costly public structure.

## Runtime discipline

The implementation remains standard-library-first. A third-party runtime dependency requires the review established by product, architecture, security, contribution, and release authorities. Test tooling may be selected for a defined verification responsibility without entering runtime semantics.
