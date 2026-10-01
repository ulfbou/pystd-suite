# Architecture

## Architectural style

The product is a multicall Python application with an explicit composition root and one-way dependencies.

```text
__main__ -> cli -> commands -> shared services -> standard library
```

## Responsibilities

### Entry point

Adapts the application result to process termination. It contains no command behavior.

### CLI composition

Owns command registration, parser construction, shared options, context creation, and process-level error translation.

### Commands

Own command-specific parsing, validation, orchestration, and output construction. Commands must not terminate the interpreter directly or invoke sibling commands through a shell.

### Domain logic

Where complexity warrants it, domain functions operate independently of global process state and concrete terminal presentation.

### Shared services

Cross-cutting policies may cover streams, diagnostics, terminal capabilities, paths, atomic replacement, subprocess lifecycle, serialization, and time. A shared service is introduced only after a real vertical slice demonstrates the need.

## Core invariants

- stdout contains requested data, not progress or diagnostics.
- Machine-readable output is deterministic within its documented contract.
- Destructive behavior requires explicit intent.
- Untrusted paths are validated before effects.
- Caller-owned streams are not closed by command logic.
- Expected operational failures map to stable classifications and statuses.
- Subprocesses use argument vectors rather than shell interpretation.
- State-changing workflows define validation, staging, commit, cleanup, and recovery behavior where applicable.

## Dependency rules

- Shared services do not import command modules.
- Command modules do not perform work at import time.
- Public behavior is not owned by architecture or development guidance.
- Platform-specific facilities are isolated behind explicit policy or adapter boundaries when tests require control.

## Evolution rule

Start with a complete vertical slice. Generalize only after repeated or cross-cutting responsibility is demonstrated. Record decisions whose consequences extend beyond the implementing module.
