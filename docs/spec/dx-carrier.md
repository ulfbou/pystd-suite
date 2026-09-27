# DX v2 Carrier Format

Status: Normative
Owner: DX v2 carrier format and preservation semantics
Scope: DX v2.0.0 carrier framing, entries, attributes, payload representation, logical carrier paths, decoding, serialization, and structural verification
Maturity: Accepted

## Purpose

This specification defines the DX v2.0.0 carrier as a platform-neutral representation of transported files and carrier metadata. It establishes the rules needed to parse, validate, serialize, structurally verify, and recover the exact decoded bytes of transported entries.

## Scope

### In scope

This specification governs:

- v2.0.0 framing;
- FILE and NOTE blocks;
- FILE attributes;
- text and base64 payload representation;
- terminal LF preservation;
- block-terminator escaping;
- logical carrier-path syntax;
- duplicate-path handling;
- decoded-byte preservation;
- normative serializer ordering;
- format-level determinism;
- structural verification and decoded-entry hashing terminology.

### Out of scope

This specification does not govern workspace applicability, physical filesystem behavior, source selection, operation lifecycle, application conflict policy, CLI syntax, process results, machine-output fields, historical compatibility classifications, or implementation structure.

## Terminology

**Physical line** means a line in the UTF-8 carrier text, separated by LF for parsing purposes.

**Directive** means a physical line beginning with `%%` at column zero and recognized by the framing grammar.

**Decoded entry bytes** means the byte sequence represented by a FILE block after text reconstruction or base64 decoding.

**Normative serializer** means the serializer that emits the canonical v2.0.0 representation defined by this specification.

## Carrier structure

A v2.0.0 carrier MUST contain, in order:

1. exactly one header line;
2. zero or more complete FILE or NOTE blocks, with semantically insignificant blank lines permitted between blocks;
3. exactly one logical end line.

The header is:

```text
%%DX v2.0.0
```

The logical end is:

```text
%%END
```

A missing, duplicate, or unsupported header makes the carrier invalid. A missing logical end makes the carrier invalid. Nonblank content after the logical end makes the carrier invalid.

Blank physical lines outside blocks are permitted and carry no meaning. Blank lines inside a block are interpreted according to that block's payload rules.

An unknown framing directive makes the carrier invalid. Directive lines MUST be consumed completely by their governing grammar. Unmatched, malformed, or unexplained trailing text is invalid.

DX v1.3.1 is outside this specification. New serialization MUST NOT emit it. Future migration support requires independent compatibility evidence and authority.

## NOTE blocks

A NOTE block begins with a NOTE directive and ends with an ENDBLOCK directive:

```text
%%NOTE
carrier metadata
%%ENDBLOCK
```

A NOTE block is carrier metadata. It is not a transported workspace file and has no v2.0.0 semantic effect on selection, workspace mapping, structural verification, or application.

The normative serializer is not required to generate NOTE blocks. NOTE content MUST NOT be interpreted as an extension mechanism in v2.0.0.

An unterminated NOTE block makes the carrier invalid.

## FILE blocks

A FILE block begins with a FILE directive and ends with an ENDBLOCK directive:

```text
%%FILE path="docs/example.txt"
payload
%%ENDBLOCK
```

The FILE directive consists only of the directive name and recognized double-quoted attributes separated by whitespace. Attribute names and values MUST be parsed completely. Unknown attributes, duplicate attributes, missing required attributes, malformed quoting, or unmatched directive text make the carrier invalid.

The FILE framing lines are not part of decoded entry bytes.

### FILE attributes

The only recognized FILE attributes are:

- `path`;
- `readonly`;
- `encoding`;
- `escaped`;
- `trailing_newlines`.

`path` is mandatory and occurs exactly once. The remaining attributes are optional and use the defaults defined below.

Boolean values accept exactly `"true"` and `"false"`. They are case-sensitive. Omitted `readonly` and `escaped` values default to false.

`encoding` is omitted for text entries or has the exact value `"base64"` for base64 entries. Other values are invalid.

`trailing_newlines` is valid only for text entries. Its value is a canonical nonnegative ASCII decimal integer: one or more digits, no sign, no whitespace, and no alternate numeric notation. Malformed values make the carrier invalid and MUST NOT escape as an unclassified implementation exception.

