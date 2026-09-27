# DX Compatibility Classifications
Status: Normative
Owner: Historical DX compatibility classifications and migration obligations
Scope: Relationships between evidenced historical behavior and the Accepted current carrier, selection, operation, diagnostic, CLI/process, schema, and workspace contracts
Maturity: Accepted

## Purpose
This specification classifies evidenced historical DX behavior relative to Accepted current semantics. It records historical relationships only. Current behavior remains owned by the cited current specification.

## Classification rules
Each admitted historical behavior has exactly one classification: retain, intentionally replace, migrate, or unspecified. A migration treatment states the complete transition boundary when the classification is migrate. Unspecified establishes no compatibility promise.

## Classifications

### Provisional `dx.py` executable name
- **Observed historical behavior:** The public executable identity is `dx.py`.
- **Classification:** migrate.
- **Migration treatment:** During one compatibility transition, `dx.py` invokes the canonical `dx` process contract and emits a deprecation diagnostic; removal requires a later compatibility change.
- **Owning current specification:** `docs/spec/cli-process.md`.

### Command aliases
- **Observed historical behavior:** Short aliases include `p`, `u`, and `a`, and `apply` aliases extraction behavior.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/cli-process.md`.

### `unpack` workflow
- **Observed historical behavior:** `unpack` extracts carrier entries directly to a destination and is also exposed through `apply`.
- **Classification:** migrate.
- **Migration treatment:** During one compatibility transition, `unpack` maps to `apply` request semantics and emits a deprecation diagnostic; it must not bypass application planning or workspace safety, and removal requires a later compatibility change.
- **Owning current specification:** `docs/spec/cli-process.md`; operation meaning is owned by `docs/spec/operations.md`.

### No-argument `pack --dry-run` behavior
- **Observed historical behavior:** No process arguments are interpreted as `pack --dry-run` for the current directory.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/cli-process.md`.

### Numbered implicit output file
- **Observed historical behavior:** Packing without an explicit output selects the next numbered `dx-carrier-N.dx.txt` filesystem path.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/cli-process.md`.

### Positional `OUTPUT`
- **Observed historical behavior:** `pack` accepts a deprecated positional output operand.
- **Classification:** migrate.
- **Migration treatment:** During one compatibility transition, positional `OUTPUT` is accepted only when `-o` or `--output` is absent, maps to the filesystem sink, and emits a deprecation diagnostic; removal requires a later compatibility change.
- **Owning current specification:** `docs/spec/cli-process.md`.

### Duplicate-command tolerance
- **Observed historical behavior:** A duplicated command token matching the selected command is ignored with a warning.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/cli-process.md`.

### Standard-input `-` convention
- **Observed historical behavior:** A carrier operand of `-` reads carrier bytes from standard input.
- **Classification:** retain.
- **Owning current specification:** `docs/spec/cli-process.md`.

### `--json` versus `--machine`
- **Observed historical behavior:** `--json` selects structured output for admitted dry-run or inspection forms.
- **Classification:** migrate.
- **Migration treatment:** During one compatibility transition, `--json` is accepted as a deprecated alias for `--machine` only on invocations eligible for machine mode and emits a deprecation diagnostic; no historical JSON object shape is retained, and removal requires a later compatibility change.
- **Owning current specification:** `docs/spec/cli-process.md`; machine-structure governance is owned by `docs/schema/README.md`.

### Historical numeric process values
- **Observed historical behavior:** Historical values include `2` usage, `3` invalid carrier, `4` I/O, `5` write conflict, `6` verification failure, and `7` empty selection, with comparison also using `1` for differences.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/cli-process.md`.

### Exception-class machine error codes
- **Observed historical behavior:** Machine errors use implementation class names such as `EmptySelectionError` as codes.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/diagnostics.md`; process presentation is owned by `docs/spec/cli-process.md`.

### Automatic `.dxignore` activation
- **Observed historical behavior:** A root `.dxignore` file is activated automatically when present.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/selection.md`.

### Implicit Git-ignore behavior
- **Observed historical behavior:** Git-ignore evaluation is active by default when a Git repository is available unless disabled.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/selection.md`.

### Implicit default exclusions
- **Observed historical behavior:** A built-in default exclusion set is active unless disabled.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/selection.md`.

### Hidden output exclusion
- **Observed historical behavior:** A selected filesystem output path is silently excluded from packing candidates.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/selection.md`; output self-reference is owned by `docs/spec/operations.md`.

### Binary skip or fail behavior
- **Observed historical behavior:** Binary classification can include, skip, or fail selected content according to a packing policy.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/operations.md`.

### Default existing-target skip
- **Observed historical behavior:** Application defaults to skipping existing targets when no explicit existing-target policy is supplied.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/operations.md`; policy spelling is owned by `docs/spec/cli-process.md`.

### Unconditional read-only skip
- **Observed historical behavior:** Application silently skips every read-only entry without evaluating whether its target is satisfied or discrepant.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/operations.md`; explanation is owned by `docs/spec/diagnostics.md`.

### Historical comparison letters
- **Observed historical behavior:** Comparison presents letter statuses such as `A`, `M`, and `D` as its public difference vocabulary.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/operations.md`; diagnostic interpretation is owned by `docs/spec/diagnostics.md`.

### Structural verification described as integrity
- **Observed historical behavior:** Verification language can imply a broader integrity claim despite the absence of trusted expected content hashes.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/dx-carrier.md`, `docs/spec/operations.md`, and `docs/spec/diagnostics.md` within their respective scopes.

### Symlink-following behavior
- **Observed historical behavior:** Historical comparison or application behavior may follow destination or ancestor symlinks, including links resolving within the workspace.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/workspace-paths.md`.

### Partial writes without complete retained evidence
- **Observed historical behavior:** Mutation may leave partial writes without complete retained classification of completed, failed, untouched, and uncertain effects.
- **Classification:** intentionally replace.
- **Owning current specification:** `docs/spec/operations.md`; reconstruction diagnostics are owned by `docs/spec/diagnostics.md`.

### DX v1.3.1 input
- **Observed historical behavior:** The historical parser accepts carriers declaring DX v1.3.1.
- **Classification:** unspecified.
- **Owning current specification:** `docs/spec/dx-carrier.md`.

## Required verification
Verification must demonstrate that every admitted historical behavior has exactly one classification, every migrate classification has the stated transition boundary, every entry names its current semantic owner, and no entry is interpreted as redefining current semantics.

## Authority boundary
This document owns only historical compatibility classifications and migration obligations. Accepted domain specifications own current semantics. Schema and fixture governance must not classify compatibility independently.
