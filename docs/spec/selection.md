# Packing Selection Semantics
Status: Normative
Owner: DX workspace-to-carrier packing selection semantics
Scope: candidate-universe construction, scope, positive selectors, exclusions, ignore inputs, optional Git facts, override, deterministic selected-set construction, and per-candidate decisions
Maturity: Accepted

## Purpose
This specification defines the correctness-first semantics that determine which workspace-relative logical paths are selected for DX packing. It owns candidate-universe construction, selection rules, retained decision provenance, and deterministic selected-set production.

Selection consumes explicit facts. Discovery, filesystem access, Git invocation, content loading, carrier creation, carrier-output mutation, presentation, and process behavior remain outside selection.

## Scope
### In scope
This specification governs:
- candidate identity and candidate facts;
- packing candidate-source semantics and explicit source composition;
- candidate-universe construction and deduplication;
- scope;
- candidate-universe safety restrictions;
- positive selectors;
- final and soft exclusions;
- override authority;
- explicitly supplied DX-ignore rules;
- optional, explicitly supplied Git candidate and ignore facts;
- path-pattern and extension-selector semantics;
- rule ordering;
- per-candidate outcomes and provenance;
- empty selected-set semantics;
- deterministic selected-set construction;
- the reference selection procedure;
- required conformance evidence.

### Out of scope
This specification does not govern:
- carrier framing, encoding, serialization, or preservation;
- mapping logical paths to physical workspace targets or determining workspace applicability;
- candidate discovery mechanics or filesystem traversal algorithms;
- content loading, binary classification, or content policy;
- carrier-output safety, creation, persistence, or mutation;
- operation-wide success, failure, planning, or application;
- CLI commands or option spelling;
- streams, numeric process outcomes, or machine-output fields;
- Git executable discovery, subprocess behavior, or output decoding;
- historical compatibility classifications;
- internal expression trees, modules, classes, functions, or implementation architecture.

## Terminology
**Logical path** means exact workspace-relative, slash-separated path text used as selection identity.

**Candidate** means one logical path together with the explicit facts supplied for selection.

**Candidate source** means a declared source of candidate facts: an explicit file, explicit subtree, broad recursive workspace discovery, or optional Git-derived candidates.

**Candidate universe** means the deduplicated candidates admitted by declared candidate sources, scope, request validity, and candidate-universe safety.

**Positive selector** means an exact path, subtree, path glob, or filename-extension suffix that can admit a candidate after it enters the candidate universe.

**Final exclusion** means an exclusion that no selection or override authority can reverse.

**Soft exclusion** means an effective DX-ignore exclusion or explicit Git-ignore exclusion fact that permitted override authority can reverse.

**Override authority** means an explicit and narrowly bounded authority to reverse soft exclusions only.

**Decisive outcome** means the semantic result that determines whether one candidate is selected.

## Inputs
Complete selection input consists of:
- a selection semantic version;
- explicit candidate facts and all source contributions;
- explicit-selection attribution;
- zero or more scopes;
- zero or more positive selectors;
- zero or more final exclude path patterns;
- zero or more excluded extensions;
- zero or more dedicated override path patterns;
- zero or more explicitly declared DX-ignore sources in request order, each with ordered rules and source identity;
- optional Git candidate facts;
- optional Git-ignore facts and their declared evaluation context;
- candidate availability and unsupported-source facts;
- the mandatory `.git` protection rule;
- exact logical path text.

Selection MUST NOT obtain missing facts by filesystem access, Git invocation, environment access, current-directory lookup, or presentation state.

## Candidate identity and facts
A candidate is identified only by its exact logical path text. Identity is case-sensitive and Unicode-preserving. Selection MUST NOT case-fold, normalize Unicode, or use a physical absolute path as semantic identity.

Candidate facts include, where applicable:
- logical path;
- relevant source-entry kind;
- every contributing candidate source;
- explicit exact-file contribution;
- explicit subtree contribution;
- optional Git candidate facts;
- scope membership or facts sufficient to determine it;
- availability or unsupported-source status.

