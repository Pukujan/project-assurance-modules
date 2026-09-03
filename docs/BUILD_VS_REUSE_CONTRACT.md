# Build-vs-reuse assessment contract

## Purpose

`projectization.build-vs-reuse@0.2.0` hardens the projectization gate against a concrete failure mode discovered in a real adopter: a free-form decision document can look complete while comparing a bespoke capability only against self-references, methodology, internal context, or abstract categories rather than researched alternatives.

The v0.2 module therefore separates **discovery evidence** from the **implementation decision**. It uses `schemas/reuse-assessment.schema.json` with contract identity `pam-reuse-assessment/0.1.0` and semantic validation in `scripts/pam_reuse.py`.

This is a projectization evidence contract, not a web crawler or procurement system. PAM does not decide which search engine, registry, catalog, or repository host an adopter must use. It does require the adopting project to preserve enough concrete evidence to show what discovery was performed and which identified candidates informed the decision.

## Evidence chain

```text
capability + constraints
        |
required discovery scopes / asset classes
        |
traceable internal + external searches
        |
source/search receipts
        |
concretely identified candidates
        |
trade-off comparison + cheap probes
        |
reviewed implementation disposition
```

The durable decision may summarize this chain, but it cannot substitute for the chain itself.

## Search coverage

For nontrivial software projectization, the v0.2 assessment declares and executes both:

- `internal` discovery — prior systems, components, contracts, datasets, or other reusable assets already available to the adopting organization/owner;
- `external` discovery — maintained OSS, packages, services, standards, applications, datasets, models, corpora, benchmarks, question banks, or other relevant external alternatives.

A search record names its surface, query, target classes, outcome, and one or more concrete receipts. A receipt must resolve to an externally or organizationally identifiable location such as a repository, URL, package-registry locator, catalog, or standard. A project-authored prose file saying "research was done" is not itself a search receipt.

The contract does not require a candidate to exist. A traceable search may legitimately record `no_candidates`. The requirement is discovery coverage, not fabrication of alternatives.

## Candidate identity

A serious candidate must have a concrete identity and locator. Examples include:

- `owner/repository`;
- a package-registry identity;
- a service or application URL;
- a standard identifier/locator;
- a dataset/model/corpus/benchmark/question-bank/content-asset locator.

Abstract labels such as `generic quiz framework`, `existing library`, or `some OSS` do not establish that an actual alternative was researched.

Two identities are explicitly disallowed as product/runtime alternatives:

1. the adopting project itself;
2. `Pukujan/project-assurance-modules`.

PAM may of course appear as the methodology revision governing the assessment. It simply cannot be used as evidence that application/runtime alternatives were researched.

## Internal reuse is necessary but not sufficient

Prior internal systems can be high-value reuse candidates and should be considered. They do not, by themselves, establish adequate discovery when plausible external alternatives exist.

This prevents a project from searching only its owner's repositories, finding something adjacent, and concluding that the external solution space has been considered.

## Reusable asset discovery

Build-vs-reuse applies to more than runtime code. A project may unnecessarily create datasets, models, corpora, benchmark material, question banks, or other content assets even when mature reusable assets exist.

The assessment therefore declares `required_asset_classes`. Every required class must appear in executed search coverage. When the Project Assurance Manifest declares `benchmark_or_dataset_use=true`, semantic validation requires at least one reusable asset class to be part of the search plan.

Selection of an asset does not waive benchmark integrity. Once an external or mutable asset is actually used for evaluation, the benchmark module still owns exact protocol/data identity, contamination boundaries, leakage checks, and reproducible result evidence.

## Candidate comparison

Each serious candidate records material trade-offs including:

- fitness;
- maintenance;
- license;
- security;
- extensibility;
- integration cost;
- performance;
- material reasons for its disposition.

Unknowns should remain explicit. The contract is designed to prevent a fluent agent from converting missing research into confident prose.

## Cheap probes

A serious full-coverage candidate that is rejected or still marked `spike_required` must have a probe record.

A probe may be:

- `run`, with concrete evidence; or
- `not_run`, with an explicit rationale explaining why testing would be disproportionate, unsafe, or otherwise unjustified.

This does not require expensive benchmarking of every candidate. It prevents silent prose-only rejection where the material uncertainty is cheap to test.

## `build_new` gate

A `build_new` decision must:

- record concrete unmet scoped requirements or unacceptable trade-offs;
- be grounded in the traceable searches and candidate register;
- preserve partial reuse where appropriate rather than treating reuse/build as a false binary;
- have no unresolved serious full-coverage candidate still requiring a probe;
- retain residual uncertainty and reconsideration triggers.

`build_new` is therefore a conclusion earned after discovery, not the default starting state.

## Review state

Assessments have two states:

- `draft` — discovery/comparison may still be incomplete;
- `reviewed` — the final disposition has explicit human/project-owner approval evidence.

`REUSE_008` cannot be satisfied by a draft assessment.

When any v0.2 reuse requirement from `REUSE_002` through `REUSE_008` is marked satisfied in a manifest, `pam_validate` requires the satisfied closure to reference one shared reuse-assessment artifact and validates that artifact semantically. Human approval alone cannot replace it.

## Versioning and compatibility

`projectization.build-vs-reuse@0.1.0` remains valid historical methodology. It is not rewritten.

`projectization.build-vs-reuse@0.2.0` is a **breaking methodology change** because its closure semantics are intentionally stricter. An assessment accepted under v0.1 may fail under v0.2 until traceable discovery evidence is added.

`projectization.software@0.2.0` references the hardened module. Automatic profile composition selects the newest shipped profile version, while a historical manifest that explicitly pins `projectization.software@0.1.0` continues to resolve against its original module identities.

The repository Git revision remains part of the full methodology identity. Consumers should continue pinning an exact PAM commit.

## Validation

Validate an assessment directly with:

```text
python -m scripts.pam_reuse <reuse-assessment.json>
```

`python -m scripts.pam_validate <PROJECT_ASSURANCE.json>` also validates referenced v0.2 reuse-assessment artifacts when applicable.

The normal `make check` lane includes a positive contract example and adversarial tests covering the Interview OS shortcut, adopting-project self-reference, PAM-as-runtime misuse, abstract candidates, missing external discovery, missing reusable-asset discovery, circular search evidence, unresolved cheap probes, unknown versions, and draft final dispositions.

## Regression precedent

PAM issue #10 records the originating defect. `fixtures/reuse/interview-os-shortcut.json` preserves a schema-shaped reproduction of the invalid shortcut so future changes cannot silently re-open the loophole.
