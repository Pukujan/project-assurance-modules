# Module roadmap

This is a candidate extraction map, not a promise that every module will be implemented or applicable to every project.

The main source for v0 candidates is the process developed manually in `Pukujan/research-assurance`.

| Family | Candidate module | Status | Typical applicability |
| --- | --- | --- | --- |
| Planning | `planning.product-definition` | planned | nontrivial projects with explicit goals/non-goals/success criteria |
| Planning | `planning.system-design` | planned | projects with architectural boundaries/interfaces/state |
| Planning | `planning.invariants` | planned | systems making durable correctness claims |
| Planning | `planning.failure-register` | planned | systems with meaningful failure surface |
| Planning | `planning.scope-control` | planned | research/assurance/meta systems prone to horizontal expansion |
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
| Research | `research.external-precedent-reuse` | planned | projects that should test build-vs-reuse / standards / OSS precedent |
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

The first extraction is structured handoff because it is currently needed in both Research Assurance and RA-plugin and has a clear machine-valid contract.

Likely next extraction cluster from Research Assurance:

```text
product-definition
system-design
invariants + failure-register
SWE/CI foundation
validation-strategy router
benchmark-integrity / hidden-holdout
scope-control + adversarial-review
GitHub issue/project planning
FOSSIL decision-lineage
```

Each should get its own module contract rather than becoming one giant checklist.
