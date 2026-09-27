# DX CLI and Process Semantics
Status: Normative
Owner: DX public invocation, standard streams, terminal behavior, machine-mode selection, and numeric process results
Scope: Canonical executable and commands, request grammar, process input and output channels, carrier-output sink selection, help and version behavior, machine mode, verbosity, environmental resolution, terminal safety, interruption, and numeric process outcomes
Maturity: Accepted

## Purpose
This specification defines the public process boundary for DX. It maps accepted semantic operations, results, diagnostics, primary product data, and retained findings to command invocation, standard streams, terminal behavior, machine-mode selection, and numeric process results.

The process boundary adapts requests and presents already-determined semantic outcomes. It MUST NOT re-evaluate selection, carrier validity, workspace applicability, operation effects, diagnostic meaning, or mutation state.

## Scope
### In scope
This specification governs:
- the canonical public executable identity;
- public command names;
- command-specific operands and options;
- repeated, ordered, mutually exclusive, and contradictory request forms;
- carrier acquisition from a file or standard input;
- standard-output and standard-error ownership;
- carrier-output sink selection;
- broken-pipe and incomplete-delivery process behavior;
- interactive-terminal safety;
- help, version, and no-argument behavior;
- machine-mode eligibility and stream purity;
- inspection projections;
- planning invocation;
- quiet and verbose presentation controls;
- numeric process results;
- environmental resolution at process entry;
- unsupported-capability presentation;
- bounded external-interruption behavior.

### Out of scope
This specification does not govern selection membership or precedence, carrier grammar or preservation, workspace mapping or applicability, operation result meaning, mutation effects, diagnostic identifiers or diagnostic semantics, machine-object fields, encoding of a machine representation, schema structure, historical compatibility classifications, package internals, modules, classes, exception types, internal plans, or replaceable parsing and stream algorithms.

## Fundamental process invariant
The governing process flow is:

```text
process request
→ validated public request
→ authoritative semantic operation
→ semantic result plus retained findings
→ diagnostic interpretation
→ process and presentation mapping
```

The process boundary MUST NOT rerun semantic rules. Numeric results, stream selection, human presentation, and machine presentation MUST consume the same authoritative semantic result and retained findings.

## Canonical executable identity
The canonical public invocation name is:

```text
dx
```

`dx.py` is provisional historical identity only and is not a normative executable name in this specification. Any obligation to retain, migrate, or remove that name is outside this current process contract and remains unspecified until separately classified.

The executable name does not constrain package name, module layout, implementation language details, or repository structure.

## Public commands
The normative command set is:

```text
dx pack
dx inspect
dx verify
dx compare
dx apply
```

The command mapping is:
- `pack`: plan or execute carrier creation;
- `inspect`: expose an inspection projection;
- `verify`: structurally verify a carrier;
- `compare`: compare a carrier with an explicit workspace;
- `apply`: plan or execute workspace application.

No alias is normative in the initial process contract. There is no normative `unpack` command. Raw extraction that bypasses application planning and workspace safety is not admitted.

## Request grammar
The public request forms are:

```text
dx pack [PATH ...] [selection options] [-o FILE] [--dry-run]
dx inspect CARRIER [projection]
dx verify CARRIER
dx compare CARRIER WORKSPACE [--workspace-only]
dx apply CARRIER WORKSPACE [--existing POLICY] [--create-parents] [--dry-run]
```

A `CARRIER` operand is either a filesystem operand or `-` for standard input. `WORKSPACE`, `PATH`, `FILE`, and file-valued options are filesystem operands resolved according to this specification.

### General request rules
- Singular positional carrier and workspace operands occur exactly where their command form requires them.
- Scalar options occur at most once unless this specification expressly makes them repeatable.
- Repeatable unordered semantic inputs compose according to their owning semantic specification after validation.
- Ordered inputs preserve command-line order.
- Mutually exclusive options, duplicate scalar options, contradictory policies, malformed values, unknown options, unknown commands, and missing required operands are invalid requests.
- Invalid requests MUST be rejected before the semantic operation is invoked.
- Omitted options MUST NOT imply overwrite, skip, parent creation, ignore activation, Git activation, or any other authority not established by the request and upstream semantics.
- CLI spelling MUST NOT redefine the meaning or precedence of semantic inputs.

