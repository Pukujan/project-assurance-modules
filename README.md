# Project Assurance Modules

A versioned, modular methodology registry for turning sufficiently researched ideas into engineered projects without relying on a human or agent to remember every planning, validation, governance, continuity, and evidence requirement.

The core question is:

> Before research becomes repositories, issue plans, architecture, code, benchmarks, or releases, what applicable engineering-assurance work are we forgetting?

This repository is **not** a runtime assurance service and is **not** a universal stamp system. It provides reusable methodology modules, routing profiles, schemas, validators, and evidence requirements that projects can pin by exact revision.

## Intended flow

```text
research / exploration
        |
human decides research is mature enough for projectization
        |
project-assurance preflight
        |
classify project facts and intended claims
        |
route applicable versioned modules
        |
gap analysis + human review
        |
freeze PROJECT_ASSURANCE manifest
        |
create project specs / repo / issues / CI / benchmarks
        |
implementation closes requirements with evidence
```

A requirement is not satisfied because an agent says it is done. Closure should point to mechanically checkable evidence where possible: files, tests, CI runs, benchmark artifacts, exact revisions, reviewed decisions, or explicit justified `not_applicable` dispositions.

## Bootstrap documents

- `specs/PDD.md` — product problem, goals/non-goals, workflow, trust boundary and kill criteria.
- `docs/ARCHITECTURE.md` — module/profile/router/manifest architecture and versioning rules.
- `docs/ROUTING.md` — research-to-project preflight and applicability routing semantics.
- `docs/MODULE_ROADMAP.md` — candidate module families extracted from real repeated project work.
- `schemas/module.schema.json` — v0 module contract.
- `schemas/project-assurance-manifest.schema.json` — v0 adopting-project manifest contract.
- `modules/continuity/structured-handoff/module.yaml` — first reference module.
- `examples/PROJECT_ASSURANCE.example.json` — example adopter state.

## First reference adopter

`Pukujan/research-assurance` is the first reference source/adopter. Its structured handoff/continuity process is the first extracted module; its PDD/SDD/invariants, failure/validation strategy, benchmark integrity, scope/adversarial process, FOSSIL lineage, GitHub planning, and multi-repository orchestration are candidate future extractions rather than automatic universal requirements.

## Future-session usage target

Eventually a project owner should be able to tell a fresh capable agent:

> Read `Pukujan/project-assurance-modules`. My research is mature enough for projectization. Run preflight before creating the repository/issue/implementation plan.

The agent should inspect the durable research/project facts, route applicable versioned modules, show gaps and N/A/conditional rationale, and wait for review before generating the executable project bootstrap.

## Status

The repository is bootstrapping under issue `#1`. Until a stable methodology release exists, consumers should pin an exact commit and treat module contracts as experimental.
