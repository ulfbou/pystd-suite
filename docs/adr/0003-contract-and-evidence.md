# ADR 0003: Contract and evidence ownership

## Status

Accepted for initial development.

## Context

Vision, architecture, examples, tests, and implementation can drift when several artifacts appear to own the same behavior.

## Decision

Shared public behavior is owned by `docs/spec/COMMON.md`; command-specific behavior is owned by one command specification. Schemas define structured shapes. Golden fixtures provide representative byte-exact evidence. Tests verify the contract but do not silently redefine it.

## Consequences

Behavioral changes update the owning specification and relevant evidence together. Contradictions are defects to resolve, not precedence choices delegated to implementers.
