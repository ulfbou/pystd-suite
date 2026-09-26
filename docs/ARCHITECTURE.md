# DX Architecture

Status: Normative
Owner: System architecture
Scope: DX prototype responsibilities, dependency direction, capability boundaries, environmental boundaries, and architectural invariants

## Purpose and authority

This document defines the architecture that governs the initial DX product within pystd-suite. It establishes responsibility boundaries, allowed dependencies, capability separation, environmental boundaries, and invariants that implementations must preserve.

Product identity and scope belong to `docs/VISION.md`. Observable syntax and behavior belong to later specifications. This document does not define carrier grammar, selection precedence, operation details, CLI syntax, numeric process results, machine-output fields, workflow, release procedure, roadmap sequence, package layout, module layout, or replaceable algorithms.

## System context

DX interacts with:

- human CLI users and automation consumers;
- untrusted requests, supplied paths, selection inputs, and destination requests;
- untrusted DX carriers;
- repository or workspace filesystems;
- operating-system filesystem semantics;
- standard streams and the process boundary;
- optional Git capabilities;
- the Python runtime and packaging environment;
- explicit carrier-output destinations.

The workspace filesystem and carrier-output destination are separate mutation boundaries. Git is optional. Environmental facts that affect semantics must be eliminated, resolved, declared, or reported rather than read implicitly by semantic logic.

## Architectural domains and boundaries

### Carrier domain

The carrier domain owns carrier representation, decoding, encoding, validity, transported logical paths and attributes, payload bytes, and preservation-relevant facts. It does not interpret physical workspace behavior.

Decoding converts carrier bytes to syntax-level content. Validation establishes whether that content satisfies accepted carrier requirements. Encoding produces carrier bytes from valid carrier content. Persisting those bytes is a separate mutation responsibility.

### Workspace and path domain

The workspace and path domain owns workspace-relative logical path meaning, explicit workspace context, filesystem observations, logical-to-physical relationships, containment, and observable path conflicts.

It does not own carrier framing or selection policy. A valid carrier path is not automatically a safe or applicable physical target.

### Selection domain

The selection domain owns deterministic decisions over explicit candidate and rule facts. It returns typed decisions and relevant reasons.

Selection does not traverse the filesystem, invoke Git, read process environment, write carriers, or format human or machine output.

### Operation and planning domain

The operation and planning domain coordinates carrier, workspace, and selection semantics. It owns inspection, verification, comparison, carrier-creation planning, workspace-application planning, and typed operation outcomes.

Inspection, verification, and comparison are capabilities within this domain, not independent top-level domains.

### Mutation boundary

Mutation executes validated planned intent through explicit, resource-specific write capability. Workspace mutation and carrier-output mutation are distinct capabilities. Neither is available to read-only operations.

### Presentation and process boundary

The presentation and process boundary owns CLI adaptation, standard-stream interaction, human presentation, machine presentation, and later translation of typed outcomes into public process behavior.

It does not own product semantics and must not re-evaluate semantic decisions.

### Git integration boundary

Git integration owns invocation of explicitly requested Git capabilities and translation of Git output into adapter facts. It does not own candidate or selection semantics.

## Responsibility model

The architecture separates the following responsibilities:

- carrier decoding, encoding, and validation;
- workspace-path interpretation and filesystem observation;
- candidate discovery and selection semantics;
- content loading and product-relevant classification;
- carrier-creation planning and carrier-output execution;
- inspection, verification, and comparison;
- workspace-application planning and workspace mutation;
- typed diagnostics, explanation, and relevant provenance;
- CLI adaptation and human or machine presentation;
- optional Git-derived observations.

Discovery produces candidate facts. Selection decides among those facts. Content loading reads only selected content needed for packing. Planning combines validated facts into intended effects. Execution applies accepted plans through explicit write capability.

## Dependency direction

The conceptual dependency direction is:

```text
process and presentation
        |
        v
operation orchestration
        |
        v
carrier, workspace/path, and selection semantics
```

Environmental capabilities enter orchestration through explicit boundaries:

```text
filesystem observation ---> operation orchestration
optional Git facts      ---> discovery or operation input
workspace mutation      <--- application-plan execution
carrier-output mutation <--- creation-plan execution
```

Semantic domains must not depend on:

- CLI parsing or `argparse`;
- terminal or JSON formatting;
- environment-variable reads;
- subprocess invocation;
- mutable filesystem services where read-only facts suffice;
- Git implementation details.

Concrete filesystem and Git integrations implement boundaries requested by orchestration. Mutation integrations are visible only to mutation execution.

## Read, plan, and write capabilities

### Read