Base64 entries MUST NOT declare `escaped="true"` or `trailing_newlines`.

## Text representation

A text entry represents valid UTF-8 decoded entry bytes. Its represented byte sequence:

- contains no CR byte;
- contains no NUL byte;
- is reconstructed from UTF-8 payload text and LF line boundaries;
- has exactly the declared number of terminal LF bytes restored from `trailing_newlines`.

When `trailing_newlines` is omitted, its value is zero.

The body represents the payload after terminal LF bytes have been removed. Nonterminal LF bytes remain represented by payload line boundaries. Reconstruction MUST NOT depend on host text-mode newline conversion.

For normative serialization, source bytes use text representation only when they:

- decode as UTF-8;
- do not begin with a UTF-8 byte-order mark;
- contain no CR byte;
- contain no NUL byte.

All other source byte sequences use base64 representation.

An empty text block represents zero bytes. The normative serializer emits an empty source file as an empty text entry.

## Base64 representation

A base64 entry declares:

```text
encoding="base64"
```

Its payload MUST be strictly valid base64 and may represent any byte sequence, including zero bytes. Malformed base64 makes the carrier invalid.

Uniform serializer indentation and line wrapping are representational only. They do not add bytes to the decoded payload.

An empty, otherwise valid base64 body represents zero bytes. Both empty text and empty base64 are valid zero-byte representations, but normative serialization uses empty text for an empty source file.

## Escaping

Text escaping is required when an unescaped payload would contain a physical line exactly equal to:

```text
%%ENDBLOCK
```

An escaped text entry declares:

```text
escaped="true"
```

The normative escaped representation prefixes every payload physical line with exactly four ASCII space characters. Parsing removes exactly those four characters from every escaped payload line before text reconstruction. Any escaped payload line lacking the required prefix makes the carrier invalid.

The first framing-level, unescaped `%%ENDBLOCK` line closes the FILE block.

Other directive-like payload lines do not require escaping solely because they begin with `%%`.

Escaping changes carrier representation only. It MUST NOT change decoded entry bytes.

## Logical carrier paths

A carrier path is a platform-neutral, workspace-relative logical coordinate. It is not a host filesystem path.

A valid carrier path:

- is nonempty;
- uses `/` as its only separator;
- does not begin with `/`;
- is not a drive-like or UNC-like form;
- contains no empty component;
- contains no `.` or `..` component;
- does not end with `/`;
- contains no backslash;
- contains no double quote;
- contains no NUL, CR, LF, other C0 control character, or DEL.

Forms such as `C:/file`, `C:\file`, `//server/share`, repeated separators, and trailing separators are invalid.

Valid Unicode path text is preserved exactly as UTF-8. Carrier parsing does not apply Unicode normalization or case folding.

Carrier-path identity is case-sensitive. For example, `A.txt` and `a.txt` are distinct valid logical paths. Whether both are applicable to a particular workspace is governed by the workspace-path specification.

Each path MUST occur at most once in a carrier. An exact duplicate makes the complete carrier invalid.

## Read-only declaration

`readonly="true"` declares that application does not write the FILE entry's payload to its mapped workspace path.

The declaration does not exempt the path from carrier validation or safe workspace mapping. Comparison, verification, and operation-success semantics for missing or differing read-only entries belong to later operation specifications.

## Decoding and preservation

A valid FILE block decodes to exactly one logical carrier path, one decoded byte sequence, and its accepted attributes.

Parsing, structural verification, inspection, serialization of unchanged semantic inputs, and later application MUST NOT silently change decoded entry bytes.

Carrier framing, attribute syntax, base64 layout, text escaping, and serializer ordering are representation. Decoded bytes and accepted attributes are semantic carrier content.

## Structural verification

Structural verification establishes only that:

- the carrier parses;
- the declared format version is supported;
- framing is valid;
- attributes are recognized and valid;
- carrier paths are valid;
- carrier paths are unique;
- payloads decode successfully.

Structural verification does not establish:

- authenticity;
- carrier-contained integrity;
- agreement with a workspace;
- applicability to a workspace;
- historical compatibility.

## Decoded-entry hashing

A decoded-entry hash is SHA-256 calculated over one entry's decoded bytes.

A calculated hash supports inspection and verification evidence only when its expected value and trust source are identified. Computing a decoded-entry hash alone is not integrity verification.

