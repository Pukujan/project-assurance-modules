# Architecture

## Design principle

Project Assurance Modules is a **methodology composition repository**, not a runtime control plane.

It stores reusable, versioned definitions that answer:

- what methodology exists;
- when it applies;
- what evidence closes it;
- how projects compose modules;
- how a project pins the exact methodology it used.

Project-specific state remains in the adopting project.

## Conceptual model

```text
project facts + intended claims
          |
          v
      profile/router
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
```

## Repository layout

```text
project-assurance-modules/
├── specs/
│   └── PDD.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── ROUTING.md
│   └── MODULE_ROADMAP.md
├── schemas/
│   ├── module.schema.json
│   └── project-assurance-manifest.schema.json
├── modules/
│   ├── continuity/
│   ├── planning/
│   ├── engineering/
│   ├── validation/
│   ├── benchmark/
│   ├── governance/
│   ├── provenance/
│   └── release/
├── profiles/
├── fixtures/
├── scripts/
└── tests/
```

Directories are organizational. A module's stable identity comes from `module_id` + module version, not its path alone.

## Module

A module is intentionally narrow. It contains:

- stable ID and semantic version;
- intent and non-scope;
- applicability signals;
- requirements;
- acceptable evidence kinds;
- closure rules;
- dependencies/conflicts where unavoidable;
- references to source methodology/precedent.

Examples:

```text
continuity.structured-handoff
planning.product-definition
planning.system-design
validation.metamorphic-testing
validation.mutation-testing
benchmark.hidden-holdout
provenance.fossil-decision-lineage
governance.github-project-bootstrap
```

Do not make one "complete engineering" module containing every practice.

## Profile

A profile is a reusable starting composition, for example:

```text
python-library
research-backed-software
stateful-system
empirical-ml-system
multi-repository-program
agent-assisted-project
```

Profiles are hints/compositions, not unquestionable policy. Routing still evaluates project facts and allows explicit justified exclusion/defer decisions.

## Routing

Routing has two stages:

1. **deterministic candidate routing** where rules can be expressed from declared project facts;
2. **reviewed disposition** where project context requires judgment.

The router must never silently turn uncertainty into `not_applicable`.

Allowed module dispositions:

- `required`
- `recommended`
- `conditional`
- `not_applicable`

A project manifest then tracks requirement execution state separately:

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

## Project Assurance Manifest

The adopting project owns its manifest. It records:

- project identity and facts;
- exact `project-assurance-modules` revision;
- selected profile versions;
- module versions/dispositions;
- per-requirement state and evidence;
- explicit N/A/defer rationale;
- current methodology phase.

This repository never stores every adopter's live project state.

## Versioning

Three identities matter:

```text
methodology repo revision
module semantic version
profile semantic version
```

Adopters should pin an exact repository SHA even when module/profile versions are present. A module version must change when its requirement semantics, applicability, or closure evidence materially changes.

Historical project manifests are never rewritten merely because a newer methodology version exists.

## Projectization gate

Before automated project bootstrap (repositories, issue trees, GitHub Projects, milestone creation, generated CI plans), the project should have a reviewed preflight manifest.

The methodology may generate a gap report before approval, but should not create large executable backlogs based on unreviewed routing.

## Extraction rule

New modules should preferably come from one of:

- a repeated process observed across multiple real projects;
- a well-established external engineering/research methodology;
- a failure repeatedly caused by absence of the process;
- a project-specific mechanism that demonstrated portable value.

A technique being interesting is not enough.

## First extraction

`continuity.structured-handoff` is the first reference extraction from `Pukujan/research-assurance`. Research Assurance remains the reference adopter while the generic contract is stabilized.
