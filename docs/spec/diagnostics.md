# DX Diagnostic Semantics
Status: Normative
Owner: DX semantic diagnostics, explanations, and human/machine diagnostic agreement
Scope: Diagnostic interpretation of retained semantic results and findings, automation-relevant finding identifiers, required diagnostic context, warnings, suggestions, causal context, ordering, stability, and human/machine agreement
Maturity: Accepted

## Purpose
This specification defines how DX explains already-determined semantic results and retained findings to human and machine consumers. It establishes diagnostic kinds, stable automation-relevant identifiers, required context, human and machine agreement, warning and suggestion boundaries, partial-failure reconstruction, ordering, and stability.

Diagnostics consume authoritative semantic results and retained findings. They do not determine selection, operation outcomes, workspace relationships, conflicts, effects, or mutation state.

## Scope
### In scope
This specification governs:
- the distinction between semantic result, diagnostic, and presentation;
- diagnostic kinds and blocking status;
- stable symbolic identifiers for automation-relevant findings;
- primary-result and supporting-finding relationships;
- selection explanations from retained decisions;
- diagnostic requirements for carrier creation, inspection, structural verification, comparison, and application;
- partial-failure reconstruction;
- warning and remediation semantics;
- typed resource references and bounded cause chains;
- internal-defect diagnostics;
- human and machine semantic agreement;
- verbosity, ordering, and diagnostic stability;
- semantic information required by a future machine representation;
- stream and process handoff categories.

### Out of scope
This specification does not govern underlying selection or operation semantics, carrier grammar, workspace mapping, final human prose, colors, tables, concrete machine fields, data schemas, standard-stream ownership, CLI spelling, verbosity options, broken-pipe process behavior, numeric process results, logging internals, stack-trace policy for development tooling, exception class contracts, or internal plan representation.

## Fundamental invariant
The governing flow is:

```text
semantic operation
→ authoritative typed semantic result plus retained findings and provenance
→ diagnostic interpretation
→ human or machine presentation
```

A presentation MUST NOT be reparsed to establish product meaning. A machine presentation MUST NOT perform a separate semantic evaluation.

Diagnostics MUST NOT rerun selection, carrier parsing, content loading, workspace mapping, comparison, application planning, conflict evaluation, or mutation-state evaluation. Human and machine presentations derive from the same semantic result and retained findings.

## Result, diagnostic, and presentation
**Semantic result** means the authoritative outcome produced by selection or an operation. It exists independently of diagnostics and presentation.

**Diagnostic** means a structured explanation of a semantic result and its relevant retained facts. A diagnostic references the result and MUST NOT replace, weaken, strengthen, or recalculate it.

**Presentation** means a human or machine rendering of the semantic result and diagnostics. Wording, formatting, grouping, and localization are presentation concerns unless this specification assigns semantic significance.

A diagnostic is not a second result system. Ordinary success need not produce a finding merely to narrate success.

A finding is required when necessary to explain a semantic negative result, invalid input, invalid carrier, unsupported version or capability, safety or state conflict, environmental failure, verification difference, changed precondition, partial failure, or internal failure.

## Diagnostic taxonomy
DX uses these diagnostic kinds:
- **blocking finding**, explaining why intended semantic completion was prevented;
- **difference finding**, describing an expected-versus-observed difference;
- **negative-result finding**, explaining a valid completed operation that did not produce the requested positive artifact or match;
- **warning**, identifying an important non-blocking condition;
- **informational finding**, providing relevant explanation or provenance;
- **progress or effect fact**, recording planned, completed, untouched, satisfied, or uncertain effects.

Diagnostic kind and semantic result category are independent. A comparison may complete correctly with a verification-difference result and difference findings. A success result may contain a warning. A partial-failure result has a blocking finding and effect-state facts.

The taxonomy MUST NOT mirror every semantic result with a redundant diagnostic category.

## Stable symbolic identifiers
DX uses stable symbolic identifiers for automation-relevant findings. It does not require an identifier for every prose sentence, ordinary result fact, suggestion, or display element.

Identifiers:
- use lowercase concern-qualified names with underscore-separated words;
- identify semantic finding kinds;
- are independent of prose wording and implementation exception names;
- contain no numeric process value;
- remain stable in semantic meaning.

Illustrative forms include `selection.positive_not_matched`, `creation.empty_selection`, `carrier.invalid_framing`, `comparison.content_different`, and `application.partial_failure`. These forms demonstrate naming style and do not constitute an exhaustive registry.

