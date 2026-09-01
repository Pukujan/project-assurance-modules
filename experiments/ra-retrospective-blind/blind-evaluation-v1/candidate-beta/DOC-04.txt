# Project plan

All implementation work below is **proposed**. Entry into implementation requires project-owner review of `PROJECT_ASSURANCE.json`, `BUILD_VS_REUSE.md`, and `SCOPE.md`. The first vertical slice deliberately avoids making speculative mechanisms prerequisites.

## Milestone M0 — contract and engineering foundation

**Objective**

Freeze the product/system contract and establish a deterministic engineering substrate for the thin coordinator.

**Scoped capability/claim**

The project can state exactly what a promotion is, what the coordinator owns, which states/transitions exist, which evidence dimensions remain separate, and what must fail closed.

**Dependencies / entry criteria**

- project-owner approval of preflight dispositions;
- proposed new coordinator repository authorized;
- exact candidate revisions of existing systems resolved for probing (not yet necessarily admitted as dependencies);
- implementation language/tooling selected with deterministic local checks.

**Required evidence/validation**

- committed PDD and SDD;
- explicit invariants and failure-mode register;
- machine-valid evidence/promotion/replay schemas;
- no-network PR check lane where feasible: formatting/lint, strict typing/static checks, unit/contract tests, schema validation;
- negative fixtures for forbidden universal verification state, missing required evidence, unresolved/stale identity, invalid transition, unauthorized review/promotion;
- exact dependency/component manifest format;
- structured handoff schema/policy design.

**Exit gate**

M0 closes only when the normal deterministic check lane is green from a clean environment and objective test/schema evidence exists for the contract. No stochastic model or benchmark quality claim is required to close M0.

**Non-scope**

FOSSIL behavior claims, retrieval quality, Source Ranker benefit, semantic claim verification, graph retrieval, and harness plugins.

## Milestone M1 — deterministic promotion vertical slice

**Objective**

Implement the smallest fail-closed promotion coordinator and compose it with pinned FOSSIL Core plus the financial application contract.

**Scoped capability/claim**

A finance workflow can propose a consequential promotion; exploration can continue on assurance failure; acceptance cannot occur unless required deterministic/evidence/reference/review conditions are satisfied; accepted state carries exact replay identity.

**Dependencies / entry criteria**

- M0 green;
- exact FOSSIL and financial-application candidate revisions pinned;
- FOSSIL candidate contract/integrity probe plan approved;
- application contract defines exact source/time/version/restatement/numeric identities needed by the slice.

**Required evidence/validation**

- FOSSIL contract tests for referenced capabilities;
- corruption, failed-ingest/orphan, crash/partial-batch, retry/idempotency, actor attribution, review-reference authority, redaction/rebuild/replay tests where applicable to the relied-on contract;
- deterministic finance wrong-version/restatement/as-of-time/evidence-root/numeric corruption fixtures;
- coordinator state-machine/property tests;
- integration tests proving promotion failure does not forge accepted state and does not require exploratory work to terminate;
- replay descriptor round-trip and exact revision/dataset/config identity tests;
- human review binding to an exact claim/evidence/revision tuple where judgment is required.

**Exit gate**

A fully local fixture demonstrates proposal -> evidence assembly -> review (when required) -> accepted/rejected behavior with fail-closed negative cases and replay metadata. FOSSIL properties are claimed only to the extent supported by current test evidence.

**Non-scope**

Source Ranker runtime inclusion, retrieval-quality improvement claims, semantic claim-verification claims, graph retrieval, cross-domain packs.

## Milestone M2 — empirical evaluation and layer separation

**Objective**

Add evaluation evidence without turning evaluation infrastructure into a production dependency or collapsing quality dimensions.

**Scoped capability/claim**

The program can measure retrieval behavior and first-domain task behavior on immutable public development material; reports remain layer-specific and reproducible. Optional Source Ranker value can be measured independently.

**Dependencies / entry criteria**

- M1 deterministic core green;
- exact Retrieval Benchmarker revision pinned and compatibility fixture passes;
- selected public development datasets have manifests, licenses/usage constraints, hashes/versions, and task-specific metric definitions;
- hidden confirmatory material is already access-separated before adaptive tuning begins.

