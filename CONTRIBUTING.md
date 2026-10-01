# Contributing

## Working model

Changes should advance the product through a narrow vertical slice: define observable behavior, implement it, verify normal and adverse cases, then evaluate architectural consequences.

## Change sequence

1. Identify the user-visible outcome and affected contract.
2. Implement the smallest complete behavior.
3. Keep domain logic separate from process and I/O adaptation where that separation is useful.
4. Add deterministic unit and subprocess-level tests.
5. Verify error, interruption, encoding, and platform boundaries that apply.
6. Update the owning specification in the same change.
7. Record an ADR only when the decision has lasting architectural significance.

## Runtime constraint

Runtime code uses Python and the Python standard library. Development tooling may be evaluated separately, but it must not become an undeclared runtime dependency.

## Public behavior

A change to arguments, streams, output, diagnostics, exit status, ordering, side effects, persistence, or compatibility is a contract change. Examples alone do not define behavior.

## Review expectations

Review should ask:

- Is ownership unambiguous?
- Are invariants and trust boundaries explicit?
- Are mutation and commit points defined?
- Are success, failure, and partial completion mechanically distinguishable?
- Is the abstraction justified by demonstrated use?
- Does the change preserve established behavior unless revision is deliberate?
