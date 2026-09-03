# Architecture

## Design principle

Project Assurance Modules is a **methodology composition repository**, not a runtime control plane.

It stores reusable, versioned definitions that answer:

- what methodology exists;
- when it applies;
- what evidence closes it;
- how projects compose modules;
- how a project pins the exact methodology it used;
- how a fresh workspace acquires/verifies that revision;
- how material execution state is handed off without making stale prose authoritative.

Project-specific live state remains in the adopting project.

## Conceptual model

```text
exact PAM revision
       |
project facts + intended claims
          |
          v
    profile selection
          |
          v
       router
          |
          v
module dispositions
(required / recommended / conditional / not_applicable)
          |
          v
human review / rationale
          |
          v
PROJECT_ASSURANCE manifest
          |
   +------+------------------+
   |                         |
project bootstrap         implementation
specs/issues/CI           evidence closure
   |                         |
   +-----------+-------------+
               |
     machine-valid handoff
```

The bootstrap acquisition contract proves the methodology revision being used. The project manifest records routing/requirement state. Specialized evidence contracts may establish additional fail-closed closure semantics for requirements that cannot safely rely on free-form self-attestation. The structured handoff records resumable current execution state. None of these replaces live GitHub/CI truth.

## Repository organization

The repository deliberately separates:

- `schemas/` — generic and specialized machine contracts;
- `modules/` — independently versioned methodology obligations;
- `profiles/` — reusable selection/composition entry points;
- `scripts/` — deterministic validators, routing, profile composition, specialized evidence validation, and documentation checks;
- `examples/` — validating adopter examples;
- `fixtures/` + `tests/` — positive/negative routing, adversarial, and contract evidence;
- `docs/` + `specs/` — human architecture, routing, contract, and product documentation;
- `experiments/` — frozen methodology-evaluation evidence, not current mutable project state;
- `knowledge-packs/` — optional durable lineage artifacts that do not imply external-runtime ingest.

Directories are organizational. Stable identities come from the contracts themselves plus exact Git revision, not paths alone.

<!-- BEGIN PAM GENERATED INVENTORY -->
## Current repository inventory

> Generated from the shipped module/profile/schema files. This inventory describes landed repository state, not roadmap candidates or unmerged pull requests.

Methodology status: **bounded PAM v0.2** (landed); frozen tested revision `a10ad56b7088c1e101e80914a9e00357dbef9120`.

### Modules

- `benchmark.integrity@0.1.0` — Benchmark, dataset, and holdout integrity (`modules/benchmark/integrity/module.yaml`)
- `continuity.structured-handoff@0.1.0` — Structured project and agent handoff (`modules/continuity/structured-handoff/module.yaml`)
- `engineering.swe-ci-foundation@0.1.0` — Software engineering and CI foundation (`modules/engineering/swe-ci-foundation/module.yaml`)
- `planning.foundation@0.1.0` — Planning foundation (`modules/planning/foundation/module.yaml`)
- `projectization.build-vs-reuse@0.1.0` — Build vs reuse decision (`modules/projectization/build-vs-reuse/module.yaml`)
- `projectization.build-vs-reuse@0.2.0` — Build vs reuse decision with traceable discovery (`modules/projectization/build-vs-reuse/versions/0.2.0/module.yaml`)
- `projectization.scope-boundary@0.1.0` — Project scope boundary (`modules/projectization/scope-boundary/module.yaml`)
- `provenance.decision-lineage@0.1.0` — Decision lineage and provenance boundary (`modules/provenance/decision-lineage/module.yaml`)

### Profiles

- `benchmark.empirical-work@0.1.0` — Empirical evaluation integrity (`profiles/benchmark/empirical-work/profile.yaml`)
- `continuity.material-work@0.1.0` — Material continuity (`profiles/continuity/material-work/profile.yaml`)
- `projectization.software@0.1.0` — Software projectization (`profiles/projectization/software/profile.yaml`)
- `projectization.software@0.2.0` — Software projectization with traceable reuse discovery (`profiles/projectization/software/versions/0.2.0/profile.yaml`)
- `provenance.material-decisions@0.1.0` — Material decision lineage (`profiles/provenance/material-decisions/profile.yaml`)

### Schemas

- `schemas/bootstrap-acquisition.schema.json`
- `schemas/module.schema.json`
- `schemas/profile.schema.json`
- `schemas/project-assurance-manifest.schema.json`
- `schemas/reuse-assessment.schema.json`
- `schemas/structured-handoff-v0.2.schema.json`
- `schemas/structured-handoff.schema.json`
<!-- END PAM GENERATED INVENTORY -->

## Module

A module is intentionally narrow. It contains:

- stable ID and semantic version;
- intent and non-scope;
- applicability signals;
- requirements;
- acceptable evidence kinds;
- closure rules;
- dependencies/conflicts where justified;
- compatibility impact for newer module-contract revisions;
- references to source methodology/precedent.

Do not make one "complete engineering" module containing every practice.

`pam-module/0.1.0` modules remain valid. The evolved `pam-module/0.2.0` contract adds portable motivation/conflict/compatibility metadata without rewriting older module identities.

