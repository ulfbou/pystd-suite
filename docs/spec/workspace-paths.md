# Workspace Path and Filesystem Boundary

Status: Normative
Owner: Workspace-relative path and filesystem-boundary semantics
Scope: Mapping validated carrier paths to explicit workspace roots, filesystem observation, containment, entry types, links, collisions, and workspace applicability
Maturity: Accepted

## Purpose

This specification defines how validated logical carrier paths relate to an explicit physical workspace. It establishes containment, no-follow observation, entry-type, link, collision, parent, permission, and changed-precondition requirements needed to determine workspace applicability safely.

## Scope

### In scope

This specification governs:

- the explicit workspace root;
- conversion from logical carrier paths to workspace-relative targets;
- lexical and physical containment;
- filesystem observation without following links;
- supported and unsupported entry types;
- final and ancestor symlink treatment;
- directory-versus-file conflicts;
- conditions for missing parent creation;
- case and Unicode mapping collisions;
- permission failures;
- safety-precondition revalidation;
- the distinction between carrier validity and workspace applicability;
- the currently verified environment and portability limitations.

### Out of scope

This specification does not define carrier grammar, source selection, application overwrite policy, operation-wide partial-failure behavior, read-only success semantics, CLI behavior, process results, machine-output fields, or filesystem implementation algorithms.

## Terminology

**Workspace root** means the explicit directory boundary within which a workspace operation observes or plans physical targets.

**Logical path** means a validated platform-neutral carrier path governed by `docs/spec/dx-carrier.md`.

**Mapped target** means the physical workspace location considered for one logical path.

**Applicability** means that the relevant logical paths can be mapped and observed under this specification without a containment, type, link, collision, permission, or unsupported-environment conflict.

**Final component** means the last component of a mapped target. **Ancestor** means any preceding component between the workspace root and final component.

## Workspace context

Every workspace operation MUST receive an explicit workspace root. Semantic path behavior MUST NOT depend on an implicit current working directory.

The workspace context includes the root and the resolved environmental facts needed to interpret mappings. Platform and filesystem behavior affecting applicability must be declared, observed, or reported as unverified or unsupported.

The initial verified environment is:

- Linux;
- Python 3.12;
- overlayfs as the tested filesystem.

The design is portable, but support is claimed only where verified. Windows, macOS, case-insensitive filesystems, Unicode-normalizing filesystems, network filesystems, and other Python versions remain unverified.

## Logical-to-physical mapping

A validated logical carrier path is mapped relative to the explicit workspace root. Mapping does not change the carrier path's text, case, or Unicode representation.

Every mapped target MUST remain lexically and physically within the workspace root.

Containment is evaluated during planning and revalidated before an affected mutation whenever links, parents, destination identity, or other relevant facts may have changed.

A valid carrier may be inapplicable to a particular workspace. Workspace inapplicability does not make the carrier malformed.

## Filesystem observation

Before content access or write planning, every existing relevant path component and final target MUST be observed without following links.

Observation distinguishes at least:

- regular file;
- directory;
- symbolic link, including broken link;
- FIFO;
- socket;
- block device;
- character device;
- unknown or unsupported object.

An implementation MUST NOT open or read an unsupported object merely to classify it.

Required observation failure, including permission denial, is an environmental failure. Planning MUST NOT report an applicable writable target when required observation did not succeed.

## Source workspace links

Source symlinks are not transportable file payloads in the initial prototype.

Packing discovery and explicit-source handling MUST identify symlinks without following them. A symlink target's bytes MUST NOT be transported under the symlink's logical name.

Directory traversal MUST NOT follow symlinked files or directories.

A source symlink resolving outside the source workspace is rejected before target access. The selection outcome belongs to `docs/spec/selection.md`; operation aggregation belongs to `docs/spec/operations.md`; diagnostic interpretation belongs to `docs/spec/diagnostics.md`.

## Destination links

A final destination symlink is an applicability conflict, including when it is broken or resolves within the workspace. Planning and application MUST NOT follow, replace, or write through it.

Any ancestor symlink is an applicability conflict, including an ancestor resolving to another location inside the workspace. This rule protects physical target identity and plan stability from link retargeting.

A target that resolves outside the workspace root is inapplicable and MUST NOT be read or mutated.

Comparison MUST NOT follow final or ancestor symlinks. `docs/spec/operations.md` owns the precise comparison result.

A final carrier-output destination symlink is rejected. Detailed carrier-output planning and conflict behavior belongs to `docs/spec/operations.md`.

## Supported entry types

Regular files are the supported workspace payload targets.

Directories are supported only as workspace containers. A directory at a location where a regular file is intended is a planning conflict. Preview MUST NOT report that target as writable.

FIFO, socket, block device, character device, and unknown special objects are unsupported as transported payload sources and regular-file targets. They MUST be identified without content access and reported as explicit unsupported-entry or applicability outcomes by the owning operation.

## Parent directories

Missing parent directories MAY be included in planned workspace effects when all the following are true:

- every parent remains within the workspace root;
- no existing parent is a symlink or unsupported entry type;
- no path collision prevents directory creation;
- the owning operation explicitly includes parent creation.

Preview must expose required parent creation through the owning operation's result. This specification does not define that result's presentation.

## Case and Unicode mapping

Carrier-path identity remains case-sensitive and Unicode-preserving.

If distinct logical paths map to the same destination identity under the resolved filesystem's case behavior, the carrier is inapplicable to that workspace.

If distinct logical paths cannot be represented distinctly under the resolved filesystem's Unicode behavior, the carrier is inapplicable to that workspace.