### Packing operands and selection options
Each positional `PATH` contributes an explicit file or subtree candidate source. With no `PATH`, `pack` requests broad recursive discovery rooted at the resolved source root.

The initial selection option vocabulary is:

```text
--root DIR
--scope PATH
--include PATTERN
--exclude PATTERN
--override PATTERN
--include-extension EXT
--exclude-extension EXT
--ignore-file FILE
--git-candidates
--git-ignore
```

`--scope`, `--include`, `--exclude`, `--override`, `--include-extension`, `--exclude-extension`, and `--ignore-file` are repeatable. Declared ignore sources preserve request order. Other repeatable inputs follow the unordered composition rules of the selection authority.

No ignore file or Git capability is activated merely because it exists or is available. Requested Git candidate and Git-ignore capabilities are independent.

### Application policy
`--existing POLICY` supplies an explicit existing-target policy admitted by operation semantics. Its accepted values are:

```text
fail
skip
overwrite
```

Omission supplies no explicit policy. `--create-parents` supplies explicit parent-creation authority. Neither option overrides containment, symlink, unsupported-object, collision, or other non-overridable safety rules.

## Standard input
A carrier operand may be:

```text
FILE
-
```

`-` means carrier bytes are read from standard input.

Only one primary input may consume standard input in an invocation. A request requiring standard input for multiple independent inputs is invalid. Omission of a required carrier operand MUST NOT implicitly select standard input.

Carrier input is byte acquisition. It MUST NOT depend on terminal text encoding.

## Standard-output and standard-error ownership
Standard output owns the invocation's selected primary output class:
- complete carrier bytes from `pack` without `-o`;
- exact decoded entry bytes from `inspect --entry PATH`;
- one complete machine representation in machine mode;
- ordinary textual primary data such as summaries, lists, read-only paths, and hashes;
- help output;
- version output.

Standard error owns human diagnostic presentation and non-primary human explanation.

When standard output carries carrier bytes or decoded entry bytes, all human diagnostics use standard error.

A normal invocation MUST NOT mix machine-readable output and human prose on standard output.

## Carrier-output sink mapping
The public sink mapping is:

```text
dx pack ...
→ complete carrier bytes to standard output

dx pack ... -o FILE
→ complete carrier bytes to filesystem sink FILE
```

`--output FILE` is the long form of `-o FILE`.

Omission of `-o` selects the standard-output sink. DX MUST NOT invent a numbered output file, derive an output filename from a source operand, or choose an implicit filesystem destination.

This specification does not define `-o -` as a required duplicate spelling for the standard-output sink.

A filesystem output operand is not a selection rule and MUST NOT alter selected membership.

## Broken pipes and incomplete delivery
A broken pipe while writing complete carrier bytes is an incomplete output-delivery result.

The process MUST:
- stop attempting further delivery;
- avoid reporting successful carrier creation;
- avoid emitting an implementation traceback as normal product output;
- preserve output-delivery failure as the primary process-visible result;
- preserve uncertainty when the accepted byte prefix cannot be established.

Broken pipe MUST NOT be reclassified solely as invalid carrier, invalid request, selection failure, workspace conflict, or internal failure.

A broken pipe while delivering exact entry bytes or a machine representation is likewise a process-boundary environmental failure. It does not alter an already-determined underlying semantic result, but the invocation did not complete its requested delivery.

## Interactive-terminal safety
DX MUST refuse by default to write either of these byte streams directly to an interactive terminal:
- complete carrier bytes;
- exact decoded entry bytes.

The refusal is an invalid request and occurs before byte delivery.

The explicit override is:

```text
--allow-terminal-output
```

