# Executable work decomposition

This issue plan is organized as milestones with parent epics and implementation-ready child issues. Issue numbers are intentionally not assigned; create them in tracker order while preserving the dependency graph below.

## Milestone 0 — Scope, contracts, and reproducibility foundation

### Epic M0-E1 — Define the protected promotion model

#### M0-1 — Write problem/scope specification
**Goal:** Define exactly what the project assures and what remains exploratory.

**Deliverables**
- `docs/problem-and-scope.md`
- promotion kinds and protected transition definitions
- explicit non-goals and first-domain boundary

**Acceptance criteria**
- Exploration is allowed after failed assurance checks.
- Accepted/reviewed promotion cannot be silently bypassed.
- The document explicitly rejects a universal agent-control layer and universal `verified=true` semantics.
- Finance is identified as the first domain without claiming cross-domain transfer.

**Depends on:** none

#### M0-2 — Define dimension-specific assurance result model
**Goal:** Separate provenance, citation, temporal, numeric, retrieval, semantic, authorization, review, and source-related judgments.

**Deliverables**
- `docs/assurance-model.md`
- dimension vocabulary and status semantics
- applicability rules

**Acceptance criteria**
- No aggregate score/flag can imply one dimension proves another.
- `not_applicable`, `not_run`, success, and failure states are distinguishable.
- Source authority/quality and claim/source suitability are separate concepts.
- Retrieval correctness and claim correctness are separate concepts.

**Depends on:** M0-1

#### M0-3 — Specify promotion state machine and authorization invariants
**Goal:** Define legal and illegal transitions for candidate, assessed, reviewed, accepted, rejected-for-promotion, and superseded state.

**Deliverables**
- `docs/promotion-state-machine.md`
- transition table
- authorization requirements
- supersession/review invalidation rules

**Acceptance criteria**
- Failed gates cannot produce `ACCEPTED`.
- Changed candidate/evidence identities invalidate prior review binding unless explicitly superseded/re-reviewed.
- Research artifacts remain available after rejection for promotion.
- Illegal transition examples are enumerated for later property tests.

**Depends on:** M0-1, M0-2

### Epic M0-E2 — Define receipts, evidence references, and replay identity

#### M0-4 — Design evidence-reference schema
**Goal:** Represent durable evidence identity without making rebuildable indexes authoritative.

**Deliverables**
- `schemas/evidence-reference.schema.json`
- examples for source snapshot, exact citation/span, version/timestamp, digest

**Acceptance criteria**
- References can distinguish source identity from index/projection identity.
- Exact citation/span/version identity is representable.
- Mutable upstream references require durable snapshot/content identity before accepted promotion.

**Depends on:** M0-2

#### M0-5 — Design promotion-receipt schema
**Goal:** Capture an append-only record of attempted/completed protected transitions.

**Deliverables**
- `schemas/promotion-receipt.schema.json`
- valid and invalid examples

**Acceptance criteria**
- Receipt binds exact candidate, evidence, policy version, check results, actor, review, and disposition.
- Check implementation/config/version identity is preserved.
- Receipt semantics do not assert universal truth.
- Schema supports replay and supersession references.

**Depends on:** M0-3, M0-4

#### M0-6 — Define reproducibility manifest schema
**Goal:** Preserve exact composition and evaluation identity.

**Deliverables**
- `schemas/dataset-manifest.schema.json`
- component/environment/run manifest specification

**Acceptance criteria**
- Component commits/digests, dataset/corpus/query/qrel identity, dependency lock, model/configuration, seeds, outputs, and policy/schema versions are representable where applicable.
- Hidden confirmatory run identity can be recorded without exposing hidden material to implementers.

**Depends on:** none

### Epic M0-E3 — Define finance policy and evaluation split

#### M0-7 — Specify first finance promotion scenario
**Goal:** Select one consequential conclusion workflow using versioned SEC/financial evidence.

**Deliverables**
- scenario narrative
- required evidence types
- expected promotion path
- negative-case matrix

**Acceptance criteria**
- Includes correct case plus wrong-version, stale/restated, numeric corruption, citation corruption, evidence-root mismatch, and unauthorized promotion cases.
- Required human review points are explicit.
- Scenario is small enough for deterministic end-to-end tests.

