# DX Operation Semantics
Status: Normative
Owner: DX carrier creation, inspection, structural verification, comparison, and workspace application semantics
Scope: Content loading after selection, carrier-creation planning and execution, carrier serialization and output delivery, inspection, structural verification as an operation, comparison, workspace-application planning and execution, conflict behavior, read-only treatment, changed preconditions, no-op behavior, and partial failure
Maturity: Draft

## Purpose
This specification defines the observable semantics of DX carrier creation, inspection, structural verification, workspace comparison, workspace-application planning, and explicit application. It begins after packing selection has produced retained decisions and selected logical paths.

The operation model separates reading, planning, and writing. Inspection, structural verification, and comparison are read operations. Carrier-creation preview and workspace-application preview are planning operations. Carrier creation and workspace application are explicit write operations. Read and planning operations are non-mutating. Mutation consumes validated operation-specific planned intent.

## Scope
### In scope
This specification governs:
- content loading after selection;
- source-content eligibility;
- empty selected-set treatment at creation level;
- carrier-creation planning, serialization, delivery, and execution;
- general carrier-output sinks and filesystem-sink-specific safety;
- carrier inspection and structural verification;
- comparison with an explicit workspace;
- workspace-application planning and execution;
- existing-target and read-only behavior;
- unchanged targets and no-op outcomes;
- changed preconditions and parent creation;
- mutation atomicity and partial failure;
- semantic results, findings, provenance, and determinism.

### Out of scope
This specification does not govern carrier grammar, packing selection, physical path grammar, CLI command or option spelling, standard-stream mapping, terminal behavior, broken-pipe process behavior, numeric process outcomes, machine-output fields, diagnostic presentation, schemas, internal plan serialization, package structure, or replaceable write algorithms.

## Terminology
**Read operation** means a non-mutating operation that obtains or relates facts.

**Planning operation** means a non-mutating operation that combines validated semantic facts and resolved observations into immutable intended effects, findings, and preconditions.

**Write operation** means explicit execution of validated planned intent through the applicable mutation capability.

**Carrier-output sink** means the explicit destination to which complete carrier bytes are delivered. A filesystem path is one sink specialization, not an inherent carrier-creation requirement.

**Content-loading observation** means the post-selection observation that establishes whether a selected logical path denotes a readable regular file and, when it does, obtains its exact bytes.

**Satisfied target** means a safe regular workspace target whose bytes already equal the decoded carrier bytes and therefore requires no write.

**Volatile precondition** means an observed environmental fact that may change between planning and execution and whose change can invalidate intended effects.

## Conceptual operation set
DX defines these semantic operations.

### Read
1. Inspect carrier.
2. Structurally verify carrier.
3. Compare carrier with an explicit workspace.

### Plan
4. Plan carrier creation.
5. Plan workspace application.

### Write
6. Create carrier.
7. Apply carrier.

Summary, entry listing, read-only listing, calculated decoded-entry hashes, and exact-entry decoded content are inspection projections, not independent semantic operations.

Structural verification is a distinct read operation over carrier parsing and validation facts. Comparison is read-only and does not create mutation intent.

Workspace extraction and workspace application are one conceptual operation. Raw extraction that bypasses workspace safety and planning is not admitted. Public naming and compatibility aliases belong to later CLI/process and compatibility authorities.

## Read, plan, and write invariants
Read operations and planning MUST NOT perform product mutation.

Mutation MUST consume validated operation-specific planned intent. Workspace-write capability and carrier-output capability remain separate.

Execution MAY revalidate volatile environmental and safety preconditions. It MUST NOT silently rediscover candidates, reselect paths, change retained selection decisions, change content eligibility, substitute changed source content, choose a different conflict policy, or broaden requested scope.

Execution and explanation MUST use the same retained semantic facts.

## Common operation inputs
Semantic inputs include, where applicable:
- supplied carrier bytes or a carrier validated within the same trusted operation context;
- supported carrier versions and the applicable carrier contract;
- an Accepted selection result and its retained decisions;
- selected logical paths and exact loaded payload bytes;
- accepted carrier attributes and deterministic serializer inputs;
- an explicit carrier-output sink;
- an explicit workspace root and resolved workspace context;
- explicit replacement, skip, comparison-scope, or parent-creation authority;
- read-only declarations;
- a requested exact carrier entry for content inspection.

