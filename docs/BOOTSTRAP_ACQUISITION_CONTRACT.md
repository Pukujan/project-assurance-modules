# Fresh-workspace bootstrap and acquisition contract

PAM uses `schemas/bootstrap-acquisition.schema.json` to define the minimum protocol a fresh worker needs before methodology routing or projectization begins.

## Contract identity

The first contract identity is `pam-bootstrap/0.1.0`.

This is an acquisition and identity boundary, not a deployment system. It does not install project dependencies, configure production infrastructure, choose a runtime, or authorize implementation work.

## Required sequence

A conforming fresh-workspace bootstrap follows this order:

1. identify the methodology repository and requested revision;
2. resolve that request to an immutable full Git commit;
3. fetch only the required revision or bounded shallow ref;
4. check out the resolved revision detached from a mutable branch;
5. verify `HEAD` resolves to the expected full commit;
6. locate the required start document, profile, or manifest;
7. only then begin routing or projectization.

If acquisition, revision resolution, revision verification, or the start locator fails, execution stops before routing. The worker must not guess a nearby branch, latest tag, default branch, or substitute start document.

## Tags and versions

A requested tag or version is not itself sufficient immutable identity. The contract always records `source.resolved_commit`, and verification is bound to that full commit. A tag/version may be the human-facing request while the resolved commit is the reproducible execution identity.

When the request is already a Git commit, the requested commit, resolved commit, and verification target must be identical. `scripts/pam_bootstrap.py` enforces this relationship in addition to JSON Schema validation.

## Content identity

Platform-transformed working-tree bytes are not the primary identity for methodology or benchmark inputs. Line-ending conversion and checkout filters can change those bytes without changing Git object identity.

Prefer:

- Git commit/tree/blob object identity for repository content;
- an explicit content digest for bytes that are not represented by Git objects.

The schema therefore fixes both `working_tree_bytes_authoritative` and `line_ending_normalization_authoritative` to `false`.

## Start locator

The bootstrap contract names exactly one required start locator and classifies it as a document, profile, or manifest. It must exist before routing begins. Profile selection semantics are intentionally deferred to the next bounded extraction; this contract only establishes how a fresh worker finds the authoritative starting point.

## Validation

Run:

```text
python -m scripts.pam_bootstrap <bootstrap-contract.json>
```

The normal PAM check lane validates `examples/BOOTSTRAP_ACQUISITION.example.json` and runs positive and fail-closed tests.