An identifier's meaning is compatibility-sensitive. Prose may change independently. One result may have several findings and identifiers. A genuinely new finding may receive a new identifier without changing existing meanings. Reusing an identifier for a materially different meaning is prohibited. Removal, merger, or material meaning change requires semantic-change and compatibility review.

Numeric diagnostic identifiers are not defined.

## Primary result and supporting findings
Every diagnostic interpretation preserves one primary semantic result.

A primary finding is required when a non-ordinary result needs a decisive explanation. This applies to invalid input, invalid carrier, unsupported behavior, conflict, environmental failure, changed precondition, partial failure, internal failure, creation-negative empty selection, and absent requested inspection entry.

A result may retain several independent blockers. Diagnostics MUST NOT invent one exclusive cause when semantics retained several.

Findings may be operation-level or resource-specific. Supporting findings may include contributing failures, differences, rule matches, provenance, overridden facts, completed effects, untouched effects, uncertainty, warnings, and suggestions.

Presentation may group equivalent findings, but it MUST preserve each resource-specific semantic fact or an equivalent lossless relationship.

## Selection explanation
Selection explanation consumes retained Accepted selection decisions without rematching patterns or reevaluating rule order.

### Selected
An explanation MAY expose the logical candidate path, selected outcome, candidate-source provenance, positive matches, and effective override authority. If override was required, the authority and overridden soft exclusion are mandatory.

### Outside scope
An explanation identifies the logical path, retained outside-scope outcome, and scope relationship. It MUST NOT describe scope as an exclusion pattern.

### Positive selector miss
An explanation identifies the logical path, `positive_not_matched`, and the fact that positive selection was active. Retained selector classes MAY be included. It MUST NOT recast the result as a final exclusion.

### Final exclusion
An explanation identifies `excluded_final` and retained matching final exclusions. All retained matches may be exposed, while the decisive outcome appears once. It MUST NOT suggest that ordinary override can reverse a final exclusion.

### Soft exclusion
An explanation identifies `excluded_soft`, the contributing DX-ignore or Git-ignore facts, and absence of permitted override. Retained ignore source, line, pattern, and Git source MAY be included.

### Permitted override
An explanation identifies the selected outcome, override authority, and soft exclusion reversed. It MUST NOT imply reversal of scope, final exclusion, protected metadata, unavailable input, unsupported source, or workspace safety.

### Protected metadata
An explanation identifies the protected workspace metadata outcome and `.git` candidate-universe safety. It MUST NOT describe it as an ordinary overridable exclusion.

### Unavailable or unsupported input
An unavailable requested candidate explanation identifies the requested logical path or operand and availability fact, distinct from broad-discovery absence. An unsupported source explanation identifies the path and retained source kind. An unavailable requested Git capability explanation identifies the explicit capability and absence of silent fallback.

### Empty selected set
An explanation exposes retained categories among empty candidate universe, empty scope, no positive match, all finally excluded, all softly excluded, all unavailable or unsupported, and mixed reasons.

Selection explanation distinguishes:
- **decisive fact**, determining the outcome;
- **supporting match**, relevant but nondecisive retained evidence;
- **provenance**, identifying candidate or fact origin;
- **suggestion**, optional non-semantic remediation.

A suggestion MUST NOT be represented as fact.

## Carrier-creation diagnostics
Carrier-creation diagnostics preserve the general output-sink model.

### Empty selected set
The diagnostic identifies the semantic negative result, retained empty-selection reasons, absence of executable creation intent, and absence of carrier-byte delivery. It MUST NOT describe the result as invalid carrier or successful empty-carrier creation.

### Content-loading failure
For a selected path that cannot be loaded, the diagnostic identifies the logical path, retained selected outcome, post-selection failure category, source observation or boundary cause, lack of accepted payload, and creation impact. It MUST NOT reinterpret the path as excluded.

A changed selected source additionally identifies the prior relevant observation, changed observation, and whether the change occurred before payload freezing or invalidated a later precondition. An unsupported selected source identifies the observed unsupported source kind.

### Output-sink delivery
Incomplete delivery identifies sink kind, required complete delivery, failure to complete, known delivery state where retained, and absence of successful carrier creation. An unavailable sink identifies sink kind, unavailability, and boundary cause. An uncertain final sink state identifies the affected delivery and resource-specific uncertainty.

