# pystd-suite

pystd-suite is an enduring learning and software-engineering project for building trustworthy command-line products through complete, evidence-backed product work. DX is its complete initial product and prototype.

## DX

DX addresses unreliable exchange of repository workspace state. Its Accepted specifications define how workspace content is selected intentionally, represented in a DX v2.0.0 carrier, preserved as exact supported bytes, inspected and structurally verified, compared with an explicit workspace, previewed before mutation, and explicitly applied with visible conflicts and outcomes.

The redesigned DX product is specified, but its target implementation is not yet complete or released. This repository does not currently claim an installable package, an available canonical `dx` executable, or prototype release readiness. Historical `dx.py` and `dxlib` content is implementation and compatibility evidence, not the target product architecture.

## Current status

The pre-implementation authority set is established:

- product vision and architecture;
- Accepted carrier, workspace-path, selection, operation, diagnostic, CLI/process, and compatibility specifications;
- machine-schema and fixture governance;
- contributor, security, roadmap, and release policies.

The next phase is implementation architecture realization. Conformance fixtures, tests, implementation, machine encoding when consumers make it decidable, packaging, compatibility-transition verification, supported-environment expansion, and prototype release evidence follow the gates in `ROADMAP.md` and `RELEASE.md`.

## Specified capabilities

The Accepted DX contract covers:

- DX v2.0.0 carrier parsing, validation, deterministic serialization, text and binary preservation, read-only declarations, and structural verification;
- explicit workspace-root mapping, containment, link and special-object safety, collision handling, and changed-precondition detection;
- deterministic packing selection from explicit candidate, scope, selector, exclusion, ignore, override, and optional Git facts;
- carrier creation, inspection, structural verification, workspace comparison, application planning, explicit application, no-op behavior, and partial-failure evidence;
- human and machine diagnostic agreement;
- the canonical `dx` process contract, command set, streams, terminal safety, machine mode, and numeric process results;
- classified historical relationships and defined migration obligations.

These are specification commitments for the redesigned product. They are not claims that the current repository implementation already conforms.

## Documentation

- `docs/VISION.md`: project identity, initial DX product, principles, scope, and non-goals.
- `docs/ARCHITECTURE.md`: dependency, capability, environmental, and mutation boundaries.
- `docs/adr/`: consequential architecture decisions and rationale.
- `docs/spec/README.md`: specification governance and domain ownership.
- `docs/spec/dx-carrier.md`: DX v2.0.0 carrier and preservation semantics.
- `docs/spec/workspace-paths.md`: workspace mapping and filesystem safety.
- `docs/spec/selection.md`: packing selection semantics.
- `docs/spec/operations.md`: creation, inspection, verification, comparison, and application semantics.
- `docs/spec/diagnostics.md`: diagnostic meaning and human/machine agreement.
- `docs/spec/cli-process.md`: public invocation, streams, machine mode, and process results.
- `docs/spec/compatibility.md`: historical classifications and migration obligations.
- `docs/schema/README.md`: machine-schema governance. No concrete machine schema is active.
- `tests/fixtures/README.md`: fixture representation and evidence governance.
- `CONTRIBUTING.md`: contribution workflow, evidence, and acceptance gates.
- `SECURITY.md`: private reporting route and security expectations.
- `RELEASE.md`: release eligibility, evidence, artifact verification, and release records.
- `ROADMAP.md`: ordered outcomes and readiness gates.

## Contributing

Start with `CONTRIBUTING.md`. Observable changes are specification-first, focused, compatibility-reviewed where triggered, and accepted only with applicable deterministic, safety, exact-byte, architecture, fixture, test, and environment evidence.

## Security

Use the repository's available private security-reporting mechanism for suspected vulnerabilities. Do not disclose a security issue publicly before remediation when premature disclosure could increase risk. See `SECURITY.md` for scope, safe reproduction, evidence handling, and current support limits.

## Support and portability

DX is designed for portability, but support is claimed only where conformance evidence exists. The current specification evidence boundary is Linux, Python 3.12, and overlayfs for the stated carrier and workspace contracts. Windows, macOS, other filesystems, other Python versions, and broader terminal or packaging environments remain unverified.

No cryptographic authenticity, signing, attestation, whole-workspace transaction, rollback, crash-recovery, or unrestricted cross-platform guarantee is claimed.

## Compatibility

Historical behavior is retained, intentionally replaced, migrated, or left unspecified only as classified in `docs/spec/compatibility.md`. Current semantics remain in the owning domain specifications. Historical `dx.py` behavior does not silently define the redesigned product.

## Development state

Use the Accepted authorities as the source for design and conformance work. Do not infer current availability from provisional or historical implementation files. Release and support claims require the complete evidence defined by `RELEASE.md`; sequencing and readiness belong to `ROADMAP.md`.
