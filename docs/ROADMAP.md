# Roadmap

The roadmap develops Python capability and architectural responsibility through the same product increments.

## Phase 0: Foundation slice

Deliver the package entry point, command registry, common process context, diagnostics, exit-status mapping, subprocess test harness, and one small end-to-end command.

Architectural focus: composition root, process boundary, ownership, and error translation.

## Phase 1: Streams and text

Develop commands such as `cut`, `grep`, `wc`, `uniq`, `sort`, and `hexdump` through small slices.

Engineering focus: bytes versus text, incremental decoding, record boundaries, broken pipes, stable ordering, and bounded processing.

## Phase 2: Filesystems and integrity

Develop traversal, search, usage, duplicate detection, safe removal, atomic replacement, and tailing capabilities.

Engineering focus: identity, symlinks, metadata, transaction boundaries, rollback, and partial filesystem failure.

## Phase 3: Structured data and archives

Develop JSON, CSV, configuration, TAR, and ZIP capabilities.

Engineering focus: formal input boundaries, deterministic serialization, schema evolution, archive preflight, and containment.

## Phase 4: Processes and concurrency

Develop argument batching, watching, timeout control, environment handling, repository orchestration, and timing.

Engineering focus: child lifecycle, monotonic deadlines, cancellation, bounded concurrency, deterministic presentation, and aggregate status.

## Phase 5: Networking

Develop HTTP client, local server, socket, and name-resolution capabilities.

Engineering focus: finite timeouts, byte preservation, validation, redaction, safe URL paths, and loopback-only automated tests.

## Phase 6: Persistence and integration

Develop SQLite-backed notes and integrated Markdown and static-site capabilities.

Engineering focus: schemas, migrations, transactions, escaping, staging, publication, and recovery.

## Release progression

A phase is not complete because files exist. Completion requires implemented contracts, normal and adverse verification, compatibility evidence for claimed environments, and no unresolved weakening of established behavior.