Environmental observations include source availability, type, readability, and bytes; sink availability; filesystem-output existence, type, identity, parent state, and access; workspace target and ancestor states; target bytes; workspace-only paths within an explicit comparison scope; permissions; and resolved filesystem identity behavior.

Volatile preconditions include source identity where later access remains relevant, sink availability, filesystem destination and parent state, workspace target and ancestor identity and type, containment, observed content, planned missing-parent state, and required permissions.

Presentation inputs include rendering mode, wording, localization, formatting, grouping, and display destinations. They MUST NOT affect semantics.

Invocation names, option spelling, stream ownership, machine-output fields, numeric process values, internal plan types, package structure, and subprocess mechanics are outside operation semantics.

## Content loading after selection
Selection is the sole authority for path membership. Content loading processes only paths whose Accepted selection outcome is selected and MUST NOT re-evaluate candidate, scope, selector, exclusion, ignore, or override rules.

For each selected logical path:
- a readable regular file yields its exact bytes;
- an empty regular file yields zero bytes;
- arbitrary readable byte sequences remain exact payload content;
- unreadable content produces an environmental content-loading failure;
- a missing or disappeared source produces an unavailable-source or changed-source result according to the established observation context;
- a regular source that becomes a symbolic link, directory, or unsupported object produces a changed-precondition or unsupported-source result;
- symbolic links MUST NOT be followed.

These outcomes do not change the selected path into an exclusion. The retained selection decision remains available with the post-selection content result.

A carrier-creation plan is executable only when every selected path has an accepted payload fact. Core operation semantics do not implicitly omit selected content.

## Content eligibility
Every readable regular-file byte sequence supported by the governing carrier representation is eligible.

Source eligibility is distinct from carrier representation. Content classification may determine representation, but binary classification does not make content invalid and MUST NOT by itself determine whether deliberately selected content is transported.

Core operation semantics define no binary skip or binary fail policy.

## Empty selected set
An empty selected set is valid selection output but produces a creation-level semantic negative result:
- no executable carrier creation is planned;
- no carrier is emitted;
- no sink delivery is attempted;
- no existing filesystem destination is replaced;
- retained empty-selection reasons remain available.

DX does not create an empty carrier implicitly. This specification assigns no process outcome.

## Fundamental carrier-creation output model
Carrier creation semantically produces complete carrier bytes and delivers those bytes to an explicit carrier-output sink.

The semantic pipeline is:

```text
selection
→ content loading
→ carrier-creation planning
→ carrier serialization
→ complete carrier bytes
→ selected output sink
```

A filesystem path is one output-sink specialization. For a filesystem sink, complete bytes are delivered subject to filesystem-specific safety and replacement semantics. Carrier creation MUST NOT otherwise assume a filesystem destination.

## Carrier-creation planning
Carrier-creation planning is non-mutating. It preserves or establishes:
- Accepted selection result context;
- selected logical paths and retained selection decisions;
- exact loaded payload bytes or equivalent immutable payload facts;
- accepted carrier attributes;
- content-loading results;
- deterministic serializer inputs;
- selected output sink;
- sink-specific observations and preconditions;
- findings and volatile preconditions.

The internal plan is ephemeral and is not a public artifact, schema, compatibility format, or extension point.

Preview MUST disclose, as applicable:
- intended transported paths;
- payload readiness and blocking source failures;
- relevant carrier attributes;
- output-sink type;
- applicable sink-specific conflicts;
- replacement authority for a filesystem sink;
- filesystem self-reference conflict;
- parent creation for a filesystem sink;
- relevant volatile preconditions;
- complete-plan executability.

Preview and execution derive from the same planned intent.

## Non-filesystem output sinks
A non-filesystem sink:
- has no filesystem output path;
- does not participate in packing selection;
- creates no filesystem output self-reference;
- has no filesystem replacement policy;
- has no filesystem parent-directory semantics;
- has no filesystem symlink semantics.

Its delivery failures remain operation outcomes. Successful carrier creation means that the complete planned carrier bytes were delivered according to the selected sink's contract. Incomplete delivery MUST NOT be reported as successful creation.

Exact stream and process behavior belongs to the CLI/process specification.

