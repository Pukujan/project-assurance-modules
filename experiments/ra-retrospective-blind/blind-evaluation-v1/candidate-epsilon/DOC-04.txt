# Project plan

## Program principle

Implementation begins only after the authorized owner reviews the candidate preflight, especially build-vs-reuse and scope dispositions. The plan then proceeds from deterministic contracts and cheap reuse probes to one finance-first vertical slice, followed by empirical evaluation and resilience/adversarial evidence. Speculative mechanisms do not become prerequisites merely because they may be useful later.

## Milestone M0 — Reviewed project foundation

### Objective

Convert the frozen candidate preflight into an owner-approved implementation boundary and durable product/system specification before repository-scale build work.

### Scoped claim/capability

The project can state exactly what promotion means, which assurance dimensions exist, what the new core owns, what it delegates, and what evidence will close the first vertical slice.

### Dependencies / entry criteria

- Candidate run is frozen.
- Owner reviews `BUILD_VS_REUSE.md`, `SCOPE.md`, and `PROJECT_ASSURANCE.json` dispositions.
- No claim is made that pending empirical probes have already passed.

### Work

- Freeze project PDD and SDD for the new core/adoption program.
- Define promotion record and independent assurance-dimension schema.
- Define allowed promotion lifecycle/state transitions, review authority, supersession/revocation semantics, and fail-closed behavior.
- Freeze explicit invariants and failure-mode register.
- Establish deterministic/no-network PR check lane for the new core where feasible.
- Define project-specific handoff schema/validator because the frozen PAM module requires one but supplies no handoff schema.
- Freeze component/repository contract and exact-version composition manifest format.

### Required evidence / validation

- Reviewed PDD/SDD/scope/build-vs-reuse artifacts.
- Schema positive/negative fixtures.
- State-transition table plus forbidden-transition tests.
- Initial failure register mapped to planned validation classes.
- CI/check-lane configuration and deterministic local reproduction command.
- Handoff schema positive/negative validation fixtures.

### Exit gate

Owner approves implementation start; core contract/invariants are reviewable; manifest/schema fixtures are green; no repository boundary requires inventing a second runtime service.

### Explicit non-scope

No Source Ranker runtime integration, claim verifier, GraphRAG, cross-domain abstraction, or agent/harness experiment.

---

## Milestone M1 — Provenance contract and minimal promotion core

### Objective

Prove the reusable provenance boundary and implement only the deterministic promotion logic that remains genuinely project-owned.

### Scoped claim/capability

A promotion candidate can be represented with exact evidence/component identities; invalid deterministic prerequisites cannot produce an accepted transition; accepted/reviewed evidence lineage can be bound to FOSSIL without duplicating FOSSIL storage/history.

### Dependencies / entry criteria

- M0 exit gate passed.
- Exact FOSSIL Core revision selected for the probe.
- Local/frozen test fixtures available; no hidden confirmatory data required.

### Work

- Run FOSSIL contract/integrity probes for whole-artifact verification, review-reference authority, failed-ingest/orphan behavior, crash/partial-batch behavior, actor attribution, role/quality metadata binding, retry/replay/rebuild/redaction behavior.
- Record each hypothesis as pass/fail/uncertain rather than assuming a bug or feature.
- Shrink/adjust the new core if FOSSIL already owns a proposed responsibility.
- Implement promotion schema/model and deterministic policy/state engine.
- Implement FOSSIL adapter against public versioned contracts only.
- Implement generic identity/reference/authorization validator interfaces.
- Implement fail-closed promotion with a separate exploration path that remains usable when assurance infrastructure is unavailable.

### Required evidence / validation

- FOSSIL probe report pinned to exact revision and fixtures.
- Contract tests for adapter behavior and incompatible versions.
- Negative tests for missing/altered evidence IDs, stale/mismatched review references, unauthorized reviewer/actor, invalid transitions, and unavailable provenance service.
- Property/state-machine tests for lifecycle invariants.
- Replay/rebuild checks for promoted evidence/receipt identities.
- Evidence that exploration can continue while promotion remains blocked on assurance failure.

### Exit gate

A deterministic local integration fixture demonstrates one accepted and multiple rejected/fail-closed paths with exact replayable evidence identities; no unproven FOSSIL capability is represented as satisfied.

### Explicit non-scope

No empirical quality claim yet; no hidden evaluation; no finance-domain generalization claim.

---

## Milestone M2 — Finance-first vertical slice

### Objective

Exercise the core in a real domain boundary with deterministic SEC/financial identity, temporal/version, numeric, citation-root, and authorization semantics.

### Scoped claim/capability

A financial research result can be proposed from exact evidence, evaluated by domain-specific deterministic checks, reviewed where required, and either promoted with replayable lineage or rejected without blocking exploration.

### Dependencies / entry criteria

- M1 exit gate passed.
- Financial application revision and adapter contract pinned.
- A small immutable public/development fixture set is frozen, including wrong-version/restatement/temporal/numeric/citation-root negative cases.

### Work

- Implement/locate finance adapter at the application boundary rather than importing application logic into the core.
- Bind SEC/financial source identity and temporal/version semantics.
- Add deterministic numeric and citation-root checks where an oracle exists.
- Exercise reviewed promotion and rejected/blocked promotion paths end to end.
- Persist exact composition identity for core + FOSSIL + financial application + fixtures.

