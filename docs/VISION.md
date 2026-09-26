# pystd-suite Vision

Status: Normative
Owner: Product definition
Scope: pystd-suite project identity and the accepted boundary of the initial DX product

## Purpose

pystd-suite is an enduring learning and software-engineering project. It uses trustworthy command-line products to develop practical Python engineering capability and junior software-architecture judgment through complete, evidence-backed product work.

Delivery automation, security engineering, user and compatibility validation, and version-control and release discipline support both learning tracks. These learning goals explain why the project exists; they are not user-facing DX capabilities.

## Learning purpose

pystd-suite provides a substantive setting in which to learn how to:

- turn a product problem into an explicit boundary;
- distinguish requirements from implementation choices;
- define and verify observable behavior;
- reason about compatibility, portability, determinism, and safety;
- develop maintainable Python software;
- automate verification, package artifacts, and make evidence-backed release claims;
- evolve decisions from implementation and user evidence without allowing experiments to become accidental contracts.

The learning outcome is demonstrated through the quality and coherence of the product lifecycle, not through a required number of commands or features.

## Product identity

pystd-suite is the continuing project within which products may be designed, developed, verified, and released. It is not defined by the historical familiar-utility catalog and does not promise a fixed collection of utility commands.

DX is the complete initial product and prototype. This initial boundary does not make pystd-suite permanently synonymous with DX. No second product is currently promised.

## Initial product: DX

DX concerns reliable processing of DX carriers and their controlled relationship with repository workspaces.

The product enables workspace content to be selected intentionally, represented in a carrier, preserved according to an explicit contract, inspected and structurally verified before action, compared with a workspace where applicable, previewed before mutation, and explicitly applied.

DX also provides meaningful human diagnostics and machine-readable outcomes where automation interfaces are deliberately exposed. It must avoid hidden writes, unsafe path behavior, silent conflicts, misleading success, accidental environmental behavior, and unsupported compatibility claims.

DX is the product and domain name. `dx.py` is a provisional executable identity retained for continuity. This does not require the product to remain one Python file, require a final executable named `dx.py`, determine the package name, or establish a `pystd` umbrella CLI.

## Problem

Exchanging workspace state is unreliable when the transported content, selection rules, preservation behavior, destination effects, or failure outcomes are unclear. Acting on an opaque carrier can modify the wrong paths, lose meaningful bytes, conceal conflicts, or create automation that depends on accidental behavior.

DX addresses this problem by establishing a product boundary in which:

- the content intended for transport can be selected deliberately;
- the carrier can preserve supported text, binary content, paths, and declared properties;
- people and automation can inspect and verify the carrier before relying on it;
- intended workspace effects can be reviewed before mutation;
- mutation occurs only through an explicit operation;
- relevant decisions, exclusions, conflicts, and failures are visible;
- compatibility and platform support are claimed only when supported by evidence.

The exact carrier grammar, selection semantics, operation behavior, CLI contract, and filesystem rules belong to later authorities.

## Users and automation consumers

### Project author and learner

The project author uses DX as the substantive product through which Python engineering and software-architecture judgment are developed. The author needs product behavior, design decisions, verification evidence, packaging, and release claims to remain coherent and explainable.

### Developer or repository maintainer

A developer or repository maintainer uses DX to exchange workspace content. This user needs transport to be inspectable, preservation to be explicit, destination effects to be previewable, application to be controlled, and conflicts or rejected content to be visible.

### Automation consumer

An automation consumer invokes accepted DX operations through process or machine-readable contracts. It needs declared outcomes and must not depend on informal terminal prose, accidental output structure, or hidden environmental behavior.

No additional market persona or organizational role is part of the initial product definition.

## Product principles

### Standard-library-first

The Python standard library is the default runtime foundation. A third-party runtime dependency requires explicit, need-based justification showing that the standard-library solution would materially compromise an accepted concern such as correctness, interoperability, security, portability, or maintainability.

Development, testing, analysis, build, and release tooling is not required to be standard-library-only, but each tool must have a defined responsibility.

The word "suite" allows related tooling to enter the project through future product decisions. It does not promise multiple shipped products in the initial prototype and does not preserve the historical familiar-utility interpretation.

### Compatibility-informed redesign

Current DX behavior is evidence. Useful established behavior is not broken casually, but accidental implementation behavior is not preserved automatically. Future behavior is selected deliberately.

Compatibility claims require representative evidence. Deliberate incompatibilities must be visible, and migration treatment is required when an accepted change would otherwise harm established usage.

Compatibility investigation covers carrier format, CLI behavior, process outcomes, machine-readable output, selection semantics, filesystem and application behavior, and legacy DX. Detailed decisions to retain, intentionally replace, migrate, or leave behavior unspecified belong to later compatibility and behavioral authorities.