Contributions with the same logical path are merged into one candidate. Deduplication MUST retain all contributing provenance and MUST NOT create duplicate selected paths.

## Candidate sources and universe construction
The candidate-source classes are:
- explicit file;
- explicit subtree;
- broad recursive workspace discovery;
- optional Git-derived candidates.

Declared candidate sources compose by union. No source class has precedence over another.

An explicit file is both a candidate-source request and an exact positive selector. An explicit subtree is both a recursive candidate-source request and a subtree positive selector.

A missing explicitly requested candidate is represented as unavailable requested input. Broad discovery contributes only observed paths and therefore does not create an unavailable result for a path it did not discover.

An object that cannot be represented as a supported source candidate is not an ordinary excluded path. Its candidate fact records an unsupported source object or another applicable precondition outcome.

## Scope
Scope is part of candidate-universe construction. It is not an include pattern, an exclusion, or override authority.

A file scope admits only its exact logical path. A directory scope admits its subtree. Repeated scopes form an unordered union. Overlapping scopes do not duplicate candidates.

When no scope is declared, the declared candidate-source boundary applies. A candidate outside every declared scope is not in the candidate universe. An outside-scope explanation fact MAY be retained.

An explicit exact-file or subtree selector outside the declared scope is an invalid request combination. Path patterns always use workspace-root-relative coordinates and are never rebased by scope.

## Candidate-universe safety
The logical path `.git` and every descendant of `.git` are outside the candidate universe. This is a workspace-source safety restriction, not an exclusion. No override authority can admit such a path.

Discovery and explicit-source processing do not follow symbolic links. A symbolic link or another unsupported source object is represented by the applicable unsupported or unavailable fact and is not treated as an ordinary exclusion.

Paths outside the workspace source root, invalid logical paths, unavailable candidates, and unsupported objects fail applicable preconditions. Override cannot reverse those conditions.

## Positive selection
Positive selector classes are:
- exact logical path;
- logical subtree;
- path glob;
- filename-extension suffix.

When no positive selector exists, every candidate in the universe passes positive selection. When at least one positive selector exists, a candidate passes when one or more selectors match. Positive selectors compose by unordered union.

An ordinary positive path glob or extension selector does not override a soft exclusion.

### Extension selectors
An include extension is a positive filename-suffix selector. An exclude extension is a final filename-suffix exclusion.

Extension input is normalized to one leading dot. Matching compares the candidate filename suffix using ASCII case-insensitive comparison. Extension selectors are semantic suffix selectors and MUST NOT be translated into public glob text.

## Final exclusions
Final exclusions are:
- explicit exclude path globs;
- excluded extensions.

Final exclusions are unordered and decisive when matched. No positive selector, DX-ignore re-inclusion, explicit path, subtree contribution, or override selector reverses a final exclusion.

All matching final-exclusion facts are retained even when one match is sufficient to decide `excluded_final`.

## Soft exclusions
Soft exclusions are:
- the effective DX-ignore exclusion;
- an explicit Git-ignore exclusion fact.

A soft exclusion rejects a candidate unless accepted override authority exists. DX-ignore and Git-ignore are independent. DX-ignore re-inclusion changes only the DX-ignore state and does not reverse a Git-ignore fact.

## Override authority
Override authority comes only from:
- an explicit exact-file selector;
- an explicit subtree selector that contributed the candidate;
- a dedicated override path-glob selector.

Override authority can reverse only an effective DX-ignore exclusion or Git-ignore exclusion.

Override authority cannot reverse:
- scope;
- final exclusions;
- `.git` protection;
- invalid paths;
- unavailable requested candidates;
- symbolic-link restrictions;
- unsupported source objects;
- content-loading failures;
- carrier-output safety;
- physical workspace safety.

The semantic primitive is override authority, independent of invocation vocabulary.