`projectization.build-vs-reuse@0.2.0` is a breaking methodology revision of the build-vs-reuse module, not a rewrite of `0.1.0`. It requires traceable discovery through the separate `pam-reuse-assessment/0.1.0` evidence contract.

## Profile

A profile is a reusable composition selected from explicit project facts. The landed bounded profiles currently cover:

- software projectization;
- material continuity;
- empirical/benchmark work;
- consequential/material decisions.

Profile selection is three-state:

- `selected`;
- `conditional` when required facts are missing;
- `not_selected` when declared facts contradict the selector.

Profiles constrain/organize module consideration; the router still determines module disposition. Profiles do not turn every referenced module into an unconditional requirement.

When multiple semantic versions of a profile are shipped, automatic composition selects the highest version for that profile identity. Exact historical profile versions remain resolvable when a manifest pins them explicitly.

## Routing

Routing has two stages:

1. **deterministic candidate routing** from explicit declared project facts;
2. **reviewed requirement/evidence state** in the adopting project manifest.

The router must never silently turn uncertainty into `not_applicable`.

Allowed module dispositions:

- `required`
- `recommended`
- `conditional`
- `not_applicable`

A project manifest tracks requirement execution state separately:

- `pending`
- `satisfied`
- `not_applicable`
- `deferred`
- `blocked`

This separation prevents "selected" from meaning "completed".

## Evidence-backed closure

Markdown checkboxes may be generated for humans, but they are not authoritative state.

A satisfied requirement points to one or more concrete evidence references such as:

- repository path;
- test identifier;
- CI run;
- commit/PR;
- benchmark report/artifact;
- reviewed decision record;
- provenance receipt;
- explicit human approval where judgment is inherent.

Agents cannot satisfy a requirement solely by stating that it was completed.

For methodology obligations vulnerable to circular self-attestation, PAM may additionally require a specialized machine-valid evidence contract. Build-vs-reuse v0.2 is the first such case: search/source receipts, concrete candidate identities, reusable-asset discovery, probe state, and the reviewed disposition live in a `pam-reuse-assessment/0.1.0` artifact. A prose decision may explain that artifact but cannot substitute for it.

## Project Assurance Manifest

The adopting project owns its manifest. It records:

- project identity and facts;
- exact PAM revision;
- selected profile versions;
- module versions/dispositions;
- per-requirement state and evidence;
- explicit N/A/defer rationale;
- current methodology phase.

PAM never stores every adopter's live project state.

When build-vs-reuse v0.2 requirements are marked satisfied, manifest validation resolves the referenced reuse-assessment artifact within the adopting project and applies the specialized semantic validator in addition to ordinary evidence-kind validation.

## Bootstrap acquisition

A fresh workspace must be able to acquire the exact requested methodology revision, checkout detached, verify the resolved commit, and fail before routing if acquisition/revision/start-state verification fails.

Git-object/content identities are authoritative; transformed working-tree bytes are not used as a substitute for exact repository identity.

## Structured handoff

The generic handoff contract preserves current resumable project/component/revision/validation/blocker/next-action state while enforcing:

- live-state precedence over stale handoff state;
- explicit current versus historical-checkpoint semantics;
- exact methodology/component identities;
- exclusion of hidden/confirmatory evaluation material from agent-visible state.

An adopter may retain a project-local handoff contract until generic parity is explicitly proven and migration is separately approved.

## Versioning

Four identities matter:

```text
methodology repository revision
schema contract version
module semantic version
profile semantic version
```

Adopters should pin an exact repository SHA even when module/profile versions are present. A module version must change when its requirement semantics, applicability, or closure evidence materially changes. A profile version must likewise change when its referenced methodology set changes materially.

The Python package version is tooling metadata; it is not a methodology revision identifier.

Historical manifests, handoffs, bootstrap records, reuse assessments, and frozen benchmark artifacts are never rewritten merely because a newer PAM revision exists.

## Projectization gate

Before automated project bootstrap (repositories, issue trees, GitHub Projects, milestone creation, generated CI plans), a nontrivial project should have a reviewed preflight manifest.

The methodology may generate a gap report before approval, but should not create large executable backlogs based on unreviewed routing.

For current software projectization, build-vs-reuse must establish traceable internal/external discovery and relevant reusable-asset search before a bespoke implementation decision can be considered reviewed. See `docs/BUILD_VS_REUSE_CONTRACT.md`.

## Extraction rule

New modules should preferably come from one of:

- a repeated process observed across multiple real projects;
- a well-established external engineering/research methodology;
- a failure repeatedly caused by absence of the process;
- a project-specific mechanism that demonstrated portable value.

A technique being interesting is not enough. Research Assurance is a reference source/adopter, not a universal architecture; extraction must preserve that boundary.

A real adopter defect may justify a versioned hardening of an existing module when the failure demonstrates that its current closure semantics can be satisfied without achieving the intended methodological outcome. That hardening must preserve the historical module identity rather than silently changing it.

## Documentation inventory rule

`docs/repository-state.json` owns the small shared release-status facts. Module/profile/schema inventory is derived directly from the shipped files. `make docs-sync` regenerates the marked README/architecture blocks, and `make docs-check` fails when they drift.

Roadmap candidates and unmerged pull requests are intentionally excluded from generated landed-state inventory.
