# Quality strategy

## Verification layers

### Unit tests

Verify domain rules, parsers, state transitions, serializers, policies, and boundary value behavior without unnecessary process coupling.

### CLI integration tests

Invoke `python -m pystd` and verify exit status, stdout bytes, stderr bytes, filesystem effects, and persistent state.

### Golden fixtures

Use byte-exact fixtures for representative public behavior. Specifications define rules; fixtures demonstrate selected cases.

### Fault-oriented tests

Inject controlled failures at meaningful effect boundaries to verify cleanup, rollback, partial-result policy, and diagnostics.

### Compatibility checks

Exercise supported Python and operating-system environments only for behavior actually claimed. Separate portable guarantees from platform enhancements.

## Quality gates

Each material capability should establish:

- functional correctness;
- pipeline and redirection behavior;
- invalid-input and operational-failure behavior;
- encoding and record-boundary behavior where relevant;
- bounded resource behavior where promised;
- platform assumptions;
- automated evidence;
- updated public documentation.

## Non-regression

Regression is a semantic loss or weakening of established behavior, scope, safety, verification, or architectural obligation. Structural movement or rewriting is acceptable when the established meaning is preserved or strengthened.
