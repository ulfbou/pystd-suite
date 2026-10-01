# Common behavioral contract

This document owns behavior shared across `pystd` commands. Individual command specifications refine it without silently contradicting it.

## Invocation

```text
pystd COMMAND [arguments]
python -m pystd COMMAND [arguments]
```

## Streams

- stdout contains requested command data.
- stderr contains diagnostics, warnings, and explicitly requested operational detail.
- Commands do not assume standard streams are terminals.
- Commands do not close caller-owned streams.
- Text and binary modes are distinguished explicitly where both are meaningful.

## Exit status

Every command documents the statuses it can return. Shared meanings should remain stable. Invalid usage is distinct from malformed input, operational failure, partial completion, timeout, interruption, and internal failure.

## Diagnostics

Diagnostics are concise, actionable, and free from uncontrolled tracebacks for expected failures. Stable classifications may be exposed independently from human-readable wording.

## Determinism

Commands document their ordering guarantee. Concurrency, filesystem enumeration, resolver results, timestamps, and serialization must not introduce accidental nondeterminism into behavior claimed as stable.

## Structured output

Machine-readable modes use documented schemas or versioned structures, contain no terminal decoration, and remain separate from diagnostics. Success, failure, and partial completion must be mechanically distinguishable.

## Interaction

Commands run noninteractively unless interaction is explicitly requested. A command must not unexpectedly prompt when streams are redirected.

## Mutation

Destructive or irreversible effects require explicit intent. Where practical, commands provide preview or dry-run behavior and postconditions that can be checked mechanically.

## Security boundaries

Commands validate untrusted paths, archive members, subprocess arguments, configuration, protocol data, and terminal-bound content at the boundary where each becomes meaningful.

## Resource behavior

Commands document meaningful limits, buffering strategies, timeout behavior, and capture bounds. Unbounded accumulation must not be hidden behind a streaming interface.
