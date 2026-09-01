# Projectization gate

## Purpose

The projectization gate is the boundary between exploratory research and an engineered project. Its job is not to decide whether a research conclusion is true. Its job is to prevent an agent from jumping directly from "interesting idea" to repository/issue/code generation without first answering two questions:

1. **Should we build this at all, or can an existing system be reused/composed/extended?**
2. **What is the smallest justified scope if we do build?**

The gate runs after an authorized human/project owner says the research is mature enough for project preflight.

## Required sequence

```text
research / exploration
        |
human: research is mature enough for projectization
        |
research handoff
        |
build-vs-reuse assessment
        |
scope boundary
        |
project classification + PAM routing
        |
gap analysis
        |
human review of material dispositions
        |
freeze PROJECT_ASSURANCE manifest
        |
only then: repository/spec/issue/CI/benchmark bootstrap
```

Do not create a large implementation backlog before this boundary is reviewed.

## Research handoff

The handoff should summarize the research that matters to projectization without forcing implementation agents to replay an entire transcript. It should preserve:

- problem and intended outcome;
- research conclusions that are being treated as input assumptions;
- important evidence/source references;
- alternatives already considered;
- unresolved questions;
- known existing systems/standards/OSS candidates;
- rejected approaches and why;
- constraints, non-goals, and decision uncertainty.

The handoff is project-operational context. It is not proof that every underlying research claim is correct.

## Build-vs-reuse decision

Before authorizing bespoke implementation, evaluate plausible existing options. Valid dispositions include:

```text
reuse
configure
wrap
extend
compose
fork
build_new
more_research
```

A `build_new` disposition must identify concrete unmet requirements or unacceptable trade-offs. An agent preference to write code is not evidence.

Where a candidate is serious and cheaply testable, prefer a spike, contract test, compatibility probe, or benchmark over prose-only rejection.

## Scope boundary

Freeze at least:

- current goal;
- current claims/capabilities to be delivered;
- explicit non-goals;
- current assurance horizon;
- deferred mechanisms and their reconsideration triggers;
- rejected mechanisms and rationale;
- current repository/component boundary;
- complexity budget where useful.

A new technology, red-team finding, or interesting mechanism does not automatically become project scope. It must pass the adopting project's scope-admission rule.

## Durable outputs

The adopting project should normally keep these as Git-tracked operational truth:

```text
PROJECT_ASSURANCE.yaml/json
assurance/RESEARCH_HANDOFF.md or structured equivalent
assurance/BUILD_VS_REUSE.yaml
assurance/SCOPE_BOUNDARY.yaml or docs/SCOPE.md
```

Generated checklists may render this state for humans, but the authoritative requirement state is the validated Project Assurance Manifest and its evidence references.

## FOSSIL boundary

PAM and FOSSIL solve different problems.

- **PAM/project Git state** answers what methodology applies now, what remains pending, and what evidence closes a requirement.
- **FOSSIL** preserves durable evidence/lineage for consequential research and project decisions.

Do not require FOSSIL writes for every exploratory thought or every checklist transition. A useful default is:

```text
exploration transcript/notes
        |
projectization promotion
        |
Git operational artifacts
        |
important reviewed transitions
        |
FOSSIL lineage/receipts
```

Ingest the compact research handoff, reviewed build-vs-reuse decision, scope boundary, frozen Project Assurance Manifest, and later material architecture/milestone decisions when durable lineage is valuable. Keep ordinary scratch reasoning cheap.

## Failure modes

The gate fails its purpose if:

- the agent creates code/backlogs before checking reuse;
- every project is forced through every available methodology;
- `not_applicable` is used to hide uncertainty;
- FOSSIL becomes the live task tracker;
- transcript ingestion becomes mandatory per thought;
- checkboxes can be satisfied by agent self-report;
- scope-control becomes a universal ban on experimentation;
- build-vs-reuse is satisfied by an untested search result when a cheap comparison was feasible.