### Portable by design; supported where verified

Carrier paths are platform-neutral representations of workspace-relative locations. A carrier does not depend on the originating machine's absolute workspace location.

Platform differences that affect observable results must not be hidden. Support claims require verification evidence. Exact case, Unicode, symlink, permission, replacement, and Git behavior is defined by later authorities rather than assumed here.

### Semantic determinism

For identical declared inputs and resolved environmental semantics, DX must produce semantically equivalent outcomes.

Environmental state that affects a result must be eliminated, declared, resolved into explicit operation input, or reported honestly. Byte-identical carrier generation is not promised unless a later carrier specification establishes a canonical serialization contract that supports that guarantee.

### Inspect and preview before mutation

Workspace mutation follows this product invariant:

```text
inspect/verify
→ plan/preview
→ explicit application
```

Carrier creation follows:

```text
select/preview
→ explicit carrier creation
```

Read operations do not mutate carriers, workspaces, or configuration. Planning exposes intended effects without applying them. Mutation requires explicit invocation, and validation that can occur before mutation must occur before mutation.

Conflicts, unsafe paths, symlinks, read-only entries, overwrite consequences, rejected content, and partial failure require explicit treatment in later specifications. This vision does not prescribe atomic-write, rollback, transaction, or staging mechanisms.

## Initial prototype boundary

### Included capabilities

The initial DX prototype includes, at product level:

- DX v2 carrier parsing;
- DX v2 carrier serialization;
- carrier inspection;
- carrier structural verification;
- workspace-to-carrier packing;
- deterministic selection necessary for packing;
- carrier-to-workspace planning;
- explicit application;
- comparison;
- read-only declarations;
- text and binary preservation;
- dry-run or preview behavior;
- human-readable diagnostics;
- machine-readable outcomes where accepted automation interfaces exist;
- compatibility characterization;
- safety verification;
- automated conformance evidence.

Prototype completion is evidence-based. It requires coherent specified behavior, verification of the accepted capabilities, honest compatibility and portability boundaries, installable artifacts, automated test execution, release evidence, and documented limitations. It is not measured by command count.

### Explicit non-goals

The initial prototype does not include or promise:

- the historical 32-command utility catalog;
- familiar-utility cloning;
- POSIX, GNU, or BSD compatibility by implication;
- a `pystd` umbrella CLI;
- a generic CLI framework;
- pathsel reimplementation or its expression phases, Mode A or Mode B, identity machinery, or exit-code allocation;
- speculative provider or policy frameworks;
- schemas without real consumers and validators;
- a plugin ecosystem;
- hosted services;
- networking or remote carrier registries;
- production deployment infrastructure;
- high availability;
- production monitoring;
- automated rollback;
- formal supply-chain attestations;
- artifact signing;
- unrestricted cross-platform guarantees;
- speculative caching or identity infrastructure;
- optimization before correctness;
- blanket preservation of every existing `dx.py` option or behavior.

A non-goal is outside the accepted initial prototype. It is not a permanent prohibition. Later inclusion requires a separate, evidence-backed decision.

## Relationship to ulfbou/collab

ulfbou/collab is a source of existing DX implementation evidence, observed behavior, candidate compatibility requirements, and useful implementation lessons.

pystd-suite owns the future redesigned DX product. The redesign is not a mechanical refactoring of the existing `dx.py`, and the existing implementation structure is not architectural authority.

Redesign also does not authorize casual breakage of valid carriers, useful established workflows, automation contracts, or safety expectations. Such changes require evidence and explicit compatibility decisions.

## Future evolution

Future evolution is capability- and evidence-driven rather than catalog-driven.

A future non-DX product may enter pystd-suite only when:

- its user problem is explicit;
- it provides meaningful product or learning value;
- it has a coherent product boundary;
- it is not introduced merely to justify the word "suite";
- claimed reuse is demonstrated rather than predicted;
- it does not force speculative abstractions into DX.

Reusable capabilities are extracted only after genuine reuse is demonstrated or the capability has an independently valuable boundary.

## Authority boundary

This document is the sole authority for pystd-suite product identity and the accepted boundary of the initial DX product.

It does not own system or component architecture, dependency direction, package or module structure, carrier grammar, selection semantics, exact operation behavior, CLI commands or flags, streams, numeric exit codes, machine-output fields, filesystem algorithms, Git integration architecture, workflow policy, release procedure, roadmap sequencing, or implementation plans.

Those concerns belong to later architecture, decision-record, specification, workflow, release, and planning authorities admitted by the documentation system. Until those authorities are drafted and accepted, this document establishes their product constraints but does not pre-decide their detailed content.
