# pystd-suite

`pystd-suite` is a cohesive suite of production-minded command-line utilities built with the Python standard library.

## Purpose

The project has two inseparable purposes:

1. build a useful, coherent, and dependable Python command-line product; and
2. provide its author with a sustained learn-by-doing path from Python development toward junior software architecture.

Python engineering and architectural responsibility progress together. Each real product increment moves from observable behavior through implementation, verification, boundary design, and architectural review. The repository is not a workshop, public curriculum, or imitation of mature operating-system tools feature for feature.

## Product direction

The product is a multicall command:

```text
pystd COMMAND [arguments]
python -m pystd COMMAND [arguments]
```

Commands share consistent conventions for streams, diagnostics, exit statuses, safety, deterministic behavior, and machine-readable results. Individual commands remain focused and independently specified.

## Principles

- Standard-library runtime dependencies only.
- Requested data belongs on stdout; diagnostics belong on stderr.
- Non-destructive defaults and explicit mutation boundaries.
- Deterministic ordering wherever the contract permits it.
- Expected failures do not produce uncontrolled tracebacks.
- Public behavior is specified and mechanically verifiable.
- Architecture grows from demonstrated product needs, not speculative abstraction.
- Platform-specific behavior is explicit rather than disguised as portable behavior.

## Initial scope

The planned suite develops through vertical slices across:

- streams and text processing;
- filesystems and storage;
- structured data and archives;
- processes, concurrency, and signals;
- networking and protocols;
- persistence and integrated applications.

The command inventory and sequencing are planning inputs, not a promise that every command must be implemented before the product becomes useful.

## Documentation

- [Vision](docs/VISION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Roadmap](docs/ROADMAP.md)
- [Quality strategy](docs/QUALITY.md)
- [Common behavioral contract](docs/spec/COMMON.md)
- [Architecture decisions](docs/adr/README.md)
- [Contributing](CONTRIBUTING.md)

## Current phase

The repository is in pre-development. Initial work establishes the smallest executable vertical slice and the contracts needed to evolve it safely.