The override authorizes terminal delivery only. It does not alter payload bytes, carrier semantics, diagnostics, completion requirements, or any mutation authority.

Human text, help, version information, summaries, lists, hashes, plans, and machine-readable text MAY be written to a terminal.

## Help, version, and no-argument behavior
These invocations write their output to standard output and succeed:

```text
dx
dx --help
dx COMMAND --help
dx --version
```

No-argument invocation prints top-level help. Help and version processing MUST NOT:
- perform workspace discovery;
- read a carrier;
- request a Git capability;
- create a semantic plan;
- perform product mutation;
- depend on the current working directory for their meaning.

Unknown commands, missing required operands, and invalid option combinations are invalid requests rather than successful help requests.

Exact help prose and layout are presentation details unless separately accepted. Version output identifies the public DX version and does not expose internal module identity as a required contract.

## Machine mode
Machine mode is selected with:

```text
--machine
```

It is admitted for:
- `pack --dry-run`;
- `pack -o FILE`;
- `inspect`, except `inspect --entry PATH`;
- `verify`;
- `compare`;
- `apply --dry-run`;
- `apply`.

Machine mode is invalid when standard output is already the primary byte sink, including:
- `pack` without `-o`;
- `inspect --entry PATH`.

### Machine-mode purity
In machine mode:
- standard output contains exactly one complete machine representation;
- human warnings, progress text, headings, usage prose, and human diagnostics MUST NOT contaminate standard output;
- product diagnostics representable in the machine result MUST NOT also be emitted as human diagnostics to standard error;
- process value and machine primary result MUST agree;
- a process-boundary failure that prevents machine representation MAY use standard error, but it retains its applicable process result.

Machine mode consumes the semantic information required by the diagnostic authority, including primary result, satisfaction or completion meaning, stable symbolic findings, diagnostic kind and blocking status, typed resource references, decisive facts, differences, effects, uncertainty, partial-failure relationships, and required ordering.

This specification defines machine-mode existence, eligibility, purity, and semantic agreement. It defines no field names, object shape, serialization encoding, or schema. Prose owns semantics. A future schema decision owns machine-enforced structure only after its producer, consumers, and validation boundary are admitted.

## Inspection projections
`inspect` supports these primary projections:

```text
dx inspect CARRIER
dx inspect CARRIER --list
dx inspect CARRIER --read-only
dx inspect CARRIER --hashes
dx inspect CARRIER --entry PATH
```

The default projection is summary. At most one primary projection may be selected.

`--entry PATH` writes exact decoded entry bytes to standard output. It is incompatible with machine mode and is subject to interactive-terminal safety.

Summary, list, read-only, and hashes projections may use machine mode. A missing requested entry retains the semantic negative result owned by operation semantics.

Inspection projections MUST NOT strengthen inspection into structural verification, workspace comparison, trusted integrity, safe application, or authenticity.

## Planning and dry run
Planning is requested through `--dry-run` on the corresponding write command:

```text
dx pack ... --dry-run
dx apply CARRIER WORKSPACE ... --dry-run
```

There are no separate public plan commands.

`--dry-run`:
- invokes the applicable non-mutating planning operation;
- performs no product mutation;
- preserves the request semantics and authorities intended for execution;
- presents validated intended effects and retained findings;
- MUST NOT expose an internal plan representation as a public compatibility format.

Removing `--dry-run` requests execution through the applicable mutation capability. Preview and execution consume the same semantic decisions, subject to required precondition revalidation.

Machine mode may expose selected semantic plan facts but MUST NOT serialize an internal plan as the public contract.

## Quiet and verbose presentation
The process controls are:

```text
--quiet
--verbose
```

They are mutually exclusive and purely presentational.

`--quiet` suppresses optional human explanation. It MUST NOT alter standard-output primary data, semantic result, numeric process result, mandatory non-success meaning, required affected resource, partial-failure meaning, uncertainty, incomplete satisfaction, or machine output.

`--verbose` may add provenance and explanation only from retained facts. It MUST NOT rerun semantic rules or add a stronger or weaker claim.