DX v2.0.0 defines no carrier-contained integrity field or manifest. A FILE attribute such as `sha256` is invalid. Any future integrity mechanism requires an independently justified and versioned format decision.

## Normative serialization

The normative serializer:

- emits the exact v2.0.0 header and logical end;
- emits FILE entries in ascending Unicode code-point order of validated carrier-path text;
- emits a stable documented attribute order;
- omits attributes whose default representation is required to be absent;
- chooses text or base64 according to this specification;
- applies escaping only when required;
- emits complete deterministic framing.

Attribute order is semantically irrelevant to parsing. A parser MUST NOT require normative serializer order.

For identical complete explicit serialization inputs, the normative serializer MUST produce byte-identical carrier output.

Current byte-reproducibility evidence covers Linux with Python 3.12 on overlayfs. Cross-platform byte identity remains unverified and MUST NOT be claimed without additional evidence. Semantic determinism remains required on every supported environment.

## Validation

A carrier is invalid when any mandatory framing, attribute, path, uniqueness, escaping, text, or base64 rule in this specification is violated.

Invalidity MUST be reported as an invalid-carrier result. Implementations MUST NOT guess intended syntax, silently ignore malformed directive content, or expose raw parsing-conversion errors as the carrier contract.

## Results and errors

This specification distinguishes:

- valid carrier;
- invalid carrier;
- unsupported carrier version;
- resource or environmental failure while obtaining carrier bytes.

The exact diagnostic vocabulary, process representation, and numeric outcomes belong to later authorities.

## Determinism and environmental inputs

Carrier decoding and validation depend only on the supplied carrier bytes and the supported format contract.

Serialization depends only on complete explicit semantic inputs and this serializer contract. Locale, current directory, filesystem enumeration order, timestamps, random values, and ambient configuration MUST NOT change carrier bytes once serialization inputs are fixed.

## Compatibility

No historical compatibility classification is established by this specification. Historical input and migration behavior are outside this accepted v2.0.0 format boundary and remain unspecified until separately classified.

Existing parser and serializer behavior is implementation evidence. This specification makes no compatibility commitment for DX v1.3.1 or established historical workflows.

## Applicable schemas

None. This specification has no schema-governed boundary.

## Required verification

Conformance evidence MUST cover at least:

- required, duplicate, missing, and unsupported headers;
- complete FILE and NOTE framing;
- logical end and trailing content;
- complete directive lexical validation;
- recognized, unknown, duplicate, malformed, and conflicting attributes;
- valid and malformed base64;
- zero-byte payloads;
- UTF-8 text with zero, one, and multiple terminal LF bytes;
- CRLF, CR, BOM, NUL, invalid UTF-8, and arbitrary binary bytes;
- literal `%%ENDBLOCK` payload lines;
- other directive-like payload lines;
- long physical payload lines;
- every rejected path form;
- Unicode and case-distinct carrier paths;
- duplicate-path detection;
- decoded-byte round trips;
- structural-verification limits;
- decoded-entry hashing;
- deterministic entry and attribute ordering;
- byte-identical repeated serialization in each environment for which that claim is made.

Verification compares source and recovered bytes directly and records byte counts and SHA-256 values where applicable.

## Bounded future work
The following remain outside the accepted v2.0.0 boundary and do not affect conformance to it:

- whether historical v1.3.1 input requires migration support;
- whether a future format admits carrier-contained integrity metadata;
- how future format extensions are versioned;
- whether byte-identical normative serialization is verified across additional platforms.

None of these questions changes conformance for the v2.0.0 rules stated above.

## Maturity transition

This specification is Accepted because its v2.0.0 framing, representation, preservation, validation, determinism, and verification boundary completely determine conformance. Historical migration, future extensions, future integrity mechanisms, and support claims for additional environments remain explicitly outside this boundary.

## Authority boundary

This document owns DX v2.0.0 carrier representation and decoded-content semantics.

`docs/spec/workspace-paths.md` owns whether a valid logical carrier path can be mapped safely to a particular workspace. `docs/spec/selection.md` owns which source content becomes carrier input. `docs/spec/operations.md`, `docs/spec/diagnostics.md`, and `docs/spec/cli-process.md` own their respective observable behavior. Historical compatibility relationships remain unspecified until admitted by a compatibility authority. Architecture continues to own responsibility and dependency boundaries.