The mapping boundary MUST NOT silently merge, overwrite, case-fold, or normalize distinct logical paths.

Exact collision behavior on case-insensitive or normalization-enforcing filesystems remains unverified. Such environments MUST NOT be claimed as supported until conformance evidence exists.

## Permissions and access

Failure to observe or access a required workspace location is an environmental failure, not an invalid carrier.

Planning MUST NOT claim applicability when required access is unavailable.

Exact mode-bit, ACL, ownership, privilege, and platform-specific permission behavior is unspecified outside verified environments. Diagnostics and process representation belong to later authorities.

## Planning preconditions

Planning records the safety- and conflict-relevant workspace facts on which applicability depends.

Before each affected mutation, application MUST revalidate relevant preconditions, including containment, link status, target type, parent state, collisions, and ownership of the intended path where applicable.

A changed precondition produces a conflict or environmental failure. Application MUST NOT silently reinterpret or extend the accepted plan.

Whole-operation atomicity, ordering, rollback, and partial-failure semantics belong to `docs/spec/operations.md`.

## Read-only entries

A logical path declared read-only remains subject to every validation, mapping, containment, link, collision, entry-type, and permission rule in this specification.

Application does not write the represented payload to a read-only target.

Whether a missing or differing read-only target blocks operation success, produces a verification difference, or remains an allowed reference discrepancy belongs to `docs/spec/operations.md`.

## Validation

A mapped path is applicable only when:

- the logical carrier path is valid;
- the workspace root is explicit and supported;
- lexical and physical containment hold;
- no final or ancestor symlink participates;
- existing components have supported types;
- distinct logical paths remain distinct physical targets;
- required observation succeeds;
- planned parent creation is safe;
- relevant preconditions can be recorded and later revalidated.

A failure of these conditions is a workspace-applicability, environmental, or unsupported-environment result. It is not carrier syntax invalidity.

## Results and errors

This specification distinguishes:

- applicable mapping;
- containment conflict;
- symlink conflict;
- path-identity collision;
- existing entry-type conflict;
- unsupported special entry;
- permission or observation failure;
- changed precondition;
- unverified or unsupported environment.

Operation specifications own the exact effects, result aggregation, diagnostics, and process representation of these conditions.

## Determinism and environmental inputs

For identical logical paths, workspace root, workspace observations, and resolved filesystem semantics, mapping and applicability decisions MUST be semantically deterministic.

Filesystem case behavior, Unicode behavior, entry types, links, permissions, and executable platform are environmental inputs. They must be resolved or reported at the workspace boundary rather than read implicitly by semantic path rules.

## Safety properties

Workspace path processing MUST NOT:

- access a target outside the explicit workspace root;
- follow a source, final-target, or ancestor symlink for payload access or mutation;
- open a FIFO, socket, device, or unknown object as a regular file;
- merge distinct carrier paths silently;
- claim a directory target is a writable regular file;
- continue mutation after a relevant precondition changes without reporting the change.

## Compatibility

No historical workspace-path compatibility classification is established by this specification. Historical relationships remain unspecified and do not alter the accepted mapping and safety contract.

Observed implementation behavior is evidence only. This specification deliberately rejects following comparison symlinks, allowing in-workspace ancestor symlinks during application, blocking on special objects, and treating a directory target as previewable regular-file output.

Historical reliance on those behaviors has not been demonstrated.

## Applicable schemas

None. This specification has no schema-governed boundary.

## Required verification

Conformance evidence MUST cover at least:

- explicit workspace-root handling;
- lexical and physical containment;
- missing regular-file targets;
- existing regular files;
- final and broken symlinks;
- in-workspace and escaping ancestor symlinks;
- source symlinks, including in-workspace, broken, and escaping links;
- directory traversal without following links;
- comparison without following links;
- directory where a regular file is intended;
- missing parent creation;
- FIFO, socket, device, and unknown-entry classification without content access;
- case collisions on each claimed supported filesystem;
- Unicode-equivalence collisions on each claimed supported filesystem;
- permission and observation failures;
- changed preconditions between preview and mutation;
- read-only paths passing through the same safety mapping;
- separation between carrier validity and workspace applicability.

Every supported-environment claim requires platform and filesystem evidence. Tests that intentionally use special objects or links must be bounded and must not follow or read those objects during fixture inspection.

## Bounded unspecified and future work

The following remain outside this specification's accepted boundary and do not prevent conformance within the verified boundary:

- support for Windows, macOS, network filesystems, and additional Python versions;
- exact permission behavior beyond environmental-failure classification;
- operation-wide partial-failure and atomicity semantics;
- exact operation results for read-only discrepancies;
- presentation of mapping conflicts and unsupported environments.

These decisions do not alter the mapping and safety rules stated above for the currently verified boundary.

## Maturity transition

This specification is Accepted because mapping, containment, no-follow observation, entry types, collisions, permission categories, revalidation, and the verified-environment boundary completely determine conformance within scope. Additional platform support requires evidence but is not an unresolved semantic question for the accepted boundary.

## Authority boundary

This document owns workspace mapping, filesystem observation, containment, entry-type, link, collision, permission-category, and changed-precondition semantics.

`docs/spec/dx-carrier.md` owns logical carrier-path syntax and carrier validity. `docs/spec/selection.md` owns source candidate and inclusion behavior. `docs/spec/operations.md` owns planning, mutation, comparison result categories, read-only success semantics, overwrite behavior, and partial failure. Architecture continues to own dependency and capability boundaries.
