# Project Assurance Modules

Project Assurance Modules (PAM) is a versioned, modular methodology registry for turning sufficiently researched ideas into engineered projects without relying on a human or agent to remember every planning, validation, governance, continuity, and evidence requirement.

PAM is **not** a runtime assurance service and is **not** a universal stamp system. It supplies reusable methodology modules, routing profiles, schemas, validators, bootstrap/handoff contracts, and evidence requirements that adopting projects pin by exact Git revision.

The core question is:

> Before research becomes repositories, issue plans, architecture, code, benchmarks, or releases, what applicable engineering-assurance work are we forgetting?

<!-- BEGIN PAM GENERATED REPOSITORY STATUS -->
## Current shipped methodology

> This section is generated from `docs/repository-state.json` and the live module/profile/schema files. Run `make docs-sync` after changing those inputs; CI runs `make docs-check` and fails on drift.

- Landed methodology: **bounded PAM v0.2** (landed).
- v0.2 landing merge: `66bd3e27f9241158da612f91f0204b6e4cd2855e`.
- Frozen tested methodology revision: `a10ad56b7088c1e101e80914a9e00357dbef9120`.
- Stability: **pre-v1**. Pin an exact Git commit. Do not treat mutable branch names or the Python package version as methodology identity.
- Reference source/adopter: `Pukujan/research-assurance`. Research Assurance is a reference source/adopter, not a universal architecture. Portable requirements must remain project-neutral.

### Shipped modules (7)

- `benchmark.integrity@0.1.0` — Benchmark, dataset, and holdout integrity (`modules/benchmark/integrity/module.yaml`)
- `continuity.structured-handoff@0.1.0` — Structured project and agent handoff (`modules/continuity/structured-handoff/module.yaml`)
- `engineering.swe-ci-foundation@0.1.0` — Software engineering and CI foundation (`modules/engineering/swe-ci-foundation/module.yaml`)
- `planning.foundation@0.1.0` — Planning foundation (`modules/planning/foundation/module.yaml`)
- `projectization.build-vs-reuse@0.1.0` — Build vs reuse decision (`modules/projectization/build-vs-reuse/module.yaml`)
- `projectization.scope-boundary@0.1.0` — Project scope boundary (`modules/projectization/scope-boundary/module.yaml`)
- `provenance.decision-lineage@0.1.0` — Decision lineage and provenance boundary (`modules/provenance/decision-lineage/module.yaml`)

### Routing profiles (4)

- `benchmark.empirical-work@0.1.0` — Empirical evaluation integrity (`profiles/benchmark/empirical-work/profile.yaml`)
- `continuity.material-work@0.1.0` — Material continuity (`profiles/continuity/material-work/profile.yaml`)
- `projectization.software@0.1.0` — Software projectization (`profiles/projectization/software/profile.yaml`)
- `provenance.material-decisions@0.1.0` — Material decision lineage (`profiles/provenance/material-decisions/profile.yaml`)

### Contract schemas (6)

- `schemas/bootstrap-acquisition.schema.json`
- `schemas/module.schema.json`
- `schemas/profile.schema.json`
- `schemas/project-assurance-manifest.schema.json`
- `schemas/structured-handoff-v0.2.schema.json`
- `schemas/structured-handoff.schema.json`

### Reproducible quick start

Pin the exact tested methodology revision rather than relying on a mutable branch:

```bash
git fetch origin a10ad56b7088c1e101e80914a9e00357dbef9120
git checkout --detach a10ad56b7088c1e101e80914a9e00357dbef9120
python -m pip install -e '.[dev]'
python -m scripts.pam_validate examples/PROJECT_ASSURANCE.example.json
python -m scripts.pam_handoff examples/HANDOFF_STATE.example.json
python -m scripts.pam_bootstrap examples/BOOTSTRAP_ACQUISITION.example.json
```

An adopting project owns its project facts, selected profiles, requirement/evidence state, bootstrap record, and current handoff. PAM supplies the versioned methodology contracts and deterministic validators; it is not an adopter runtime dependency.
<!-- END PAM GENERATED REPOSITORY STATUS -->

## Intended flow

```text
research / exploration
        |
human decides research is mature enough for projectization
        |
acquire and verify an exact PAM revision
        |
declare project facts and intended claims
        |
select profiles + route applicable modules
        |
gap analysis + reviewed dispositions
        |
freeze PROJECT_ASSURANCE manifest
        |
create project specs / repo / issues / CI / benchmarks
        |
implementation closes requirements with evidence
        |
maintain machine-valid current handoff across material sessions
```

A requirement is not satisfied because an agent says it is done. Closure should point to mechanically checkable evidence where possible: files, tests, CI runs, benchmark artifacts, exact revisions, reviewed decisions, receipts, or explicit justified `not_applicable` dispositions.

## Contracts and documentation

- `specs/PDD.md` — product problem, goals/non-goals, workflow, trust boundary, and kill criteria.
- `docs/ARCHITECTURE.md` — module/profile/router/manifest architecture and versioning rules.
- `docs/ROUTING.md` — research-to-project preflight and routing semantics.
- `docs/PROFILES.md` — profile selection/composition semantics.
- `docs/PROJECTIZATION_GATE.md` — reviewed preflight boundary before executable project bootstrap.
- `docs/STRUCTURED_HANDOFF_CONTRACT.md` — generic current-state handoff semantics.
- `docs/BOOTSTRAP_ACQUISITION_CONTRACT.md` — fresh-workspace exact-revision acquisition/verification contract.
- `docs/MODULE_ROADMAP.md` — candidate future module families; roadmap entries are not shipped requirements until extracted/versioned.
- `examples/` — validating adopter examples for the manifest, handoff, and acquisition contracts.

## Validation and documentation consistency

The normal deterministic lane is:

```bash
make check
```

When shipped modules, profiles, schemas, or repository release metadata change, run:

```bash
make docs-sync
make check
```

`make docs-check` derives the public inventory from the actual repository files and fails if generated README/architecture blocks drift. CI checks; it does not auto-commit documentation.

## Reference boundary

`Pukujan/research-assurance` is the first reference source/adopter and remains a primary source of extraction evidence. PAM does not copy Research Assurance topology or make every RA mechanism universal. A methodology becomes a PAM module only when its portable value and bounded applicability are justified.

The original RA retrospective evidence is frozen. New methodology revisions must receive new identities rather than rewriting the commits that were benchmarked.

## Stability

PAM is still pre-v1. Consumers should pin exact commits for reproducibility, even when module/profile/schema semantic versions are present. The Python package version is tooling metadata and is not the methodology identity.