## Explicit DX-ignore input
DX-ignore is explicit operation input. A root `.dxignore` has no effect merely because it exists. A process boundary MAY resolve such a file into a request, but activation, identity, contents, and ordering MUST be visible in semantic input.

Each declared ignore source provides:
- source identity;
- ordered rules;
- workspace-root-relative interpretation;
- source line for explanation.

Multiple sources are evaluated in declared request order. Rules within each source are evaluated in physical order. The combined sequence uses last matching rule semantics.

Rule forms are:
- blank;
- comment;
- exclusion pattern;
- `!`-prefixed re-inclusion pattern.

An unescaped initial `#` begins a comment. An escaped initial `#` is pattern text. An escaped initial `!` is pattern text. An unescaped initial `!` denotes re-inclusion and is not part of the pattern.

A re-inclusion rule changes only the DX-ignore state. It does not override final exclusions, Git-ignore facts, or safety constraints.

A missing or unreadable explicitly declared ignore source is an invalid or unavailable request input. A malformed rule makes the declared ignore input invalid. Selection MUST NOT silently omit either condition.

## Optional Git facts
Git candidate and Git-ignore capabilities are optional and independently requested. Selection never invokes Git and Git is not active merely because a repository exists.

A Git integration boundary supplies explicit candidate or ignore facts. Git-ignore input includes:
- the effective ignored or not-ignored decision;
- relevant rule source and pattern where available;
- declared evaluation context;
- availability or failure.

Selection MUST NOT reconstruct ignore behavior from Git status. Undeclared ambient global Git configuration MUST NOT influence supplied facts.

When a requested Git capability is unavailable, the result is unavailable external capability. There is no silent fallback. When Git behavior is not requested, Git availability is irrelevant.

## Absence of implicit exclusions
There are no implicit default exclusions. Editor artifacts, operating-system artifacts, temporary-file conventions, and similar names are selected unless excluded by explicit input or another rule in this specification.

Equivalent exclusions may be supplied explicitly. A future named standard exclusion set requires separate authority and explicit activation.

## Carrier-output boundary
An intended carrier-output path is not a selection rule. It MUST NOT be inserted as a hidden exclude pattern and MUST NOT change selected-set membership.

Output self-reference is handled by carrier-creation planning and operation safety after selection.

## Pattern dialect
Patterns match complete workspace-relative logical path text. Matching is case-sensitive, Unicode-preserving, locale-independent, slash-separated, and never rebased by scope.

The dialect supports:
- `*`, matching zero or more non-slash characters;
- `**`, matching zero or more characters including slash;
- `?`, matching one non-slash character;
- `[abc]` and `[a-z]`, matching one listed or ranged character;
- `[!abc]`, matching one character not in the class;
- backslash, escaping the next pattern metacharacter.

A pattern is invalid when it has any of these forms:
- empty;
- leading slash;
- trailing slash;
- repeated slash;
- a `.` or `..` component;
- trailing escape;
- malformed character class.

Patterns do not trigger candidate discovery. Directory-subtree intent uses a subtree selector or an explicit pattern such as `docs/**`.

Leading `!` is reserved for DX-ignore rule syntax and is invalid in ordinary include, exclude, and override patterns.

## Rule ordering
The following are unordered unions:
- candidate-source contributions;
- scopes;
- positive selectors;
- final exclude patterns;
- excluded extensions;
- override selectors.

Only DX-ignore rules form an ordered sequence. Git-ignore is an independent per-candidate fact. Explicit path and extension exclusions are final.

Request validity, source availability, `.git` safety, symbolic-link restrictions, output self-reference, and content readability are preconditions or adjacent-operation concerns, not ordered selection rules.

## Reference selection procedure
A conforming implementation MUST produce the same semantic result as this correctness-first procedure:

```text
validate explicit inputs
→ construct and deduplicate candidate universe
→ apply scope
→ apply candidate-universe safety
→ evaluate positive selection
→ evaluate final exclusions
→ evaluate DX-ignore and Git-ignore
→ evaluate permitted override
→ produce selected paths
→ forward selected paths to content loading
```