## Filesystem output sinks
When the selected carrier-output sink is a filesystem path:
- an absent output is eligible for creation when parent, containment, permission, and safety requirements hold;
- an existing regular file is a conflict unless explicit replacement authority exists;
- an existing directory is a conflict;
- an existing symbolic link, including a broken symbolic link, is a non-overridable safety conflict;
- an existing FIFO, socket, device, or unknown object is an unsupported conflict;
- a missing parent MAY be included in planned intent when safe parent creation is explicitly authorized;
- an inaccessible or unsafe parent produces a conflict or environmental failure.

Replacement authority applies only to a safely observed regular output. It does not override symlink, containment, directory, unsupported-object, or parent-safety rules.

Execution MUST revalidate applicable filesystem-sink preconditions before mutation.

## Output self-reference
The output sink MUST NOT alter selected-set membership. Planning MUST NOT insert a hidden output exclusion.

Self-reference rules apply only when the selected sink is a filesystem path. Planning reports a non-overridable output self-reference conflict when the filesystem output conflicts with selected source content, including when it identifies the same physical source object.

A non-filesystem sink creates no output-path self-reference. A filesystem output merely located within a selected subtree is not a conflict when it did not participate in selected source facts and does not alias selected source content.

Loaded source payload bytes are frozen before filesystem carrier-output mutation.

## Carrier serialization and creation execution
Carrier serialization determines complete carrier bytes from frozen payload facts, logical paths, accepted attributes, and the governing serializer contract. Complete equivalent semantic inputs MUST produce equivalent carrier bytes according to that contract.

Create-carrier execution consumes the accepted creation plan. It MAY revalidate sink availability and, for a filesystem sink, destination existence, type, replacement identity, symlink status, parent safety, required permissions, and other volatile sink facts.

Execution MUST NOT recompute discovery, selection, selected paths, payload eligibility, payload bytes, carrier attributes, or semantic conflict policy.

Source payload bytes SHOULD be frozen into the plan or an equivalent immutable semantic value. Execution MUST NOT silently reread and substitute changed source content.

Successful creation means complete intended carrier bytes were delivered to the selected sink. Failure means successful carrier creation was not achieved. If final sink state cannot be established, the result records uncertain state.

For a filesystem replacement, the operation MUST NOT intentionally destroy the observed prior regular output before complete replacement bytes are ready. This does not claim portable crash-proof replacement, transactional filesystem behavior, or cross-filesystem atomicity.

## Downstream CLI/process handoff
The following is an informative preferred mapping for evaluation by `docs/spec/cli-process.md`:

```text
pack request without an explicit file destination
→ complete carrier bytes to standard output

pack request with an explicit file destination
→ complete carrier bytes to a filesystem sink
```

This is not normative operation behavior. The CLI/process authority independently owns public command and option spelling, whether omission of a file destination selects standard output, stream ownership, terminal safety, broken-pipe behavior, and shell interaction.

## Inspection
Inspection obtains carrier and decoded-entry facts without mutation. Depending on the requested projection, it MAY expose:
- declared carrier version;
- structural parse status;
- entry count;
- NOTE-block count where applicable;
- logical paths and accepted attributes;
- decoded sizes and representation type;
- read-only declarations;
- calculated SHA-256 over decoded entry bytes;
- exact decoded bytes for one requested entry.

A request for exact entry content succeeds only when exactly one valid entry has the requested logical path. No match produces a semantic negative result. Multiple occurrences produce an invalid-carrier result where path uniqueness is required.

Binary entry retrieval returns exact decoded bytes. Presentation and stream routing are outside inspection semantics.

Malformed carrier bytes produce an invalid-carrier result. An unsupported version produces an unsupported-version result. Failure to obtain carrier bytes produces an environmental failure.

Inspection establishes no workspace relationship, authenticity, trusted integrity, historical compatibility, or application safety.

## Structural verification
Structural verification is a read operation that establishes only conformity with the supported structural carrier contract.

Successful structural verification may establish that parsing succeeds, required framing is valid, attributes are valid, payload representations decode, logical paths satisfy carrier requirements, and uniqueness and other structural invariants hold.

It MUST NOT claim authenticity, origin, authorization, trusted integrity without a trusted expected value, absence of harmful content, workspace equality, workspace applicability, safe application, or historical compatibility.

Calculated decoded-entry hashes are inspection facts. A calculated hash alone is not integrity verification. Workspace agreement is comparison.