**Depends on:** M0-1, M0-3

#### M0-8 — Write finance assurance policy v0
**Goal:** Define deterministic authority/temporal/version/numeric rules for the first scenario.

**Deliverables**
- `docs/finance-policy.md`
- policy version identifier
- human-review threshold rules

**Acceptance criteria**
- Deterministic rules are preferred where available.
- Policy distinguishes source authority from claim suitability.
- Restatement/version semantics are explicit.
- The policy does not claim applicability to legal, medical, or other domains.

**Depends on:** M0-7

#### M0-9 — Define public development and hidden confirmatory evaluation protocol
**Goal:** Prevent adaptive contamination of confirmatory evidence.

**Deliverables**
- evaluation protocol
- access separation rules
- freeze/run-manifest procedure

**Acceptance criteria**
- Public development data may be inspected during implementation.
- Hidden material is inaccessible until implementation/config is frozen.
- Confirmatory runs preserve exact tested composition identity.
- Same-run tuning after hidden results is prohibited.

**Depends on:** M0-6

### Epic M0-E4 — Build failure-mode register and adapter contracts

#### M0-10 — Create failure-mode register
**Goal:** Convert research concerns into owned, testable hypotheses.

**Deliverables**
- `docs/failure-modes.md`
- severity, owner, detection, mitigation, residual risk fields

**Acceptance criteria**
- Includes evidence mismatch, wrong citation/version, stale/restated evidence, numeric error, source-suitability mismatch, retrieval incompleteness, semantic overclaim, stale review binding, unauthorized promotion, ingest orphaning, crash/partial batch, projection/source divergence, hidden-data leakage, and protocol-induced blocking.

**Depends on:** M0-1 through M0-9 as relevant

#### M0-11 — Define FOSSIL Core adapter contract and boundary probes
**Goal:** Specify only the provenance behaviors this project needs, then test them empirically.

**Deliverables**
- adapter interface contract
- probe plan for whole-artifact integrity, review-reference authority, orphan storage, crash/partial batch, caller/service attribution, and provenance binding of role/quality metadata

**Acceptance criteria**
- No untested FOSSIL behavior is treated as guaranteed.
- Each probe has pass/fail consequences and workaround/stop criteria.

**Depends on:** M0-4, M0-5, M0-10

#### M0-12 — Define Source Ranker adapter contract and empirical boundary
**Goal:** Prevent assumed capabilities from becoming mandatory assurance.

**Deliverables**
- narrow adapter interface
- target failure modes
- benchmark requirements and kill criteria

**Acceptance criteria**
- Ranker output cannot replace deterministic source-policy rules without evidence.
- Source quality and claim/source suitability remain separately observable.
- No-benefit outcome permits omission from mandatory promotion.

**Depends on:** M0-2, M0-8, M0-10

#### M0-13 — Define Retrieval Benchmarker integration contract
**Goal:** Reuse existing retrieval evaluation rather than rebuilding it.

**Deliverables**
- runner/manifest interface
- persisted ranking/report requirements
- dataset mapping

**Acceptance criteria**
- Immutable corpora/queries/qrels and retrieval configuration identity are preserved.
- Retrieval metrics are reported separately from semantic assurance.

**Depends on:** M0-6, M0-10

---

## Milestone 1 — Deterministic promotion substrate and FOSSIL boundary proof

### Epic M1-E1 — Implement core transition and receipt logic

#### M1-1 — Implement assurance dimension/result primitives
**Acceptance criteria**
- Applicable dimensions can be recorded independently.
- No universal verification Boolean is introduced.
- Serialization round-trips deterministically.

**Depends on:** M0-2, M0-5

#### M1-2 — Implement promotion state machine
**Acceptance criteria**
- Legal transitions succeed; illegal transitions fail closed for protected promotion.
- Rejection does not delete/block exploratory artifact state.
- Supersession is explicit and auditable.

**Depends on:** M0-3, M1-1

#### M1-3 — Implement receipt creation and replay primitives
**Acceptance criteria**
- Receipt binds exact candidate/evidence/policy/check/review identities.
- Replay can re-evaluate deterministic checks from frozen fixtures.
- Changed input identity is detected, not silently accepted.