These outcomes MUST NOT be represented as invalid carrier, selection failure, workspace conflict, or internal defect solely because delivery failed.

### Filesystem-sink findings
Filesystem-specific findings apply only when the selected sink is a filesystem path. They may identify destination, observed target type, missing or inapplicable replacement authority, self-reference relationship, unsafe or inaccessible parent, containment state, symlink conflict, and changed destination precondition.

A non-filesystem sink MUST NOT be assigned a fabricated output path, filesystem replacement policy, parent finding, symlink finding, or filesystem self-reference.

Self-reference explanation confirms that selected membership was unchanged. Replacement authority is a semantic fact, not CLI advice.

## Inspection diagnostics
Malformed carrier content produces an invalid-carrier finding with the most specific safe carrier location retained by parsing.

An unsupported carrier version produces an unsupported-version finding and MAY include the declared version and supported-version context. It MUST NOT be presented as ordinary malformed content when the governing carrier semantics distinguish it.

An absent requested entry produces a semantic negative-result finding with the exact requested logical carrier path. It MUST NOT be confused with a missing workspace target.

Carrier-byte acquisition failure produces an environmental finding identifying carrier source kind, boundary cause, and whether parsing began.

Entry count, path list, decoded sizes, attributes, read-only declarations, and calculated hashes are normal inspection result facts and MUST NOT become warnings merely because they are presented.

Duplicate logical paths produce invalid-carrier findings where the governing carrier authority requires uniqueness.

## Structural-verification diagnostics
Structural-verification presentation is limited to the supported structural claim. A success presentation conveys meaning equivalent to `structure valid`, not an unqualified claim of a trusted or comprehensive verification.

Invalid structural findings may distinguish malformed framing, invalid or unknown attribute, invalid payload representation, invalid logical path, duplicate logical path, missing required structure, and prohibited trailing content when those distinctions are retained by carrier semantics.

Structural diagnostics MUST NOT claim authenticity, origin, authorization, trusted integrity without a trusted expected value, absence of harmful content, workspace equality, workspace applicability, safe application, or historical compatibility.

Calculated decoded-entry hashes are inspection facts. A calculated hash alone is not integrity verification. Workspace agreement is comparison.

Unsupported version remains unsupported. Carrier-byte acquisition failure remains environmental failure. Ordinary invalid structure MUST NOT be represented as an internal defect.

## Comparison diagnostics
An identical relation is an ordinary result fact and requires no warning or per-path finding unless detailed explanation was requested.

Missing, differing, and explicitly requested workspace-only relations are result facts and difference findings. They identify the logical or workspace-relative resource, observed relation, read-only status where applicable, and retained extra-scope provenance where applicable. A workspace-only path MUST NOT imply deletion intent.

A read-only discrepancy identifies read-only status and its actual missing or differing relation.

Directory and symlink conflicts support conflict results. A symlink finding identifies final or ancestor status when retained and MUST NOT follow the link for explanation.

Unsupported-object findings identify the retained object category without treating it as a regular file. Observation failures identify the required observation, affected reference, and boundary cause.

Containment, mapping, and path-identity collision findings identify participating logical paths and retained mapping failure. Diagnostics MUST NOT silently choose one colliding path.

Historical display letters are not semantic diagnostic identifiers.

## Application diagnostics
Create and replace are planned or completed effect facts, not warnings. Replacement explanation identifies target observation and explicit authority.

A satisfied target is an ordinary result or effect fact. It is not an explicit skip and is not a warning.

An explicit skip MUST remain visible. Its finding identifies the logical path, explicit skip authority, observed target relation, and the represented content left unsatisfied. It MUST NOT be presented as complete application success.

A read-only satisfied target is an ordinary optional informational fact. A read-only discrepancy MUST remain visible and identifies logical path, read-only status, missing or differing relation, lack of mutation authority, and impact on full application satisfaction.

Conflict, unsupported-target, and observation-failure findings identify the affected resource, retained observation, and actual semantic cause. Parent creation appears as planned, completed, untouched, or uncertain effect evidence as applicable.

Changed-precondition explanation identifies the saved precondition, revalidated observation, affected effect, and previously completed effects where applicable. It MUST NOT imply silent replanning.

A no-change application exposes operation-level success with no change. Per-path satisfied facts need not be emitted as warnings.

## Partial-failure diagnostics
A partial-failure diagnostic MUST contain enough retained evidence to reconstruct the known post-operation state without implying rollback.