## Comparison
Comparison is non-mutating and relates validated carrier content to an explicit workspace context. It does not create application intent.

For each carrier entry it determines the applicable relation:
- a safely mapped regular target has identical bytes;
- the target is missing;
- a safely mapped regular target has differing bytes;
- a directory exists where a file is represented;
- a final or ancestor symbolic link conflicts with observation;
- an unsupported object occupies the target;
- required observation failed;
- containment, collision, or path-identity rules prevent comparison.

Comparison MUST NOT follow final or ancestor symbolic links.

Read-only entries retain their actual byte and existence relation, with read-only status preserved.

Workspace-only extra detection is an optional explicit comparison scope. An extra path is a comparison fact and creates no deletion intent.

No differences, conflicts, unsupported conditions, or observation failures produces a successful comparison match. Missing, differing, or requested workspace-only content produces a verification difference. Unsafe mapping remains a conflict. Unsupported objects or environments remain unsupported results. Required observation failure remains an environmental failure.

Historical presentation labels are not semantic result names.

## Workspace-application planning
Workspace-application planning is non-mutating and relates a validated carrier to explicit workspace context and observations.

For each entry it conceptually distinguishes:
- create;
- replace;
- satisfied;
- explicitly skipped;
- read-only satisfied;
- read-only discrepancy;
- conflict;
- unsupported;
- observation failure.

These terms define semantic distinctions but need not become public machine enum values.

The plan exposes conceptually:
- logical path;
- workspace relationship or mapping failure;
- current observation;
- intended effect or non-effect;
- conflict or discrepancy reason;
- explicit replacement or skip authority;
- read-only status;
- required parent creation;
- relevant preconditions;
- complete-plan executability.

A blocking conflict, unsupported condition, required observation failure, or read-only discrepancy prevents a fully successful executable application plan.

## Existing workspace target policy
For a writable entry:
- an absent safe target is planned for creation;
- an identical safe regular target is satisfied and is not written;
- a differing regular target without explicit policy is a conflict;
- an explicit fail policy preserves the conflict;
- an explicit skip policy produces a visible skipped-unsatisfied outcome;
- an explicit overwrite policy authorizes planned replacement;
- a directory, symbolic link, or unsupported object is a non-overridable conflict or unsupported result.

Overwrite requires explicit authority. There is no default skip. An explicit skip is not complete application success.

## Read-only entries
A read-only carrier entry is reference material. Application MUST NOT create or replace its target.

For a read-only entry:
- an equal safe regular target is read-only satisfied;
- a missing target is a read-only discrepancy;
- a differing regular target is a read-only discrepancy;
- a directory, symbolic link, unsupported object, containment problem, collision, or permission failure produces the applicable safety, unsupported, or environmental result.

Read-only paths undergo the same workspace safety checks as writable paths. Comparison reports their actual relation.

## Unchanged targets
An existing safe regular file whose bytes equal represented carrier bytes is satisfied. No write is planned, no replacement authority is required, and execution does not touch the target.

Satisfaction is distinct from explicit skip because represented intent is already fulfilled.

## Changed preconditions
Immediately before the first mutation, execution MUST revalidate the complete set of safety- and conflict-relevant preconditions. Immediately before each effect, it MUST revalidate facts that remain volatile.

Invalidating changes include:
- a planned-absent target appeared;
- a target disappeared where prior identity mattered;
- a regular target became a symbolic link, directory, or unsupported object;
- a parent changed type or became a symbolic link;
- containment or path identity changed;
- required permissions changed;
- content changed where planned intent depended on observed bytes;
- a filesystem output destination changed.

A planned-missing parent that appears as the expected safe directory MAY be treated as satisfied after revalidation. This is not semantic replanning.

A complete-preflight failure causes no mutation. A later changed precondition stops further mutation and produces partial failure when earlier effects completed. Execution MUST NOT silently adapt.

## Application execution, atomicity, and partial failure
Workspace application consumes executable planned intent through explicit workspace-write capability.

The atomicity boundary is:

```text
whole-plan preflight
→ deterministic ordered per-entry commit
→ possible partial failure
```

The operation does not promise a whole-workspace transaction, all-or-nothing application, general rollback, crash recovery, or cross-filesystem atomicity.