### Required evidence / validation

- Contract/integration tests across exact pinned revisions.
- Mechanically generated temporal/version/restatement/wrong-version/evidence-root cases.
- Metamorphic tests for representation/order changes that should preserve outcomes and identity changes that should invalidate them.
- Negative authorization/review-binding cases.
- Reproducible promoted/rejected fixture reports.

### Exit gate

The vertical slice passes deterministic and negative tests, replays against exact identities, and preserves the separation between provenance/integrity and semantic-support judgment.

### Explicit non-scope

No claim that the finance adapter proves generic domain validity; no cross-domain pack.

---

## Milestone M3 — Layered empirical evaluation and hidden confirmation

### Objective

Measure retrieval, source-suitability, semantic-support, and composition behavior separately, using public development material for tuning and restricted hidden material only for confirmation where adaptive contamination is meaningful.

### Scoped claim/capability

The program can make bounded empirical claims about specific layers without aggregating them into one universal assurance score or exposing hidden answers to implementation agents.

### Dependencies / entry criteria

- M2 deterministic slice green.
- Dataset/corpus/query/qrels manifests frozen with checksums/version identity.
- Evaluation metrics and decision thresholds defined before confirmatory execution.
- Evaluator/owner controls hidden payload access.

### Work

- Integrate Retrieval Benchmarker as research/CI-only and establish retrieval baselines on selected finance datasets.
- Run public-development evaluation for finance retrieval/reasoning and mechanically generated temporal/version cases.
- Run a bounded Source Ranker suitability experiment only after a baseline exists.
- Define separate semantic-support/unsupported-grounding evaluation where the output claim warrants it; use candidate claim/evidence datasets as evaluation inputs, not automatic runtime dependencies.
- Run composition tests and ablations: deterministic/provenance baseline; plus retrieval improvements; plus Source Ranker only if entry gate passed; any later verifier only as a separate experiment.
- Freeze the implementation/model/configuration before hidden confirmatory evaluation.
- Have the evaluator-owned boundary run the hidden suite and return only permitted aggregate/report artifacts.

### Required evidence / validation

- Dataset manifests and exact evaluator/component revisions.
- Layer-specific metrics, confidence/uncertainty, and error slices.
- Public-development reports separated from hidden-confirmatory reports.
- Access-control/process evidence that implementation agents cannot inspect hidden payloads.
- Ablation report showing incremental benefit/cost of optional layers.
- Explicit `NO_MEASURABLE_BENEFIT`/kill outcome when a mechanism fails its entry criterion.

### Exit gate

Every empirical claim names its dataset/protocol/component identity and scope; hidden material remained isolated; no optional layer is promoted to required runtime status without measured benefit.

### Explicit non-scope

No universal score; no domain-transfer claim; no adaptive tuning after hidden results without creating a new confirmatory run/material split.

---

## Milestone M4 — Resilience, adversarial review, and release evidence

### Objective

Test critical failure boundaries and decide whether the first program increment is supportable, what residual risk remains, and which deferred mechanisms have earned reconsideration.

### Scoped claim/capability

The released slice has evidence for deterministic correctness, fail-closed behavior, replay/rebuild under faults, reproducible empirical reports, and explicit residual risk rather than a generic verified label.

### Dependencies / entry criteria

- M1–M3 applicable exit gates passed.
- Critical invariants/failure register updated from observed test results.

### Work

- Run mutation testing against critical deterministic validators/state transitions.
- Run fault injection/crash/retry/partial-batch/replay/rebuild/redaction campaigns across the FOSSIL boundary and local core.
- Run adversarial review separate from ordinary test execution, focusing on bypass, forged acceptance, stale/mismatched evidence/review identity, hidden-holdout leakage, and ownership-boundary violations.
- Measure operational friction: latency, false block/reject rate where measurable, researcher interruption burden, and protocol-induced failure.
- Reconcile findings through the scope-admission rule rather than automatically expanding scope.
- Produce release/milestone evidence package, exact composition manifest, residual-risk register, and current/historical structured handoff checkpoint.

### Required evidence / validation

- Mutation report for critical deterministic logic.
- Fault/recovery/replay/rebuild reports.
- Adversarial review findings with disposition and evidence.
- Reproducibility run from a clean environment/frozen fixtures.
- Cost/friction report.
- Residual-risk register separating integrity, correctness, empirical, security/authorization, provenance, and review risks.
- Release decision tied to exact revision/evidence identities and human approval where judgment is inherent.

### Exit gate

The owner can accept, defer, or stop the increment from concrete evidence. Any accepted release names exact component/data/methodology identities and residual risk. Mechanisms that show no benefit remain excluded.

### Explicit non-scope

A release does not certify universal truth, cross-domain validity, or future revisions not represented by the evidence package.

## Deferred future experiments

These are **not** active implementation milestones. They may be admitted only through `SCOPE.md`:

- claim-verification layer for a measured unsupported-synthesis residual;
- GraphRAG for a measured graph-shaped retrieval failure class;
- second-domain assurance pack after a concrete adopter exists;
- agent/harness continuity experiment after deterministic state/restart/idempotency/review-binding tests and with `NO_MEASURABLE_BENEFIT` as an acceptable outcome.