Mandatory operation-level facts are:
- partial-failure primary result;
- failed effect and reason;
- deterministic intended-effect order or equivalent ordering reference;
- point after which no later effects were attempted;
- known or uncertain final state of the failed resource.

Every relevant planned effect is classified as at least one of:
- **known changed**, meaning its effect completed;
- **known unchanged**, meaning the resource is known not to have changed from the operation;
- **not attempted**, meaning execution stopped before the effect;
- **state uncertain**, meaning final resource state cannot be established.

Satisfied entries MAY remain separately identified, but MUST NOT obscure these reconstruction meanings.

The diagnostic identifies completed effects, failed effect, untouched effects, resource-specific uncertainty, changed preconditions, and parent directories created before failure. Untouched effects are described as not attempted, not rolled back or skipped.

Diagnostics MUST NOT state or imply rollback unless a future accepted operation contract provides it.

## Warning semantics
A warning is non-blocking and:
- is grounded in retained facts;
- is important to interpretation, safety, or compatibility;
- does not prevent the primary result;
- does not replace an error, conflict, difference, or unsupported result;
- does not narrate routine success;
- is not speculative advice;
- does not expose a mere implementation detail.

Selected files, binary entries, satisfied targets, normal parent creation, verification differences, conflicts, unsupported behavior, and partial failure are not warnings merely because they exist.

The initial mandatory diagnostic contract MUST NOT invent warnings whose semantic source has not been admitted by an upstream authority.

## Suggestions and remediation
Diagnostics MAY include remediation suggestions. Suggestions are non-semantic, explicitly distinct from facts, replaceable, excluded from semantic identity, and forbidden from altering result meaning or claiming universal safety.

Machine consumers must be able to distinguish a suggestion from a fact.

Suggestions use conceptual remediation such as `explicit replacement authority is required`. They MUST NOT hard-code CLI spelling before CLI/process authority establishes it.

## Typed resource references
Diagnostics distinguish:
- logical carrier path;
- workspace-relative coordinate;
- physical workspace path;
- filesystem sink destination;
- non-filesystem sink;
- ignore source;
- Git-derived source or capability.

A logical carrier path MUST NOT be represented as physical workspace identity. A non-filesystem sink MUST NOT be assigned a filesystem path.

Physical details MAY be omitted or reduced when not retained, unnecessary, unsafe to disclose, or harmful to portability. Terminal quoting and escaping are outside this specification.

## Cause-chain semantics
A public diagnostic cause chain has bounded layers:
1. semantic category;
2. boundary category;
3. typed resource context;
4. optional underlying environmental cause;
5. optional debug detail outside the stable public contract.

Boundary categories may include carrier acquisition, carrier parsing, content loading, output delivery, workspace observation, and workspace mutation.

Implementation exception class names and arbitrary exception prose MUST NOT be stable public identifiers. Operating-system detail MAY be attached when useful, but it does not replace semantic meaning and is not automatically compatibility-sensitive.

Stack traces are not normal diagnostics.

## Internal-defect boundary
Internal failure is reserved for an invariant violation or otherwise unclassified internal defect.

Invalid input, malformed carrier, unsupported capability, conflict, permission failure, changed precondition, output-delivery failure, comparison difference, and externally caused partial failure MUST NOT be classified as internal defects.

A genuine internal-failure diagnostic exposes a stable high-level category and bounded operation context. Arbitrary exception prose is excluded from semantic identity. Optional debugging details are separated and MUST NOT expose secrets or irrelevant host state.

This specification defines no logging framework.

## Human and machine agreement
For the same semantic result, human and machine presentations MUST agree on:
- primary semantic result;
- success, non-success, completion, and satisfaction meaning;
- affected paths, sinks, entries, and effects;
- blocking findings;
- verification differences;
- conflicts and unsupported conditions;
- environmental failures;
- explicit skips and read-only discrepancies;
- partial completion and uncertainty;
- effects not attempted.

They MAY differ in wording, formatting, localization, grouping, explanation depth, explicitly non-semantic ordering, presentation hints, and optional suggestions.

Neither presentation may make a stronger or weaker semantic claim. Agreement is semantic, not textual or structural identity.

## Verbosity
Verbosity is not semantic. It MUST NOT alter result category, mandatory blocking findings, necessary affected-resource references, differences, explicit skips, read-only discrepancies, partial completion, uncertainty, selection membership, planning, mutation, or eventual process meaning.