## Numeric process results
DX defines this total mapping from the primary process-visible result category:

```text
0   success, including success with no change
2   invalid request
3   invalid carrier
4   unsupported version or capability
5   environmental failure, including incomplete stream delivery
6   safety or state conflict
7   verification difference
8   semantic negative result
9   changed precondition
10  partial failure
11  internal failure
```

The following rules govern the mapping:
1. The process value is a function of the primary semantic or process-boundary result, not prose, implementation exception type, diagnostic count, verbosity, or presentation mode.
2. Blocking findings explain the primary result but do not allocate independent numeric values.
3. Warnings do not change an otherwise successful process value.
4. Human and machine modes return the same numeric result for the same primary result.
5. A process-boundary failure that prevents requested output completion may replace an underlying successful semantic result with the applicable process-boundary failure value.
6. Values outside this mapping are not public DX result values.
7. Environment-imposed signal termination is not claimed as a portable DX-controlled numeric result unless DX handles it and produces one of the documented results.

The absence of value `1` is intentional in this mapping and creates no unspecified result category.

## Unsupported capability
When an explicitly requested version or capability is unsupported or unavailable:
- no silent fallback occurs;
- the primary result is unsupported version or capability;
- the requested capability and applicable support boundary are identified;
- the numeric process result is `4`;
- machine and human presentations preserve the same unsupported meaning;
- optional remediation MUST NOT claim that a fallback produced an equivalent result.

When an optional capability was not requested, its absence is irrelevant and produces no warning or failure.

## Environmental resolution
### Initial working directory
Relative filesystem operands are resolved exactly once against the process's initial working directory. Resolved locations, rather than a later working directory, become operation inputs.

Current-directory changes after resolution MUST NOT alter semantic targets, selection membership, output destination, or numeric results.

### Text and bytes
CLI option names, argument text, and human text use UTF-8 at the public process boundary.

Carrier bytes, source payload bytes, decoded entry bytes, and machine delivery bytes are byte-oriented and MUST NOT depend on terminal text encoding.

An input that cannot be represented or decoded under the admitted process contract produces the applicable invalid-request, unsupported-environment, or environmental-failure result. It MUST NOT be silently replaced or decoded with a different meaning.

### Locale and environment
Locale may affect localized human presentation only. It MUST NOT affect request parsing, logical-path identity, ordering, numeric process results, machine semantics, selection, or operation meaning.

The initial process contract admits no semantics-affecting environment variable. Undeclared environment variables MUST NOT alter public behavior.

Platform and terminal capabilities that affect process behavior must be resolved or reported explicitly. Support claims remain bounded to verified environments.

## External interruption
When DX catches an interruption after mutation begins and can retain operation evidence, it reports the applicable partial-failure result with completed, not-attempted, failed, and uncertain effects as available.

When the operating environment terminates the process before DX can produce a result, this specification makes no portable claim about a DX-controlled numeric process value.

External interruption MUST NOT be described as rollback. Known completed effects remain completed, and uncertain effects remain uncertain.

## Validation
A process request is valid only when:
- its command exists;
- required operands are present;
- scalar and repeatable options obey their declared cardinality;
- mutually exclusive and contradictory forms are absent;
- every value satisfies its public lexical requirements;
- standard input has at most one primary consumer;
- the selected primary-output modes are compatible;
- machine mode is compatible with the selected stdout class;
- terminal-delivery authority is present when required.

Invalid process requests MUST be rejected before semantic execution. Process validation MUST NOT silently choose a semantic policy or fallback capability.

## Results and errors
The process boundary maps authoritative semantic results and process-boundary delivery results to numeric values and presentation channels. It does not redefine their semantic meaning.

Usage or request parsing failure is `invalid request`. Failure to acquire required bytes is environmental unless the request itself is invalid. A presentation failure MUST NOT alter the already-determined semantic result, though inability to complete requested delivery may produce the applicable process-boundary failure result.

Implementation exception names, stack traces, and arbitrary operating-system prose are not stable process identifiers.