**Depends on:** M0-5, M0-6, M1-2

### Epic M1-E2 — Implement deterministic gates

#### M1-4 — Implement identity and integrity checks
**Acceptance criteria**
- Candidate/evidence digests are verified.
- Corruption cases fail deterministically.

**Depends on:** M0-4, M1-3

#### M1-5 — Implement exact citation checks
**Acceptance criteria**
- Missing/out-of-bounds/wrong-version citation references fail.
- Citation check does not claim semantic support.

**Depends on:** M0-4, M1-3

#### M1-6 — Implement temporal/version checks for finance policy
**Acceptance criteria**
- Stale, wrong-version, and restated evidence cases are detected according to finance policy.
- Policy/version identity is included in results.

**Depends on:** M0-8, M1-3

#### M1-7 — Implement deterministic numeric checks
**Acceptance criteria**
- Defined finance calculations/reconciliations are reproducible.
- Mutated formulas or corrupted inputs cause test failures.

**Depends on:** M0-8, M1-3

#### M1-8 — Implement actor/authorization checks
**Acceptance criteria**
- Unauthorized callers cannot produce accepted promotion.
- Actor/service identity is recorded in receipt.

**Depends on:** M0-3, M1-3

### Epic M1-E3 — Prove FOSSIL boundary behavior

#### M1-9 — Implement FOSSIL adapter
**Acceptance criteria**
- Adapter exposes only contractually required provenance/storage operations.
- Tests use pinned FOSSIL composition identity.

**Depends on:** M0-11

#### M1-10 — Run FOSSIL integrity and review-authority probes
**Acceptance criteria**
- Whole-artifact verification and review-reference authority are empirically characterized.
- Findings are recorded as pass, workaround-required, or blocker.

**Depends on:** M1-9

#### M1-11 — Run ingest/crash/partial-batch/orphan probes
**Acceptance criteria**
- Failed ingest, crash, retry, and partial-batch behavior are characterized.
- No tested path can forge accepted promotion history.

**Depends on:** M1-9

#### M1-12 — Run actor/metadata provenance-binding probes
**Acceptance criteria**
- Caller/service attribution behavior is characterized.
- Required role/quality metadata either has sufficient provenance binding or receives an explicit mitigation.

**Depends on:** M1-9

### Epic M1-E4 — Deterministic verification hardening

#### M1-13 — Add state-machine/property tests
**Acceptance criteria**
- Generated transition sequences cannot bypass required gates/review.
- Review invalidation on identity change is covered.

**Depends on:** M1-2, M1-3

#### M1-14 — Add mutation tests for critical gates
**Acceptance criteria**
- Mutations that weaken identity, citation, temporal, numeric, or authorization gates are killed at an agreed threshold.
- Surviving critical mutants are triaged as test gaps or accepted residual risk.

**Depends on:** M1-4 through M1-8

#### M1-15 — Add fault/crash/replay/rebuild suite
**Acceptance criteria**
- Persistent-boundary failure scenarios do not create forged accepted state.
- Replay/rebuild from durable authority recovers expected state for scoped cases.

**Depends on:** M1-3, M1-9 through M1-12

---

## Milestone 2 — Finance end-to-end vertical slice

### Epic M2-E1 — Integrate the finance application

#### M2-1 — Add finance-app assurance integration boundary
**Acceptance criteria**
- Application can submit a candidate promotion with exact evidence references.
- Assurance core remains application/transport-neutral.

**Depends on:** M1-3, M1-9, M0-8

#### M2-2 — Implement human review binding
**Acceptance criteria**
- Review approval binds to exact candidate/evidence/policy identities.
- Any bound identity change requires new review or explicit supersession.
- Reviewer action is recorded without requiring review for trivial actions.

**Depends on:** M1-3, M2-1

#### M2-3 — Implement end-to-end accepted promotion path
**Acceptance criteria**
- Correct finance case reaches `ACCEPTED` only after all policy-required checks/review.
- Receipt contains sufficient replay identity.

**Depends on:** M1-4 through M1-8, M2-1, M2-2