Even a quiet presentation contract preserves access to a non-success result, primary blocker, required affected resource, partial-failure meaning, uncertainty, and incomplete satisfaction.

CLI verbosity controls are outside this specification.

## Diagnostic ordering
Diagnostic ordering is deterministic where it carries explanatory meaning:
- partial-failure effects use execution order;
- planned mutation effects use plan order;
- ordered ignore evidence uses retained semantic order;
- structural findings use physical carrier order where location matters;
- cause chains proceed from semantic to boundary to environmental context.

For unordered finding sets, stable ordering is independent of ambient filesystem enumeration. Exact logical path, symbolic identifier, and retained source position provide the default tie-breaking basis where applicable.

Presentation MAY group findings differently if all semantic facts and human/machine agreement are preserved.

## Stability and compatibility
Compatibility-sensitive diagnostic properties are semantic result category, stable symbolic identifier and meaning, required typed resource references, blocking status, effect-state meaning, uncertainty, and required semantic ordering.

Prose, prefixes, punctuation, capitalization, layout, colors, wrapping, suggestion wording, and optional explanation depth are replaceable unless another authority accepts them.

No historical diagnostic compatibility classification is established by this specification. The following are informative migration observations only and do not alter current diagnostic semantics:
- replace exception-class-name machine errors with semantic identifiers;
- leave human error prefixes to presentation;
- defer usage repetition to CLI/process authority;
- migrate empty-selection messages to retained reason categories;
- migrate selection explanation to decisive fact, supporting match, provenance, and suggestion;
- migrate summaries to semantic result facts;
- narrow verification success to structural validity;
- migrate historical comparison letters to semantic differences;
- migrate application skips to skipped-unsatisfied findings;
- migrate completion summaries to explicit completed, satisfied, skipped, discrepant, and partial facts.

These observations do not create compatibility authority.

## Machine-readable semantic boundary
This specification defines semantic information needed by a future machine representation, not a concrete serialization.

Required semantic information includes:
- diagnostic contract evolution context;
- operation identity;
- primary semantic result;
- satisfaction or completion meaning;
- stable symbolic finding identifier;
- diagnostic kind and blocking status;
- affected typed resource reference;
- decisive facts and relationship to the primary result;
- verification-difference information;
- effect state and uncertainty;
- partial-failure completed, failed, untouched, and uncertain relationships;
- semantic ordering position where required.

Optional explanatory information includes provenance, supporting matches, source and line, expected and observed categories, already-computed sizes or digests, environmental cause, suggestion, and documentation reference.

Presentation-only information includes formatted text, colors, indentation, tables, glyphs, localized headings, terminal width, and display grouping.

A future schema requires an accepted machine producer/consumer or validator boundary. This specification defines no JSON fields or schema.

## Stream and process handoff
This specification forwards these semantic output classes to the CLI/process authority:
- primary product data;
- complete carrier bytes;
- exact extracted entry bytes;
- human diagnostic presentation;
- machine-readable result;
- help and version output.

It assigns no standard streams.

The following remains an informative downstream preference:

```text
pack without an explicit filesystem destination
→ carrier bytes to standard output

pack with an explicit filesystem destination
→ filesystem sink
```

This preference is not normative diagnostic behavior. CLI/process authority owns the final mapping, stream ownership, terminal safety, shell interaction, and process results.

A streaming sink that does not accept complete bytes produces an output-delivery outcome. It MUST NOT be classified as invalid carrier, selection failure, workspace conflict, or internal defect solely because delivery stopped. Broken-pipe process behavior belongs downstream.

## Validation
A diagnostic interpretation is conforming only when it derives from an authoritative semantic result and retained findings, preserves all mandatory distinctions, uses valid symbolic identifiers, and does not perform semantic reevaluation.

A presentation is nonconforming when it omits a mandatory blocker, difference, explicit skip, read-only discrepancy, partial effect, uncertainty, or affected resource needed to understand the result, or when it makes a stronger or weaker claim than the retained semantics.

## Results and errors
Diagnostic construction may itself fail only as an internal presentation-boundary defect. Such failure MUST NOT alter the underlying semantic result.

Normal underlying invalidity, conflict, unsupported behavior, environmental failure, verification difference, changed precondition, and partial failure retain their original semantic categories.

This specification assigns no numeric process values.