For each candidate:

1. If it is outside the candidate universe or safety boundary, produce the applicable non-selection outcome.
2. If positive selectors exist and none matches, produce `positive_not_matched`.
3. If any final exclusion matches, produce `excluded_final`.
4. If a soft exclusion exists and no permitted override authority exists, produce `excluded_soft`.
5. Otherwise, produce `selected`.

The decision MUST retain matched facts and the decisive outcome. Execution and explanation MUST consume the same retained decision and MUST NOT re-evaluate membership independently.

This procedure defines semantic reference behavior. It does not prescribe replaceable implementation structure or optimization.

## Selection outcomes and provenance
Semantic outcome names include:
- `selected`;
- `outside_scope`;
- `protected_workspace_metadata`;
- `positive_not_matched`;
- `excluded_final`;
- `excluded_soft`;
- `unsupported_source_object`;
- `unavailable_requested_candidate`.

Additional outcomes MAY distinguish invalid request or unavailable external capability when the distinction is within this specification's scope. Presentation may render different wording, but it MUST preserve the semantic distinction.

Retained semantic facts include, where applicable:
- candidate path;
- contributing candidate-source classes;
- explicit contribution;
- scope result;
- positive matches;
- final exclusion matches;
- effective DX-ignore rule;
- Git-ignore fact;
- override authority;
- decisive outcome;
- unavailable or unsupported fact.

Explanatory facts MAY include:
- source operand;
- Git status;
- ignore source;
- ignore source line;
- pattern text;
- overridden rule;
- duplicate contributions;
- nondecisive matches.

Presentation-only data is not selection semantics.

## Content-loading boundary
Selection produces logical paths and retained decisions. It does not load file bytes.

The following occur after path selection:
- binary classification;
- binary skip or fail policy;
- unreadable selected file handling;
- a source becoming nonregular after observation;
- a disappearing path;
- mutation between discovery and loading;
- carrier text or base64 encoding.

These later outcomes MUST NOT be retrospectively classified as path exclusions. A selected binary path and any other selected path are forwarded to content loading.

## Empty selected set
An empty selected set is valid semantic output. It retains one or more applicable reason categories:
- empty candidate universe;
- scope empty;
- positive selectors matched none;
- all finally excluded;
- all softly excluded;
- all unavailable or unsupported;
- mixed empty reasons.

Whether carrier creation accepts or rejects an empty selected set belongs to operation semantics. Selection assigns no process outcome.

## Validation
Explicit inputs MUST be validated before selected-set construction. Invalid scope, logical path, ordinary pattern, extension selector, DX-ignore rule, declared ignore source, or contradictory explicit selector and scope combination is an invalid selection request.

Requested candidate or external-capability unavailability MUST remain distinguishable from an ordinary non-match. Unsupported source objects MUST remain distinguishable from exclusions.

A conforming implementation MUST reject malformed explicit input rather than guess its intended meaning.

## Determinism and environmental inputs
For identical complete semantic inputs, selection MUST produce the same selected paths, per-candidate outcomes, and relevant provenance.

Selection MUST NOT depend on:
- current working directory after request resolution;
- filesystem enumeration order;
- locale;
- environment variables;
- automatic `.dxignore` activation;
- undeclared Git configuration;
- output destination;
- payload bytes;
- binary classification;
- timestamps;
- randomness;
- presentation mode.

Selected paths have set semantics. Any ordered representation used downstream MUST use a stable ordering determined from exact logical path text and MUST NOT inherit discovery enumeration order.

## Results and errors
Within this specification's authority, observable result categories distinguish:
- valid selection result;
- invalid selection request;
- unavailable explicitly requested candidate;
- unsupported source object;
- unavailable requested external capability;
- selected and non-selected per-candidate decisions;
- valid empty selected set.

Operation-wide aggregation, diagnostics, process representation, and numeric outcomes belong to later authorities.

