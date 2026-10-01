# ADR 0002: Standard-library runtime

## Status

Accepted for initial development.

## Context

The project exists partly to develop direct understanding of Python systems facilities while producing a coherent tool suite.

## Decision

Product runtime code uses Python and the Python standard library. Any exception requires a later explicit architectural decision.

## Consequences

The product gains a small runtime dependency surface and exposes the author to the underlying APIs. The constraint must not be used to invent unsafe security mechanisms, misrepresent portability, or reject appropriate development-time verification tools without evaluation.