Read capability performs bounded observation. It may consume carrier bytes, observe requested filesystem facts, load content, and invoke an explicitly enabled read-only external capability. It cannot create or replace carriers, modify workspace entries, create configuration, or write product caches.

Inspection, verification, comparison, discovery, content loading, and preview use read capability only.

### Plan

Plan capability combines validated semantic facts into immutable intended effects. A plan exposes intended writes, skips, conflicts, rejections, findings, and relevant preconditions. Planning performs no product mutation.

### Write

Write capability is explicit and resource-specific. Workspace-write capability and carrier-output capability are separate. Possession of one does not imply possession of the other.

Every product mutation consumes immutable, validated, operation-specific planned intent. Execution may revalidate safety preconditions that can change after planning, but it must not silently recompute different selection or conflict semantics.

## Operation plans

The prototype uses two conceptual internal plan forms:

- a carrier-creation plan;
- a workspace-application plan.

A single generic plan is not an architectural goal.

Preview renders the applicable plan. Execution consumes the accepted plan. The creation plan records selected carrier paths, accepted payload facts and attributes, output conditions, findings, and preconditions. The application plan records the carrier context, destination context, intended writes, skips, conflicts, read-only outcomes, rejections, findings, and preconditions.

Plans are ephemeral internal values. They are not public artifacts, schemas, compatibility formats, or extension points. A future machine-readable interface may expose selected plan facts without exposing the internal representation.

## Carrier and workspace separation

Carrier representation owns transported path text, payload bytes, carrier attributes, and carrier validity. Workspace interpretation owns physical resolution, local observations, containment, links, permissions, conflicts, and replacement conditions.

Conversion occurs only when an operation intentionally relates a valid carrier entry to an explicit workspace context. Carrier validity does not imply safe applicability to every workspace. Workspace unsuitability does not by itself make the carrier malformed.

Carrier syntax must not determine local link policy, overwrite mechanics, permission handling, or replacement behavior.

## Filesystem-semantics boundary

A dedicated read-only boundary observes requested filesystem facts. Relevant semantics are resolved into explicit workspace context, represented as explicit observations, or reported as unsupported or indeterminate.

Path, discovery, selection, comparison, and planning semantics receive these facts explicitly rather than querying ambient filesystem properties. Planning records relevant preconditions. Mutation revalidates those preconditions where the environment may have changed.

Exact case, Unicode, link, permission, replacement, transaction, race, and partial-failure behavior belongs to later specifications and detailed decisions.

## Git boundary

Git provides optional, independently requested capabilities that may include repository-root information, worktree candidate facts, status facts, and ignore-decision facts.

Filesystem-based and explicit selection must function without Git. Git subprocess execution and executable discovery remain outside semantic domains. If retained, Git-derived facts become explicit semantic inputs.

Git absence is represented as irrelevant when not requested, unavailable when optional, or a typed failure when a requested capability requires it. Silent fallback is prohibited. Ambient global Git configuration does not influence selection unless a later compatibility authority explicitly accepts and reports it.

## Environmental-input model

- The process boundary resolves the current working directory into explicit resource locations.
- Environment variables do not influence semantics unless a later process contract admits and resolves them explicitly.
- Accepted ignore-file paths, contents, and ordering are explicit inputs.
- Filesystem semantics and platform facts are declared or resolved workspace context.
- Locale does not alter semantics unless later specified.
- Process encoding is resolved at the boundary; carrier and payload bytes do not depend on terminal defaults.
- Optional executable availability is reported explicitly.
- Time, randomness, and temporary locations do not alter semantic outcomes unless separately required.
- Output destination state is explicit planning input.

## Diagnostics, results, and provenance

Semantic responsibilities produce typed outcomes, findings, and relevant provenance. Human and machine presentations derive from the same facts and do not rerun semantic rules.

Architecturally relevant provenance is limited to facts needed to explain candidate origin, contributing requests or adapters, decisive selection reasons, selection or rejection outcomes, carrier-entry relationships to planned effects, and environmental causes of unsupported or safety outcomes.

The architecture does not require attributed expression trees, public diagnostic-node identities, or a public decision-graph format.

## Error boundaries

The architecture preserves these conceptual distinctions until the presentation and process boundary maps them to public behavior:

- invalid request;
- invalid carrier;
- unsupported behavior;
- environmental failure;
- safety conflict;
- semantic negative result;
- verification difference;
- internal defect.

Low-level causes are translated to typed adapter or semantic outcomes, then operation outcomes, then human, machine, and process presentation. This architecture assigns no numeric process values.

## Reference semantics

Correctness-first reference behavior governs selection, carrier round trips, planning, and comparison. An optimization must not become semantic authority.

