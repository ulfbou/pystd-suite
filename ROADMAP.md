# pystd-suite Roadmap

Status: Planning
Owner: Project sequencing, readiness gates, and evidence required to advance
Scope: Ordered outcomes from completed DX specification foundations to prototype release readiness

## Purpose

This roadmap sequences committed repository outcomes without redefining product behavior, architecture, compatibility, schema governance, fixture governance, contributor policy, security policy, or release procedure. Advancement is evidence-driven. Dates, durations, percentages, staffing, issue identifiers, milestones, package layout, module layout, and speculative implementation structure are intentionally absent.

## Current phase

The DX specification phase is complete. Product vision, architecture, foundational ADRs, specification governance, carrier, workspace-path, selection, operation, diagnostic, CLI/process, and compatibility authorities are established. Machine-schema governance and fixture governance are established without inventing artifacts whose public structure is not yet decidable.

The pre-implementation authority set is complete. `CONTRIBUTING.md` owns contributor mechanics and evidence gates, `SECURITY.md` owns security reporting and expectations, `RELEASE.md` owns release eligibility and evidence, and `README.md` is the public repository entry point. Implementation architecture realization is the current phase. This roadmap owns sequencing only.

## Completed foundations

The following foundations are complete for continued work:

- product identity, prototype boundary, principles, and non-goals;
- semantic-core and explicit-boundary architecture;
- plan-mediated mutation and separate write capabilities;
- carrier and workspace-path separation;
- optional explicit Git capabilities;
- specification governance and one-owner-per-rule discipline;
- Accepted DX v2.0.0 carrier semantics;
- Accepted workspace mapping and filesystem safety semantics;
- Accepted packing-selection semantics;
- Accepted operation, diagnostic, and CLI/process semantics;
- Accepted historical compatibility classifications and migration obligations;
- machine-schema admission and evolution governance;
- fixture representation and evidence governance;
- contributor and security governance;
- release-policy authority;
- public repository entry point.

These foundations constrain later work. Later artifacts MUST consume them by reference and MUST NOT replace them with implementation behavior.

## Committed ordered outcomes

### 1. Realize the implementation architecture

Design and implement internal boundaries that realize the Accepted architecture without treating historical `dx.py`, `dxlib`, package layout, or module layout as the target plan.

**Dependency:** the public authorities remain fixed inputs. Internal structure is selected to preserve semantic independence, explicit environmental facts, separate capabilities, and plan-mediated mutation.

**Evidence to advance:** dependency-boundary tests, read/write capability isolation, operation composition tests, and demonstrable ability to exercise semantic components independently of CLI and presentation.

### 2. Build conformance fixtures and tests

Create real fixture families and tests from Accepted specifications. Keep conformance, regression, compatibility characterization, architecture, security, and environment-support evidence distinguishable.

**Dependency:** implementation boundaries must be stable enough to test without making implementation layout normative.

**Evidence to advance:** required verification coverage for carrier, workspace, selection, operations, diagnostics, CLI/process, compatibility transitions, and security-sensitive boundaries; exact-byte and deterministic evidence where claimed; no placeholders.

### 3. Implement Accepted semantics

Implement the complete initial DX behavior against the Accepted semantic authorities, using tests and fixtures as verification evidence rather than alternative authority.

**Dependency:** architecture realization and an executable conformance harness must exist.

**Evidence to advance:** conformance across every accepted operation and important negative boundary; preview/execution agreement; no hidden mutation; exact-byte preservation; deterministic results from declared inputs; bounded partial-failure evidence.

### 4. Decide machine encoding and concrete schema when consumers make it decidable

Select a machine serialization encoding and admit a concrete schema only when implementation producers, automation consumers or validators, and interoperable required structure make the decision concrete.

**Dependency:** semantic result production and actual machine consumers must exist. Prose semantics must remain stable and complete.

**Evidence to advance:** accepted encoding decision, complete public structure, standards-based schema validation, positive and negative fixtures, semantic agreement checks, evolution rules, and absence of internal plans or implementation-private types.

### 5. Establish packaging and executable exposure

Provide installable artifacts and expose the canonical `dx` invocation without allowing packaging mechanics to redefine semantics or architecture.

