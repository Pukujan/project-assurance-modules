# Candidate output contract

A benchmark run is a frozen project-planning artifact bundle, not a prose answer.

## Required run directory

```text
experiments/ra-retrospective-blind/runs/<run_id>/candidate/
├── RUN_MANIFEST.json
├── ACCESS_ATTESTATION.json
├── PROJECT_ASSURANCE.json
├── RESEARCH_HANDOFF.md
├── BUILD_VS_REUSE.md
├── SCOPE.md
├── PROJECT_PLAN.md
├── REPOSITORY_MAP.md
├── ISSUE_PLAN.yaml
├── VALIDATION_PLAN.md
├── HANDOFF_STATE.json
└── PAM_GAPS.md
```

Equivalent YAML/JSON serialization is allowed for `PROJECT_ASSURANCE` and `HANDOFF_STATE` only when the selected PAM schema supports it. Do not omit a required artifact merely because another document mentions the same topic.

## `RUN_MANIFEST.json`

Record at least:

```json
{
  "run_id": "...",
  "benchmark": "ra-retrospective-blind/v0",
  "pam_revision": "40-hex-sha",
  "task_packet_sha256": "64-hex-sha256",
  "candidate": {
    "model": "...",
    "provider": "...",
    "harness": "..."
  },
  "started_at": "...",
  "completed_at": "...",
  "status": "complete|contaminated|aborted"
}
```

## `ACCESS_ATTESTATION.json`

Record every intentional repository/source family read during the candidate run and explicitly state whether the forbidden reference project was accessed. Primary runs must state that live web/GitHub search outside PAM was not used.

## `PROJECT_ASSURANCE.json`

Produce a project-specific PAM manifest pinned to the frozen PAM revision. Route modules based on the task packet, not on a desire to maximize checklist count. Requirements not yet executable may remain `pending`; inappropriate modules must use justified `not_applicable`/defer state rather than silent omission.

## `RESEARCH_HANDOFF.md`

Condense the supplied research into project-operational context:

- problem/outcome;
- assumptions being promoted into project planning;
- evidence/candidate-system context;
- unresolved questions;
- constraints/non-goals;
- important alternatives already considered.

Do not invent finished-project facts.

## `BUILD_VS_REUSE.md`

For each material subsystem/capability, record serious existing options from the supplied research, comparison criteria, whether a cheap empirical probe should precede a bespoke implementation, and one disposition:

```text
reuse | configure | wrap | extend | compose | fork | build_new | more_research
```

A `build_new` disposition must earn itself with unmet scoped requirements.

## `SCOPE.md`

State current goals/claims, explicit non-goals, assurance horizon, deferred/rejected mechanisms with reconsideration triggers, repository/component boundaries, and the rule for admitting new scope.

## `PROJECT_PLAN.md`

Produce a phased/milestoned plan. Each phase should state:

- objective;
- scoped claim/capability;
- dependencies/entry criteria;
- required evidence/validation;
- exit gate;
- explicit non-scope where useful.

Do not make later speculative mechanisms prerequisites for the first vertical slice without evidence.

## `REPOSITORY_MAP.md`

State whether the program should be one repository or multiple independently versioned repositories and why. For each proposed repository/component, define ownership and must-not-own boundaries. Distinguish runtime dependencies from CI/research-only systems and bounded experiments.

## `ISSUE_PLAN.yaml`

Describe the issue hierarchy without creating live issues. Each executable issue entry should include at least:

```yaml
id: proposed-stable-id
repository: proposed-owner
parent: optional-parent-id
objective: ...
acceptance_evidence:
  - ...
blocked_by:
  - ...
out_of_scope:
  - ...
```

Issue numbers are not scored. Material ownership, dependency, and closure semantics are.

## `VALIDATION_PLAN.md`

Map claims/failure surfaces to validation classes. Include applicable deterministic, negative/fail-closed, contract/integration, property/state-machine, metamorphic, mutation, fault/adversarial, benchmark/dataset/holdout, composition/ablation, reproducibility, cost/friction, and residual-risk evidence. Explicitly justify non-applicable techniques.

## `HANDOFF_STATE.json`

Provide a structured resumable checkpoint containing at least current phase, current proposed work unit, unresolved blockers, validation status, exact next action, scope exclusions, and methodology revision. It need not reproduce Research Assurance's eventual handoff schema byte-for-byte.

## `PAM_GAPS.md`

Record only shortcomings in PAM that made planning ambiguous or unnecessarily difficult. Do not edit PAM during the benchmark to fix them. This file may be empty except for `No material gaps observed.`

## Freeze rule

Once `completed_at` is written and status is `complete`, candidate files are frozen for evaluation. Any later change constitutes a new run ID.