Future optimizations require applicable golden, generated, property, regression, and reference-equivalence evidence. Optimized behavior must preserve all accepted semantic outcomes, findings, and relevant preconditions.

## State and mutability

Validated carriers, logical paths, workspace contexts, candidates, selection decisions, payload facts, plans, results, findings, and provenance are immutable semantic values by default.

Localized mutable state is permitted for bounded parsing, traversal internals, stream consumption, temporary assembly, write progress, and operating-system resources. It remains inside the responsibility using it.

Hidden module-global state that affects product behavior is prohibited. No semantic cache is part of the prototype architecture.

## Runtime dependencies

Core semantics are standard-library-first and have no third-party runtime dependency by default.

An approved third-party runtime dependency must satisfy a demonstrated need, include analysis of the standard-library alternative, be isolated behind the narrowest suitable boundary, avoid spreading dependency-specific types through semantic code without explicit acceptance, and have verified compatibility, security, portability, and packaging consequences.

Git is an optional external runtime capability, not a universal prerequisite.

## Architectural invariants

### 1. Semantic logic is independent of CLI parsing

**Rationale:** Invocation syntax must not define product semantics.

**Verification responsibility:** Dependency checks prevent semantic domains from importing CLI parsers or process-specific request types. Component tests exercise semantics without a CLI.

### 2. Semantic logic is independent of presentation

**Rationale:** Human and machine rendering must not become alternate evaluators.

**Verification responsibility:** Dependency checks and agreement tests render the same typed outcomes through both presentation forms.

### 3. Read-only operations cannot acquire write capability

**Rationale:** Inspection, verification, comparison, and preview are product-level read-only behaviors.

**Verification responsibility:** Composition tests give these operations no write boundary. Side-effect tests verify that they do not create or modify product artifacts.

### 4. Mutation consumes explicit validated planned intent

**Rationale:** Preview and execution must describe the same intended effects.

**Verification responsibility:** Mutation executors accept plans rather than raw requests and cannot rediscover or reselect content.

### 5. Workspace writes and carrier-output writes are separate capabilities

**Rationale:** They mutate different resources with different safety rules.

**Verification responsibility:** Separate boundaries and dependency checks prevent either executor from acquiring the other capability.

### 6. Carrier paths and physical workspace paths remain distinct

**Rationale:** A valid transported path is not automatically a safe local target.

**Verification responsibility:** Conversion requires explicit workspace context, and tests cover unsafe or unsupported mappings.

### 7. Selection consumes explicit facts

**Rationale:** Determinism requires declared inputs.

**Verification responsibility:** Selection has no filesystem, subprocess, environment, or Git dependency and is tested from supplied candidate and rule facts.

### 8. Environmental semantics are resolved at boundaries

**Rationale:** Platform, filesystem, executable, and process state can affect outcomes.

**Verification responsibility:** Operation inputs contain resolved context or explicit unavailable results; tests vary boundary facts independently of semantics.

### 9. Execution and explanation use the same semantic decisions

**Rationale:** Explanations are trustworthy only when they describe the executed decision.

**Verification responsibility:** Findings and provenance accompany typed results, and presentation cannot rerun rules.

### 10. Git remains optional and external to semantic selection

**Rationale:** Git is not a universal product prerequisite.

**Verification responsibility:** Core selection tests run without Git. Adapter and absence tests cover explicitly requested Git capabilities.

### 11. Optimization cannot redefine semantics

**Rationale:** Performance changes must preserve correctness.

**Verification responsibility:** Optimized implementations are compared with accepted reference behavior over representative and generated cases.

### 12. Internal plans are not public compatibility artifacts

**Rationale:** Safe orchestration must not create an accidental external format.

**Verification responsibility:** No public serializer or schema exposes an internal plan without a separate accepted decision.

### 13. Unsupported capability is explicit

**Rationale:** Portability and optional integration claims must remain honest.

**Verification responsibility:** Tests cover absent Git, unsupported entry types, and unsupported environment behavior without silent fallback.

### 14. Architecture is independent of the historical `dx.py` organization

**Rationale:** Existing code is evidence, not the target architecture.

**Verification responsibility:** Architecture and implementation reviews trace responsibilities to this document and accepted ADRs rather than historical functions or data structures.

## Decision records

The following foundational decisions are recorded separately:

- ADR 0001: Semantic core and explicit boundary dependency model
- ADR 0002: Plan-mediated explicit mutation
- ADR 0003: Carrier and workspace path separation
- ADR 0004: Git as optional explicit external capabilities

Accepted ADR consequences are integrated here so that continuing architecture does not require reconstructing the full decision history.
