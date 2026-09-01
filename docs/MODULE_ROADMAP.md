# Module roadmap

This is a candidate extraction map, not a promise that every module will be implemented or applicable to every project.

The main source for v0 candidates is the process developed manually in `Pukujan/research-assurance`.

| Family | Candidate module | Status | Typical applicability |
| --- | --- | --- | --- |
| Projectization | `projectization.build-vs-reuse` | **implemented candidate 0.1.0** | nontrivial software projectization where maintained existing systems may satisfy the need |
| Projectization | `projectization.scope-boundary` | **implemented candidate 0.1.0** | nontrivial projects where horizontal expansion or premature subsystem creation is a material risk |
| Projectization | `projectization.research-handoff` | planned | research-heavy projects needing a compact promotion boundary from exploration into engineering |
| Projectization | `projectization.preflight-freeze` | planned | projects that should freeze routed methodology before repository/issue/bootstrap generation |
| Planning | `planning.product-definition` | planned | nontrivial projects with explicit goals/non-goals/success criteria |
| Planning | `planning.system-design` | planned | projects with architectural boundaries/interfaces/state |
| Planning | `planning.invariants` | planned | systems making durable correctness claims |
| Planning | `planning.failure-register` | planned | systems with meaningful failure surface |
| Planning | `planning.scope-control` | superseded for v0 projectization | deeper milestone/runtime scope-control after the initial `projectization.scope-boundary` |
| Engineering | `engineering.swe-foundation.python` | planned | Python software projects |
| Engineering | `engineering.swe-foundation.typescript` | planned | TypeScript software projects |
| Engineering | `engineering.ci-foundation` | planned | software with automated repository gates |
| Engineering | `engineering.static-quality` | planned | lint/format/type/static checks appropriate to ecosystem |
| Validation | `validation.unit-contract-integration` | planned | most software systems |
| Validation | `validation.property-state-machine` | planned | stateful systems with generatable transitions |
| Validation | `validation.metamorphic-testing` | planned | behavior with known relation-preserving transformations |
| Validation | `validation.mutation-testing` | planned | critical deterministic logic where test sensitivity matters |
| Validation | `validation.fault-injection` | planned | persistence, network, distributed, crash/recovery boundaries |
| Validation | `validation.adversarial-review` | planned | systems making consequential/fallible assurance claims |
| Benchmark | `benchmark.protocol` | planned | empirical quality/performance claims |
| Benchmark | `benchmark.hidden-holdout` | planned | adaptive/model systems where contamination/tuning threatens validity |
| Benchmark | `benchmark.ablation` | planned | layered/compositional systems claiming incremental value |
| Benchmark | `benchmark.statistical-reporting` | planned | stochastic/empirical systems |
| Governance | `governance.github-issues` | planned | work requiring durable issue-level execution contracts |
| Governance | `governance.github-project-tracking` | planned | multi-stream/multi-repo programs; not tiny repos by default |
| Governance | `governance.multi-repo-coordination` | planned | superprojects/component portfolios |
| Continuity | `continuity.structured-handoff` | **implemented candidate 0.1.0** | multi-session/agent/harness work |
| Provenance | `provenance.fossil-decision-lineage` | planned | substantial research/design lineage worth replaying |
| Provenance | `provenance.exact-versioning` | planned | projects where artifact/component identity matters |
| Research | `research.external-precedent-reuse` | folded into projectization for v0 | deeper external-methodology discovery beyond the initial build-vs-reuse gate |
| Research | `research.dataset-selection` | planned | projects with external benchmark/dataset claims |
| Release | `release.evidence-gate` | planned | releases/milestones requiring exact closure evidence |
| Release | `release.migration-replay-rollback` | planned | persistent/stateful systems with upgrades |
| Security | `security.threat-model` | planned | projects crossing trust/security boundaries |
| Security | `security.authorization-negative-tests` | planned | systems with authorization or tenant/data isolation |

## Extraction priority

Do not implement this table top-to-bottom mechanically.

Priority should come from:

1. repeated need across real projects;
2. availability of a clear external or project precedent;
3. ability to define objective closure evidence;
4. risk/benefit of omission;
5. usefulness to the next adopter.

The first implemented cluster is deliberately small:

```text
projectization.build-vs-reuse
projectization.scope-boundary
continuity.structured-handoff
```

These address three high-cost repeated failures observed during Research Assurance work: agents building before testing reuse, horizontal scope expansion, and loss of execution state across sessions/harnesses.

The next extraction cluster should be chosen from evidence produced by the first two adopters and the blinded retrospective benchmark, not copied mechanically from Research Assurance. Likely candidates remain:

```text
projectization.research-handoff
projectization.preflight-freeze
product-definition
system-design
invariants + failure-register
SWE/CI foundation
validation-strategy router
benchmark-integrity / hidden-holdout
adversarial-review
GitHub issue/project planning
FOSSIL decision-lineage
```

Each should get its own portable module contract rather than becoming one giant checklist.