Mutation stops after an unexpected write failure or invalidated precondition. Execution MUST NOT rediscover, reselect, reinterpret read-only status, choose another target policy, or silently extend planned effects.

Results distinguish planning failure, failed preflight before mutation, changed precondition before the first write, failure during the first mutation, failure after completed effects, and interruption.

Planning failure, complete-preflight failure, and changed precondition before the first mutation cause no workspace writes.

Partial-failure evidence retains deterministic intended effects, completed effects, untouched effects, the failed effect, failure category, known or uncertain target state, parent directories already created, and relevant changed preconditions. Completed effects remain completed. No rollback is promised and later effects are not attempted.

An interruption may leave a completed prefix and an uncertain final attempted effect. Automatic recovery is not claimed.

## Parent directories
Missing parent creation is planned intent and MUST be visible in preview.

It is permitted only when applicable containment, type, no-follow, collision, and authority requirements hold. Preexisting safe directories remain distinguishable from directories intended or completed by the operation.

A planned-missing parent that appears as a safe directory MAY be treated as satisfied after revalidation. An incompatible appearance is a changed-precondition conflict.

No general removal or rollback of created parents is promised after later failure. Completed parent creation remains part of partial-failure evidence.

## No-op semantics
Comparison with no differences is a successful match.

Application where all relevant writable entries are satisfied and all read-only entries are read-only satisfied is success with no change. The same applies when all entries are read-only and satisfied.

Explicitly skipped differing entries are not complete success.

Empty selection for carrier creation is a semantic negative result, not successful creation.

When the output sink is a filesystem path, an existing byte-identical carrier MAY be treated as satisfied only when equality is safely established and explicit replacement authority would otherwise permit the operation. Without replacement authority, existing-output conflict remains.

## Operation results
Shared semantic categories include:
- success;
- success with no change;
- semantic negative result;
- invalid input;
- invalid carrier;
- unsupported version or capability;
- safety or state conflict;
- environmental failure;
- verification difference;
- changed precondition;
- partial failure;
- internal failure.

Operation-specific meaning is preserved rather than forced into one universal result shape. This specification assigns no numeric process values.

A successful result MUST NOT conceal an unresolved conflict, unsupported condition, required observation failure, read-only discrepancy, explicitly skipped unsatisfied target, changed precondition, incomplete carrier delivery, or partial mutation.

## Findings and provenance
Operations retain facts needed to explain the actual semantic result. Presentation MUST derive from these facts and MUST NOT rerun semantic rules.

Carrier creation may retain the selected candidate decision, logical path, payload readiness and byte count, content-loading failure, sink type, filesystem output observation where applicable, replacement authority, self-reference, and changed input.

Comparison may retain the logical path, workspace mapping, entry type, byte relation, read-only status, extra-path scope and provenance, and observation failure.

Application may retain intended effect, target observation, policy authority, parent creation, saved preconditions, completed effects, failed effect, untouched effects, and uncertain target state.

Final diagnostic codes and presentation wording belong to later authority.

## Determinism and environmental inputs
For identical complete semantic inputs and resolved observations:
- read operations produce semantically equivalent results;
- planning produces semantically equivalent plans;
- complete carrier semantic inputs produce equivalent carrier bytes according to the governing serializer contract;
- effect ordering is deterministic;
- presentation mode does not affect semantics.

Complete inputs include, as applicable, exact carrier bytes and supported versions, requested inspection projection, Accepted selection result, exact payload bytes, carrier attributes and serializer contract, selected sink and resolved sink observations, explicit workspace context and filesystem observations, comparison scope, policy authority, parent-creation authority, and read-only declarations.

Mutation differences may arise only from explicitly reported changed environmental facts or external failures. Filesystem enumeration order, locale, timestamps, randomness, undeclared environment variables, and current directory after request resolution MUST NOT define semantics.

## Validation
An operation request is invalid when required semantic input is absent, contradictory, malformed, or outside admitted authority.

Planning MUST complete all applicable validation, content loading, mapping, conflict evaluation, and prerequisite observation possible before mutation. It MUST NOT describe non-executable intent as executable.

Execution accepts only validated operation-specific planned intent and the matching write capability. It rejects or reports changed preconditions instead of silently recomputing different intent.

Low-level parser, filesystem, sink, and write failures are translated into semantic results without exposing implementation-specific exception types as the product contract.