**Dependency:** core conformance and process-boundary behavior must be verified, and any machine contract used by packaging or automation must be accepted.

**Evidence to advance:** reproducible build and install verification, canonical executable behavior, version reporting, artifact-content inspection, dependency review, and supported-environment installation evidence.

### 6. Verify compatibility transitions

Exercise every retained, intentionally replaced, migrated, and unspecified historical relationship against the implemented process and semantic contracts.

**Dependency:** canonical invocation, packaging, commands, diagnostics, process results, selection behavior, application behavior, and carrier processing must be testable through their public boundaries.

**Evidence to advance:** transition-boundary tests for migrated behavior, explicit verification of intentional replacements, retained-behavior conformance, and no accidental compatibility claim for unspecified behavior.

### 7. Expand supported environments only with evidence

Add platform, filesystem, Python, terminal, permission, case, Unicode, Git, or packaging support only after the applicable conformance and safety evidence exists.

**Dependency:** the conformance suite and environment-fact model must be capable of distinguishing semantic defects from unsupported environments.

**Evidence to advance:** reproducible environment-specific carrier, path, link, collision, permission, stream, process, packaging, and external-capability results. Design portability alone is insufficient.

### 8. Establish prototype release readiness and release evidence

Evaluate the complete prototype against release policy and produce the evidence required for an honest release decision.

**Dependency:** all preceding committed outcomes required by the release boundary are complete.

**Evidence to advance:** passing conformance, architecture, security, compatibility, schema when admitted, packaging, installation, and supported-environment checks; verified artifacts; documented limitations; synchronized public documentation; no unresolved release blocker.

## Dependency model

The governing progression is:

```text
Accepted product, architecture, and semantics
→ completed repository governance, release policy, and public entry point
→ architecture realization
→ conformance evidence
→ semantic implementation
→ decidable machine structure
→ packaging and canonical exposure
→ compatibility-transition verification
→ evidence-backed environment expansion
→ prototype release readiness
```

Work MAY overlap when it does not bypass a readiness gate or create a lower-level authority before its dependencies are decidable. No implementation artifact, fixture, schema, package, or README claim may advance by silently filling an unresolved upstream decision.

## Readiness rules

An outcome is ready to advance only when:

- its owning authority exists and has no blocking unresolved decision within scope;
- required upstream authorities are Accepted or otherwise complete for the dependency;
- applicable security and compatibility review has occurred;
- required evidence is reproducible from declared inputs and environments;
- lower-level artifacts do not redefine higher-level authority;
- support, readiness, and conformance claims do not exceed evidence;
- placeholders and speculative public structures are absent;
- unrelated cleanup is excluded.

A failed gate returns work to the owning outcome. It does not authorize silent fallback, reduced semantics, or a broader claim with weaker evidence.

## Explicit non-goals

This roadmap does not commit:

- the historical familiar-utility catalog;
- a `pystd` umbrella CLI;
- preservation of every historical option or behavior;
- a plugin ecosystem, hosted service, network protocol, or remote registry;
- a generic CLI framework or speculative provider architecture;
- a machine schema before encoding and consumers make it decidable;
- package, module, class, function, or repository layout;
- a particular CI, hosting, issue, or release vendor;
- signing, attestations, rollback, production operations, or unrestricted cross-platform support;
- optimization before reference-conformant correctness;
- any second pystd-suite product.

## Possible future work

Possible future work is not committed. It may be admitted only through applicable product, architecture, specification, security, compatibility, and evidence review. Examples include additional supported environments, future carrier-format evolution, a trusted integrity mechanism, new machine consumers, performance optimization after reference equivalence, or a future non-DX product that satisfies the product-admission principles.

Listing possible work creates no compatibility promise, release commitment, priority, schedule, or implementation authority.

## Authority boundary

This document owns project sequencing, dependency relationships, readiness gates, and evidence required to move between committed outcomes. Accepted specifications own observable behavior. Architecture owns dependency and capability boundaries. Compatibility authority owns historical relationships. `CONTRIBUTING.md` owns contributor mechanics, `SECURITY.md` owns security expectations, and `RELEASE.md` owns release eligibility, evidence, artifact verification, and release records.