## Compatibility
No historical CLI or process compatibility classification is established by this specification.

Historical retention, migration, or removal obligations for the `dx.py` name, aliases, `unpack`, prior stdin conventions, prior numeric values, prior option spelling, prior defaults, prior stream usage, prior terminal behavior, and prior machine formats are unspecified. They do not alter the current process contract defined here.

This specification defines intended current process semantics. It does not claim that historical behavior is retained, intentionally replaced, safely removed, or covered by migration.

## Applicable schemas
None. This specification defines machine-mode semantics but no schema-governed structure.

The decision to expose machine outcomes establishes a candidate producer and consumers for later schema evaluation. A future schema decision must identify the concrete validation boundary without moving semantic meaning out of prose.

## Accepted dependencies
### Selection
DEPENDENCY: `docs/spec/selection.md`
STATUS: Accepted
CONSUMED RULES: Candidate-source composition, scope, selectors, exclusions, override authority, explicit ignore and optional Git inputs, ordered ignore-source behavior, and invalid selection inputs.

### Operations
DEPENDENCY: `docs/spec/operations.md`
STATUS: Accepted
CONSUMED RULES: Semantic operation set, planning and mutation distinction, output sinks, complete delivery, inspection projections, comparison, application effects, result categories, changed preconditions, and partial failure.

### Diagnostics
DEPENDENCY: `docs/spec/diagnostics.md`
STATUS: Accepted
CONSUMED RULES: Human/machine agreement, required diagnostic information, blocking status, stable symbolic findings, typed resource references, output-delivery classification, verbosity limits, uncertainty, and partial-failure reconstruction.

### Carrier format
DEPENDENCY: `docs/spec/dx-carrier.md`
STATUS: Accepted
CONSUMED RULES: Carrier-byte acquisition, supported and unsupported versions, structural validity, exact decoded entry bytes, and complete carrier-byte representation.

### Workspace paths
DEPENDENCY: `docs/spec/workspace-paths.md`
STATUS: Accepted
CONSUMED RULES: Explicit workspace roots, relative resource resolution, workspace applicability, unsupported environments, path meaning, and changed environmental preconditions.

Concrete machine structure is a separate schema concern. Historical compatibility classification is not required to determine current process conformance.

## Required verification
Conformance evidence MUST cover the important rules below without making test implementation part of this specification.

### Invocation and request validation
- canonical `dx` invocation;
- every public command;
- absence of normative aliases and `unpack`;
- required positional operands;
- repeatable unordered selection inputs;
- ordered ignore sources;
- duplicate scalar rejection;
- mutual-exclusion and contradiction rejection;
- malformed and unknown request rejection;
- invalid-request rejection before semantic execution;
- absence of implicit overwrite, skip, parent creation, ignore, or Git authority.

### Standard input
- carrier acquisition from a file;
- carrier acquisition from `-` on standard input;
- rejection of multiple stdin consumers;
- no implicit stdin from an omitted carrier operand;
- byte-oriented carrier acquisition independent of terminal encoding.

### Streams and sinks
- `pack` without `-o` delivers complete carrier bytes only to standard output;
- `pack -o FILE` selects the filesystem sink and does not place carrier bytes on standard output;
- `--output FILE` is equivalent to `-o FILE`;
- no implicit numbered or derived output file;
- human diagnostics use standard error when stdout contains primary bytes;
- output destination does not alter selected membership;
- broken pipe produces incomplete-delivery environmental failure and no success claim;
- uncertain accepted prefix remains uncertain.

### Terminal behavior
- carrier-byte refusal on an interactive terminal by default;
- exact-entry-byte refusal on an interactive terminal by default;
- refusal occurs before byte delivery;
- `--allow-terminal-output` permits delivery without changing bytes or semantics;
- non-byte human and machine text remains eligible for terminal presentation.

