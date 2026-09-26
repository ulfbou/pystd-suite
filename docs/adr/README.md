# Architectural Decision Records

Status: Policy
Owner: Architectural decision-record governance
Scope: ADR admission, status, lifecycle, indexing, and relationship to architecture and specifications

## Purpose

Architectural decision records preserve the context, choice, credible alternatives, consequences, verification impact, and supersession conditions for consequential architectural decisions.

An ADR records why a decision was made. Continuing architecture is integrated into `docs/ARCHITECTURE.md`; observable product behavior belongs to specifications.

## Admission criteria

Create an ADR only when:

- credible alternatives exist;
- the choice constrains substantial future design;
- reversing it would have meaningful consequences;
- future readers need the rationale and supersession conditions.

Do not create an ADR merely to restate `docs/VISION.md`, record a routine implementation detail, reserve a possible extension, or define product behavior.

## Statuses

- **Proposed:** Under review and not authoritative.
- **Accepted:** The decision governs architecture and its continuing consequences are reflected in `docs/ARCHITECTURE.md`.
- **Superseded:** Replaced by a later accepted ADR. The record remains historical.
- **Rejected:** Considered and not adopted. It has no architectural authority.

An ADR has one current status. Superseded records identify the replacing ADR. The replacing ADR identifies the records it supersedes.

## Naming and numbering

ADR filenames use a four-digit sequence and a concise lowercase hyphenated title:

```text
NNNN-concise-decision-title.md
```

Numbers are never reused. The sequence records repository order, not precedence.

## Required content

Every ADR follows `TEMPLATE.md` and includes:

- metadata for status, owner, and scope;
- context;
- decision;
- alternatives considered;
- consequences;
- verification impact;
- supersession conditions;
- affected authorities.

The decision must be explicit. Alternatives must be credible. Consequences include costs as well as benefits.

## Acceptance

An ADR becomes Accepted only when:

- the decision is within architectural authority;
- affected product authority remains satisfied;
- affected architectural consequences are integrated into `docs/ARCHITECTURE.md`;
- behavior deferred to specifications is not silently defined by the ADR;
- verification responsibility is identified.

Repository workflow will later define review and change mechanics. This policy defines the decision-record requirements.

## Supersession

Supersede an ADR when a new accepted decision changes or replaces it. Do not rewrite an accepted ADR to make history appear consistent with the new choice.

A superseding ADR must:

- identify the superseded record;
- state the evidence requiring change;
- describe migration or compatibility consequences where relevant;
- update `docs/ARCHITECTURE.md` and other affected authorities.

## Relationship to other authorities

- `docs/VISION.md` owns product identity and scope.
- `docs/ARCHITECTURE.md` owns the current integrated architecture.
- ADRs own the historical record and rationale for consequential architecture decisions.
- Specifications own observable product behavior.
- Planning documents sequence accepted work but do not create architecture.

If an ADR conflicts with current integrated architecture without an explicit supersession, the repository contains an authority defect that must be corrected. An ADR never overrides product authority or a behavioral specification outside its scope.

## Index

| ADR | Title | Status |
|---|---|---|
| 0001 | Semantic core and explicit boundary dependency model | Accepted |
| 0002 | Plan-mediated explicit mutation | Accepted |
| 0003 | Carrier and workspace path separation | Accepted |
| 0004 | Git as optional explicit external capabilities | Accepted |