**Required evidence/validation**

- Retrieval Benchmarker persisted rankings/reports on a bounded finance retrieval task (FinanceBench/FinQA/TAT-QA subsets as justified);
- deterministic mechanically generated SEC temporal/version/restatement/wrong-version cases kept separate from stochastic quality scores;
- per-layer benchmark reports: retrieval, optional source ranking, citation/grounding or semantic task only if specifically admitted;
- baselines plus composition tests and layer ablations;
- repeated-run/reproducibility evidence with exact dataset/config/component identities;
- Source Ranker probe only if the predeclared metric/task makes it a serious candidate; allow `NO_MEASURABLE_BENEFIT`.

**Exit gate**

Public development results are reproducible and interpretable per layer; no universal score is produced; every admitted mechanism has a baseline and kill/defer criterion.

**Non-scope**

Hidden confirmatory results as a tuning loop; universal cross-domain claims.

## Milestone M3 — confirmatory, adversarial, and release evidence

**Objective**

Test the first-slice claims under contamination-resistant confirmation and adversarial failure review, then freeze a release evidence bundle if warranted.

**Scoped capability/claim**

A specific pinned composition satisfies the declared first-slice promotion/replay/finance/evaluation claims with explicit residual risk.

**Dependencies / entry criteria**

- M2 public-development work frozen for the confirmatory candidate;
- hidden evaluator material remains unavailable to implementation agents;
- release candidate pins all component revisions, policies, datasets, and configs.

**Required evidence/validation**

- hidden confirmatory evaluation run by a separated evaluator/harness;
- negative evidence that hidden labels/answers/seeds are absent from implementation-agent handoffs and fixtures;
- adversarial review distinct from the implementation validation lane: stale refs, forged receipts, bypass attempts, wrong actor, replay mismatch, partial failure, leaked holdout, misleading aggregate metrics;
- mutation testing of critical deterministic gate conditions;
- residual-risk register with accepted/deferred/unresolved risks and human approval where judgment is inherent;
- frozen release/replay manifest linking exact CI, benchmark, component, dataset, and evidence identities.

**Exit gate**

Either (a) evidence supports the bounded release claims and a reviewed release bundle is frozen, or (b) the release claim is narrowed/blocked with objective failure evidence. Failure is an allowed outcome.

## Milestone M4 — optional mechanism experiments

No M4 item is a prerequisite for M0–M3.

### M4A Source Ranker admission

Run only if M2 identifies a concrete source-suitability gap. Compare against a simpler policy baseline. Admit only for measurable incremental benefit with acceptable cost/friction; otherwise record `NO_MEASURABLE_BENEFIT` and keep it out of runtime scope.

### M4B Claim-verification experiment

Run only after a specific semantic-support task, dataset/gold policy, baseline, and hidden-confirmation plan are approved. It cannot be used to retroactively make provenance/retrieval evidence mean semantic correctness.

### M4C Graph retrieval experiment

Run only if a scoped retrieval failure survives simpler methods. Require graph-layer ablation; graph/vector state remains a rebuildable projection.

### M4D Agent/HITL continuity experiment

Phase 1: frozen local microworld, deterministic state/restart/idempotency/review-binding tests, zero model spend.

Phase 2: only if Phase 1 is green, forced interruption/restart and cross-model/harness handoff experiment with predeclared success metric plus protocol-induced failure/friction metric. `NO_MEASURABLE_BENEFIT` ends the experiment without changing core architecture.

## Structured handoff policy for the program

A material handoff is required when responsibility transfers across sessions/agents/harnesses/repositories or when work pauses with nontrivial blockers/validation state. It is not required after every trivial action.

The current handoff must include exact coordinator revision, active issue/work unit, referenced child repository revisions/PRs when any, validation status, unresolved blockers, next action, scope exclusions, and methodology revision. On resume, the worker reconciles the small referenced live set (repository SHAs, active issue/PR, relevant CI/result identity) before mutation. Live state wins over a stale handoff; inconsistency blocks mutation until reconciled.

Current state is replaceable. Material milestone/release checkpoints are immutable or append-only evidence bundles. Hidden confirmatory labels/answers/seeds are forbidden from agent-visible handoffs.