### Help and version
- no-argument help succeeds on standard output;
- top-level and command help succeed on standard output;
- version succeeds on standard output;
- help, version, and no-argument behavior perform no discovery, carrier read, Git request, planning, or mutation;
- their meaning is independent of the current working directory;
- unknown commands and invalid requests do not become help success.

### Machine mode
- eligibility for every admitted read, planning, and mutation form;
- rejection with `pack` stdout byte delivery;
- rejection with exact-entry byte delivery;
- exactly one complete machine representation on stdout;
- no human contamination of machine stdout;
- product diagnostics remain inside the machine result when representable;
- human and machine primary results and numeric process results agree;
- incomplete machine delivery reports process-boundary failure;
- machine mode does not expose internal plans or define semantics through structure.

### Inspection projections
- default summary;
- list;
- read-only paths;
- hashes;
- exact entry bytes;
- one-primary-projection exclusivity;
- exact-entry incompatibility with machine mode;
- terminal safety for exact entry bytes;
- missing requested entry preserves semantic negative-result meaning;
- projections do not strengthen the claim made by inspection.

### Planning and mutation
- `pack --dry-run` performs no product mutation;
- `apply --dry-run` performs no product mutation;
- no separate public plan commands;
- preview consumes the same semantic decisions as execution;
- machine plan facts do not expose internal plan representation.

### Verbosity
- quiet and verbose are mutually exclusive;
- quiet preserves primary output, non-success meaning, numeric result, partial state, uncertainty, and machine output;
- verbose uses retained facts without semantic reevaluation;
- verbosity does not alter mutation or selection.

### Numeric process mapping
Verification covers every public value and category:
- `0` success and success with no change;
- `2` invalid request;
- `3` invalid carrier;
- `4` unsupported version or capability;
- `5` environmental failure and incomplete delivery;
- `6` safety or state conflict;
- `7` verification difference;
- `8` semantic negative result;
- `9` changed precondition;
- `10` partial failure;
- `11` internal failure.

Verification also demonstrates:
- warnings do not change success;
- blocking-finding count does not allocate a value;
- human and machine modes agree numerically;
- verbosity does not alter the value;
- process-boundary delivery failure may replace underlying success;
- no undocumented public DX value is emitted.

### Unsupported capability
- requested unsupported version or capability returns `4`;
- requested capability is identified;
- no silent fallback occurs;
- machine and human meaning agree;
- absent unrequested optional capability is irrelevant.

### Environmental resolution and interruption
- relative operands resolve once against the initial working directory;
- later working-directory changes do not alter targets;
- UTF-8 process text and byte-oriented product data remain distinct;
- locale does not alter semantics or numeric results;
- undeclared environment variables do not alter behavior;
- support claims are bounded to verified environments;
- caught interruption preserves partial and uncertain effects;
- no rollback implication;
- no portable DX numeric claim for unhandled environment-imposed termination.

## Maturity transition
This specification is Accepted because invocation, request grammar, streams, sink mapping, delivery failure, terminal safety, machine-mode behavior, projections, dry-run adaptation, verbosity, numeric results, environment resolution, interruption, validation, and verification are fully determined within scope. Machine object structure and historical migration classification are separate concerns and are not blockers.

## Authority boundary
This document owns DX public invocation, command and option spelling, process request grammar, standard streams, terminal safety, machine-mode selection and purity, help and version behavior, environmental request resolution, and numeric process results.

`docs/spec/selection.md` owns selected-set semantics and retained selection facts. `docs/spec/operations.md` owns operation meanings, carrier-output completion, effects, conflicts, and semantic result categories. `docs/spec/diagnostics.md` owns diagnostic identifiers, required context, warning and suggestion meaning, and human/machine semantic agreement. `docs/spec/dx-carrier.md` owns carrier representation. `docs/spec/workspace-paths.md` owns workspace mapping and applicability. A separately admitted schema owns machine-enforced structure. Historical compatibility relationships remain unspecified until admitted by a compatibility authority.

Architecture continues to own dependency direction, capability isolation, environmental boundaries, and the rule that presentation and process do not re-evaluate semantics.
