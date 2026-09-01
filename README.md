# Project Assurance Modules

A versioned, modular methodology registry for turning sufficiently researched ideas into engineered projects without relying on a human or agent to remember every planning, validation, governance, continuity, and evidence requirement.

The core question is:

> Before research becomes repositories, issue plans, architecture, code, benchmarks, or releases, what applicable engineering-assurance work are we forgetting?

This repository is **not** a runtime assurance service and is **not** a universal stamp system. It provides reusable methodology modules, routing profiles, schemas, validators, and evidence requirements that projects can pin by exact revision.

Intended flow:

```text
research / exploration
        |
human decides research is mature enough for projectization
        |
project-assurance preflight
        |
classify project facts and claims
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

Initial reference adopter: `Pukujan/research-assurance`. Its structured handoff/continuity process is the first candidate module to extract and generalize.

The repository is bootstrapping. Until a tagged/stable methodology release exists, consumers should pin an exact commit and treat module contracts as experimental.