## Compatibility
No historical selection compatibility classification is established.

Existing behavior is informative evidence only. The accepted semantics deliberately replace observed designs that relied on:
- source-mode precedence;
- a semantic only mode;
- automatic `.dxignore` activation;
- implicit Git activation;
- implicit default exclusions;
- override of `.git` protection;
- broad override beyond soft exclusions;
- hidden output self-exclusion;
- binary or unreadable outcomes treated as path selection.

This section records differences for clarity and does not create compatibility authority.

## Applicable schemas
None. This specification has no schema-governed boundary.

## Required verification
Conformance evidence MUST exercise the reference procedure, decisive outcomes, retained provenance, and deterministic membership across the following matrix.

### Candidate sources
- explicit file;
- explicit subtree;
- broad recursive discovery;
- Git-derived source;
- composed sources;
- duplicate contributions merged with provenance;
- missing explicit candidate;
- unsupported source object;
- source outside the workspace root;
- `.git` and descendants.

### Scope
- absent scope;
- file scope;
- subtree scope;
- repeated scopes;
- overlapping scopes;
- candidate outside every scope;
- explicit selector outside scope;
- root-relative pattern coordinates unchanged by scope.

### Positive selection
- absent positive selectors;
- exact-path match and miss;
- subtree match and miss;
- glob match and miss;
- extension match and miss;
- union across selector classes;
- interactions with Git-derived candidates.

### Final exclusions
- path exclusion;
- extension exclusion;
- multiple matching exclusions;
- positive selector plus final exclusion;
- override authority plus final exclusion.

### DX-ignore
- no matching rule;
- exclusion;
- exclusion followed by re-inclusion;
- re-inclusion followed by exclusion;
- multiple declared files in request order;
- escaped initial `!` and `#`;
- malformed rule;
- unavailable declared source;
- ordinary include interaction;
- explicit exact-file or contributing-subtree override;
- dedicated override selector.

### Git
- capability not requested;
- requested and not ignored;
- requested and ignored;
- ignored plus ordinary include;
- ignored plus override authority;
- requested capability unavailable;
- undeclared configuration demonstrated not to influence semantics.

### Patterns
- `*`, `**`, `?`, character classes, ranges, negated classes, and escapes;
- malformed class;
- trailing escape;
- leading, trailing, and repeated slash forms;
- `.` and `..` components;
- case-sensitive matching;
- Unicode preservation and matching.

### Empty outcomes
- every defined empty reason;
- a mixed-reason empty result;
- retained per-candidate reasons when the selected set is empty.

### Boundaries
- selected binary path forwarded to content loading;
- unreadable selected path forwarded to later content failure;
- disappearing selected path handled after selection;
- output destination demonstrated not to change selection;
- presentation demonstrated not to change membership;
- explanation and execution demonstrated to use the same retained decision.

Verification MUST also demonstrate independence from candidate enumeration order, locale, timestamps, randomness, current-directory changes after request resolution, automatic ignore files, and unavailable unrequested Git.

## Authority boundary
This document is the Accepted authority for DX workspace-to-carrier packing selection semantics. It owns candidate-universe construction, scope, positive selection, exclusions, explicit ignore and optional Git facts, override authority, deterministic selected-set construction, and per-candidate decisions.

`docs/spec/dx-carrier.md` is Accepted and owns carrier representation and logical carrier-path validity within its declared boundary. This specification uses logical path text as supplied selection identity without redefining carrier semantics.

`docs/spec/workspace-paths.md` is Accepted and owns physical workspace mapping and applicability within its declared boundary. This specification does not decide physical applicability.

Discovery supplies explicit candidate facts but remains outside selection. Content loading follows selection. Carrier creation is plan-mediated, and carrier-output mutation and safety remain outside selection. Optional Git capabilities remain external. Architecture continues to own dependencies, capabilities, and internal plan boundaries. Future operation, diagnostic, CLI/process, and compatibility specifications own their respective concerns.