## Compatibility observations
No final historical operation compatibility classification is established by this Draft specification. Existing behavior is informative evidence only.

This semantic model deliberately replaces observed behavior based on default existing-file skip, omission or failure merely from binary classification, rewriting already satisfied targets, unconditional silent read-only skip, unsafe symlink following, hidden output exclusion, structural verification described as integrity, preview and execution recomputing intent independently, or partial writes without complete retained evidence.

Invocation naming, aliases, process migration, and accepted historical classifications belong to later authorities.

## Applicable schemas
None. This specification has no schema-governed boundary.

## Draft dependencies
### Carrier-format dependency
DEPENDENCY: `docs/spec/dx-carrier.md`

CURRENT STATUS: Draft

REQUIRED RULES: Parsing, payload preservation, logical carrier paths, read-only declarations, carrier serialization, and structural verification.

BLOCKS OPERATIONS ACCEPTANCE: YES

This specification does not promote that Draft or resolve its unrelated open questions.

### Workspace-path dependency
DEPENDENCY: `docs/spec/workspace-paths.md`

CURRENT STATUS: Draft

REQUIRED RULES: Workspace mapping, containment, no-follow observation, entry types, collisions, parent safety, applicable filesystem semantics, and changed-precondition categories.

BLOCKS OPERATIONS ACCEPTANCE: YES

This specification does not promote that Draft or resolve its unrelated open questions.

## Required verification
Conformance evidence MUST cover at least:

### Carrier creation
- readable text, empty, and arbitrary-byte selected files;
- unreadable, vanished, changed, symbolic-link, directory, and unsupported selected sources;
- empty selected set;
- payload freezing;
- complete deterministic serialization;
- non-filesystem sink success, incomplete delivery, failure, and uncertain state;
- filesystem output absent, existing regular file, directory, symbolic link, and unsupported object;
- replacement with and without authority;
- filesystem output self-reference and output merely inside a selected subtree;
- missing, inaccessible, and changed parents;
- output changed after planning;
- byte-identical existing output where satisfaction is claimed.

### Inspection and structural verification
- valid, malformed, unsupported-version, empty, multi-entry, read-only, and binary carriers;
- entry listing, decoded size, calculated hash, and exact decoded content;
- missing requested entry and duplicate-path invalidity;
- malformed framing, invalid attributes, bad payload, invalid logical path, and failed carrier-byte access;
- explicit demonstration that structural success does not imply authenticity, trusted integrity, workspace agreement, or safe application.

### Comparison
- identical, missing, differing, and optional workspace-only paths;
- equal, missing, and differing read-only entries;
- directory, final symlink, ancestor symlink, unsupported object, observation failure, containment conflict, and path-identity conflict;
- comparison match and verification difference;
- no symlink following.

### Workspace application
- new, identical, and differing writable targets;
- absent policy and explicit fail, skip, and overwrite policies;
- equal, missing, and differing read-only entries;
- directory, symlink, unsupported object, containment, collision, and permission outcomes;
- parent creation, already satisfied parent, and safely or incompatibly appeared parent;
- complete preflight failure with no mutation;
- changed target or parent before mutation;
- deterministic effect order;
- failure during first mutation and after prior completed effects;
- retained completed, failed, untouched, and uncertain effects;
- all entries satisfied as success with no change;
- explicit skipped-unsatisfied target as incomplete result.

Verification MUST also demonstrate that read and planning operations perform no product mutation, mutation consumes planned intent, selection is not re-evaluated, output sink does not influence selected membership, presentation does not alter semantics, and explanation uses the same retained facts as execution.

## Authority boundary
This document owns observable operation semantics for content loading after selection, carrier creation and delivery, inspection, structural verification, comparison, workspace-application planning, and explicit application.

`docs/spec/selection.md` owns candidate-universe and selected-set semantics. This specification consumes retained selection decisions and does not redefine them.

`docs/spec/dx-carrier.md` owns carrier representation, encoding, logical carrier-path validity, and format-level structural rules. It remains Draft.

`docs/spec/workspace-paths.md` owns physical workspace mapping, containment, entry-type, link, collision, permission-category, and applicability rules. It remains Draft.

Architecture owns responsibility boundaries, operation-specific internal plans, dependency direction, and separate mutation capabilities. Future diagnostic, CLI/process, and compatibility specifications own their respective public contracts.