## Accepted dependencies
### Selection
DEPENDENCY: `docs/spec/selection.md`
STATUS: Accepted
REQUIRED RULES: Selection outcomes and retained decision facts.

### Operations
DEPENDENCY: `docs/spec/operations.md`
STATUS: Accepted
REQUIRED RULES: Semantic result categories, operation findings, output-sink distinctions, comparison relations, application effects, changed-precondition facts, and partial-failure state.

### Carrier format
DEPENDENCY: `docs/spec/dx-carrier.md`
STATUS: Accepted
REQUIRED RULES: Structural-invalidity distinctions and carrier locations retained by parsing and structural verification.

### Workspace paths
DEPENDENCY: `docs/spec/workspace-paths.md`
STATUS: Accepted
REQUIRED RULES: Mapping, containment, symlink, entry-type, collision, and workspace-applicability findings.

Concrete machine structure is a separate schema concern. Historical compatibility classification is not required to determine diagnostic-semantic conformance.

## Required verification
Conformance evidence MUST cover:

### Selection
- selected;
- outside scope;
- positive miss;
- final exclusion;
- soft exclusion;
- permitted override;
- protected metadata;
- unavailable requested candidate;
- unsupported source;
- unavailable requested Git capability;
- every empty-result reason and mixed empty reasons.

### Carrier creation
- success;
- empty selection;
- unreadable, changed, and unsupported selected sources;
- filesystem self-reference and output conflict;
- non-filesystem delivery failure;
- unavailable sink;
- uncertain sink state;
- no conversion of content failure into exclusion;
- no fabricated filesystem facts for a non-filesystem sink.

### Inspection and structural verification
- missing requested entry;
- invalid carrier;
- unsupported version;
- carrier-byte acquisition failure;
- valid structure;
- invalid framing, attribute, payload, and logical path;
- duplicate path;
- bounded structural-success claim and explicit trust limits.

### Comparison
- same;
- missing;
- different;
- requested workspace-only extra;
- read-only discrepancy;
- directory and symlink conflict;
- unsupported object;
- observation failure;
- containment conflict;
- path-identity collision;
- no deletion implication for extra paths;
- no symlink following for explanation.

### Application
- create;
- replace;
- satisfied;
- explicit skip;
- read-only satisfied and discrepancy;
- target conflict;
- unsupported target;
- observation failure;
- parent creation;
- changed precondition;
- no-change success;
- partial failure.

### Partial failure
- known changed;
- known unchanged;
- not attempted;
- state uncertain;
- created parents;
- failure stop point;
- no rollback implication.

### Human and machine agreement
- same primary result;
- same blocking findings;
- same affected resources;
- same differences, explicit skips, and read-only discrepancies;
- same partial and uncertain state;
- varied wording, grouping, and formatting without changed meaning;
- no stronger or weaker claim in either presentation.

### Ordering and stability
- stable logical-path ordering;
- execution-order effects;
- retained rule ordering;
- no accidental filesystem enumeration dependence;
- stable symbolic identifier meaning despite changed prose;
- multiple findings for one result.

## COMMON and ADR boundaries
`docs/spec/COMMON.md` is not warranted. Diagnostic semantics have one coherent owner here, while presentation-independence invariants already belong to architecture.

No new ADR is required. Existing architecture already establishes typed results and findings, presentation independence, provenance, and execution/explanation agreement.

## Maturity transition
This specification is Accepted because its taxonomy, identifiers, required context, ordering, stability, reconstruction, and human/machine agreement rules completely determine diagnostic-semantic conformance. Concrete machine structure and historical migration classification are separate concerns and are not blockers.

## Authority boundary
This document owns diagnostic interpretation of retained semantic results and findings, automation-relevant symbolic identifiers, required context, warning and suggestion boundaries, cause chains, ordering, stability, and human/machine agreement.

`docs/spec/selection.md` owns selection outcomes and retained selection facts. `docs/spec/operations.md` owns operation results, effects, findings, output-sink semantics, and partial-failure state. This document consumes but does not redefine them.

`docs/spec/dx-carrier.md` owns carrier validity distinctions. `docs/spec/workspace-paths.md` owns workspace mapping and applicability distinctions. Both are Accepted.

`docs/spec/cli-process.md` owns invocation, streams, terminal behavior, and process results. A separately admitted schema owns concrete machine representation. Historical migration commitments remain unspecified until admitted by a compatibility authority. Architecture continues to own dependency and presentation boundaries.
