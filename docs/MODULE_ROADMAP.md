# Module roadmap

This is a candidate extraction map, not a promise that every module will be implemented or applicable to every project.

The original source for v0 candidates was the process developed manually in `Pukujan/research-assurance`. The v0.2 bounded cluster below was selected only after the frozen RA retrospective repeatedly demonstrated the same missing obligations.

| Family | Candidate module | Status | Typical applicability |
| --- | --- | --- | --- |
| Projectization | `projectization.build-vs-reuse` | **implemented candidate 0.1.0** | nontrivial software projectization where maintained existing systems may satisfy the need |
| Projectization | `projectization.scope-boundary` | **implemented candidate 0.1.0** | nontrivial projects where horizontal expansion or premature subsystem creation is a material risk |
| Projectization | `projectization.research-handoff` | planned | research-heavy projects needing a compact promotion boundary from exploration into engineering |
| Projectization | `projectization.preflight-freeze` | planned | projects that should freeze routed methodology before repository/issue/bootstrap generation |
| Planning | `planning.foundation` | **implemented candidate 0.1.0** | nontrivial projectization needing product definition, system design, invariants, and a failure register |
| Planning | `planning.product-definition` | folded into `planning.foundation` for v0.2 | may be split later only if independent applicability is demonstrated |
| Planning | `planning.system-design` | folded into `planning.foundation` for v0.2 | may be split later only if independent applicability is demonstrated |
| Planning | `planning.invariants` | folded into `planning.foundation` for v0.2 | may be split later only if independent applicability is demonstrated |
| Planning | `planning.failure-register` | folded into `planning.foundation` for v0.2 | may be split later only if independent applicability is demonstrated |
| Planning | `planning.scope-control` | superseded for v0 projectization | deeper milestone/runtime scope-control after the initial `projectization.scope-boundary` |
| Engineering | `engineering.swe-ci-foundation` | **implemented candidate 0.1.0** | maintained software needing reproducible local checks and automated repository gates |
| Engineering | `engineering.swe-foundation.python` | folded into generic foundation for v0.2 | language-specific extraction requires separate repeated evidence |
| Engineering | `engineering.swe-foundation.typescript` | folded into generic foundation for v0.2 | language-specific extraction requires separate repeated evidence |
| Engineering | `engineering.ci-foundation` | folded into `engineering.swe-ci-foundation` for v0.2 | generic CI obligation is currently coupled to the software foundation |
| Engineering | `engineering.static-quality` | folded into `engineering.swe-ci-foundation` for v0.2 | ecosystem-specific checks remain project-selected |
| Validation | `validation.unit-contract-integration` | planned | most software systems |
| Validation | `validation.property-state-machine` | planned | stateful systems with generatable transitions |
| Validation | `validation.metamorphic-testing` | planned | behavior with known relation-preserving transformations |
| Validation | `validation.mutation-testing` | planned | critical deterministic logic where test sensitivity matters |
| Validation | `validation.fault-injection` | planned | persistence, network, distributed, crash/recovery boundaries |
| Validation | `validation.adversarial-review` | planned | systems making consequential/fallible assurance claims |
| Benchmark | `benchmark.integrity` | **implemented candidate 0.1.0** | empirical claims or benchmark/dataset/hidden-evaluation boundaries |
| Benchmark | `benchmark.protocol` | folded into `benchmark.integrity` for v0.2 | split only if protocol selection needs independent routing |
| Benchmark | `benchmark.hidden-holdout` | folded into `benchmark.integrity` for v0.2 | requirement may be N/A when contamination risk is absent |
| Benchmark | `benchmark.ablation` | planned | layered/compositional systems claiming incremental value |
| Benchmark | `benchmark.statistical-reporting` | planned | stochastic/empirical systems |
| Governance | `governance.github-issues` | planned | work requiring durable issue-level execution contracts |
| Governance | `governance.github-project-tracking` | planned | multi-stream/multi-repo programs; not tiny repos by default |
| Governance | `governance.multi-repo-coordination` | planned | superprojects/component portfolios |
| Continuity | `continuity.structured-handoff` | **implemented candidate 0.1.0** | multi-session/agent/harness work |
| Provenance | `provenance.decision-lineage` | **implemented candidate 0.1.0** | consequential or replay-worthy project/design/evidence decisions |
| Provenance | `provenance.fossil-decision-lineage` | folded into generic boundary for v0.2 | FOSSIL remains optional; a storage-specific module requires separate need |
| Provenance | `provenance.exact-versioning` | planned | projects where artifact/component identity matters beyond existing contracts |
| Research | `research.external-precedent-reuse` | folded into projectization for v0 | deeper external-methodology discovery beyond the initial build-vs-reuse gate |
| Research | `research.dataset-selection` | folded into `benchmark.integrity` for v0.2 | dataset identity/admission is part of the current benchmark boundary |
| Release | `release.evidence-gate` | planned | releases/milestones requiring exact closure evidence |
| Release | `release.migration-replay-rollback` | planned | persistent/stateful systems with upgrades |
| Security | `security.threat-model` | planned | projects crossing trust/security boundaries |
| Security | `security.authorization-negative-tests` | planned | systems with authorization or tenant/data isolation |

## Extraction priority

Do not implement this table top-to-bottom mechanically.

Priority comes from:

1. repeated need across real projects;
2. availability of a clear external or project precedent;
3. ability to define objective closure evidence;
4. risk/benefit of omission;
5. usefulness to the next adopter.

The frozen v0 cluster remains:

```text
projectization.build-vs-reuse
projectization.scope-boundary
continuity.structured-handoff
```

The bounded v0.2 cluster selected after the retrospective is:

```text
planning.foundation
engineering.swe-ci-foundation
benchmark.integrity
provenance.decision-lineage
```

Each v0.2 module uses `pam-module/0.2.0` metadata to record motivating precedent/failure, explicit conflicts, and compatibility impact while keeping its own independently versioned module identity at `0.1.0`.

Further extraction is blocked on evidence from the second adopter and later unseen-project work. Do not continue down the roadmap merely because candidate names remain.
