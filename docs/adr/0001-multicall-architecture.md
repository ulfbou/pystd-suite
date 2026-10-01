# ADR 0001: Multicall architecture

## Status

Accepted for initial development.

## Context

The planned utilities need consistent invocation, diagnostics, stream policy, status handling, and shared safety behavior without becoming unrelated scripts.

## Decision

Provide one `pystd` application with explicitly registered subcommands and an equivalent `python -m pystd` entry point.

## Consequences

The CLI layer becomes the composition root. Commands can share deliberate policies while retaining focused ownership. Independent executable aliases may be considered later, but they must not become a second behavioral architecture.