#### M2-4 — Implement end-to-end rejection-with-continued-exploration path
**Acceptance criteria**
- Each deterministic negative case is rejected for promotion.
- Underlying research remains accessible/editable for continued work.
- No accepted receipt is forged.

**Depends on:** M2-3

#### M2-5 — Implement restatement/supersession scenario
**Acceptance criteria**
- New/restated evidence can supersede prior accepted state explicitly.
- Prior accepted state remains auditable.
- New review is required when policy says the changed evidence/candidate invalidates prior review.

**Depends on:** M2-3

#### M2-6 — Produce reproducibility bundle for finance slice
**Acceptance criteria**
- Fresh environment can replay the deterministic assessment from documented identities and fixtures.
- Bundle records all relevant component, policy, schema, dataset/evidence, and environment versions.

**Depends on:** M2-3, M2-4, M2-5

---

## Milestone 3 — Empirical retrieval, source, and semantic layers

### Epic M3-E1 — Retrieval evaluation

#### M3-1 — Establish retrieval baselines
**Acceptance criteria**
- Run appropriate TREC/BEIR and/or finance retrieval datasets through existing Retrieval Benchmarker.
- Record sparse/dense/hybrid/rerank configurations and immutable rankings/reports.
- Report retrieval metrics independently.

**Depends on:** M0-13, M0-6

#### M3-2 — Evaluate retrieval composition against finance target errors
**Acceptance criteria**
- Identify whether retrieval changes reduce the target evidence-missing/incomplete failure modes.
- Cost/latency and regressions are recorded.

**Depends on:** M3-1, M2-6

### Epic M3-E2 — Source ranking/suitability evaluation

#### M3-3 — Benchmark Source Ranker for scoped finance tasks
**Acceptance criteria**
- Evaluate source authority/quality and claim/source suitability separately where possible.
- Compare to deterministic/domain-policy baseline.
- Record no-benefit outcome if threshold is not met.

**Depends on:** M0-12, M2-6

#### M3-4 — Decide Source Ranker promotion role
**Acceptance criteria**
- Decision is one of mandatory, advisory, experiment-only, or omitted.
- Decision references measured benefit, failure modes, cost, and residual risk.

**Depends on:** M3-3

### Epic M3-E3 — Semantic/grounding evaluation

#### M3-5 — Establish simple semantic-support baseline
**Acceptance criteria**
- Use a minimal existing/simple approach before building bespoke infrastructure.
- Evaluate on selected public claim/evidence datasets and finance-specific cases.
- Report support/refute/insufficiency or grounding metrics separately by dataset.

**Depends on:** M2-6

#### M3-6 — Evaluate unsupported-grounding/citation behavior
**Acceptance criteria**
- Use appropriate grounding/citation datasets such as RAGTruth/ALCE where they fit the target error class.
- Do not conflate citation identity with semantic support.

**Depends on:** M3-5

#### M3-7 — Run composition/ablation study
**Acceptance criteria**
- Compare deterministic-only baseline with retrieval/source/semantic additions individually and in candidate composition.
- Identify mandatory, optional, and rejected layers.
- Any graph/ontology proposal remains deferred unless this study exposes a defined unmet failure mode.

**Depends on:** M3-2, M3-4, M3-5, M3-6

---

## Milestone 4 — Adversarial and confirmatory evaluation

### Epic M4-E1 — Adversarial assurance review

#### M4-1 — Build adversarial campaign from failure-mode register
**Acceptance criteria**
- Campaign targets protected-transition bypass, stale review, wrong evidence/version, projection/source divergence, corruption, retries/recovery, and protocol edge cases.
- Findings are distinguished from ordinary validation failures.

**Depends on:** M0-10, M2-6, M3-7

#### M4-2 — Close or accept adversarial findings
**Acceptance criteria**
- Each finding has fix, mitigation, residual-risk acceptance, or explicit scope exclusion.
- Findings do not automatically broaden project scope.

**Depends on:** M4-1

### Epic M4-E2 — Hidden confirmatory evaluation

#### M4-3 — Freeze implementation/configuration for confirmatory run
**Acceptance criteria**
- Exact component commits/digests, environment, policies, schemas, model/configuration, and seeds are recorded before hidden material is accessed.

**Depends on:** M3-7, M4-2

#### M4-4 — Execute hidden confirmatory evaluation
**Acceptance criteria**
- Hidden material remains unavailable to implementation agents before freeze.
- Results are preserved per dimension/dataset without universal aggregation.
- No same-run tuning occurs after results are observed.

**Depends on:** M4-3

#### M4-5 — Publish residual-risk and release-readiness decision
**Acceptance criteria**
- Decision cites deterministic, empirical, adversarial, and confirmatory evidence separately.
- Known weak/no-benefit mechanisms are not represented as successful assurance.

**Depends on:** M4-4

---

## Milestone 5 — Optional research-state/HITL continuity experiment

### Epic M5-E1 — Determine whether a thin agent/harness layer earns inclusion

#### M5-1 — Implement deterministic local research-state prototype
**Acceptance criteria**
- State/restart/idempotency/review-binding tests pass before model-spend experiments.
- Core assurance project does not depend on this prototype.

**Depends on:** M2-6

#### M5-2 — Define frozen research microworld benchmark
**Acceptance criteria**
- Includes forced interruption/restart, cross-session/cross-model handoff, exact claim/evidence review binding, and protocol-induced failure measurement.
- Development and evaluation fixtures are frozen and manifested.

**Depends on:** M5-1, M0-6

#### M5-3 — Run bounded cross-session/cross-model experiment
**Acceptance criteria**
- Compare prototype against no-layer baseline.
- Measure continuity benefit and protocol-induced failures.
- `NO_MEASURABLE_BENEFIT` is an allowed terminal result.

**Depends on:** M5-2

#### M5-4 — Decide adapter path or close experiment
**Acceptance criteria**
- If benefit is material, specify thin transport-neutral adapters for selected harnesses.
- Otherwise close experiment with no core dependency.

**Depends on:** M5-3

---

## Milestone 6 — Hardening and first release

### Epic M6-E1 — Deterministic CI and operational reproducibility

#### M6-1 — Establish no-network PR CI
**Acceptance criteria**
- Formatting/lint/type/schema/unit/contract/state-machine checks run deterministically without network where feasible.
- Immutable fixtures are used for external-data-dependent tests.

**Depends on:** M1-15

#### M6-2 — Establish scheduled/pre-release heavy verification
**Acceptance criteria**
- Mutation, fault/crash/rebuild, and benchmark suites run on documented cadence.
- Large/network/model-spend jobs are isolated from ordinary PR correctness checks.

**Depends on:** M3-7, M4-5

#### M6-3 — Write runbook and continuity handoff process
**Acceptance criteria**
- A fresh maintainer/session can identify current milestone, exact component/dataset versions, unresolved risks, and replay commands without hidden conversational memory.

**Depends on:** M2-6, M4-5

#### M6-4 — Freeze first release evidence bundle
**Acceptance criteria**
- Finance vertical slice is reproducible.
- Accepted promotion lineage is inspectable end-to-end.
- Dimension-specific results and residual risks are preserved.
- Required reused-component behavior is backed by contract/fault-test evidence.

**Depends on:** M6-1, M6-2, M6-3

## Dependency-critical path

`M0-1 -> M0-2 -> M0-3 -> M0-5 -> M1-1 -> M1-2 -> M1-3 -> deterministic gates -> M2 finance slice -> M3 empirical layers -> M4 confirmatory evaluation -> M6 release`

FOSSIL proof work (`M0-11 -> M1-9..M1-12 -> M1-15`) joins the critical path before the finance slice can be considered reliable.

Milestone 5 is explicitly off the core critical path and may terminate with `NO_MEASURABLE_BENEFIT`.

## Issue-tracker operating rules

- Every issue gets one accountable owner before work starts.
- Every empirical mechanism issue states its target failure mode, baseline, metric, threshold, and kill/no-benefit criterion.
- Every benchmark issue records immutable dataset/configuration identity.
- Every change to promotion semantics updates the state-machine/specification and corresponding tests in the same change set.
- Red-team/adversarial findings become issues only when they fall within scope or a deliberate scope-expansion decision is recorded.
- No issue may close a protected assurance requirement with agent self-attestation alone; closure requires inspectable evidence such as code/tests/reports/receipts/review records.
