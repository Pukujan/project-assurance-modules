# Baseline project plan — Research Assurance

## 1. Purpose

Build a narrowly scoped assurance-oriented research/software program that can answer one operational question:

> When evidence is promoted into a consequential conclusion, benchmark result, architecture decision, or shared knowledge, what evidence and validation justify that promotion, and how can the decision be replayed later?

The project is not an agent-control framework and is not a universal correctness layer. Exploration remains available even when assurance checks fail. Assurance applies at explicit promotion boundaries where a candidate result would become accepted/reviewed/shared state.

## 2. Desired outcomes

The first useful release should make a promotion decision inspectable and replayable by recording:

- the exact candidate claim/result/decision being promoted;
- the exact evidence artifacts and citations supporting it;
- source identity, provenance and version information;
- the deterministic checks that ran and their results;
- any fallible/empirical judgments, with method/configuration/version identity;
- any human review, bound to the exact candidate and evidence set reviewed;
- the policy/domain context under which the decision was made;
- the resulting promotion disposition without collapsing all assurance dimensions into one Boolean;
- enough immutable inputs/configuration to replay the decision or explain why exact replay is impossible.

Success is demonstrated by a small finance-oriented vertical slice and by repeatable evaluation of each assurance layer independently and in composition.

## 3. Non-goals

Initial scope explicitly excludes:

- governing every model response, coding action, tool call or exploratory research step;
- a generic agent "compliance stamp" or self-attested checklist;
- a universal `verified=true` state or universal trust score;
- mandatory graph retrieval, GraphRAG, ontology/meta-system infrastructure, MCP, or multi-harness integration;
- rebuilding provenance storage, source ranking, retrieval benchmarking or the financial application when existing systems satisfy the scoped need;
- claiming cross-domain validity from finance results;
- treating source quality, citation integrity, retrieval quality, semantic support, temporal validity, numeric validity and human review as interchangeable;
- tuning implementation behavior against hidden confirmatory material.

## 4. Core design principles and invariants

### 4.1 Promotion, not exploration, is gated

Research and analysis may continue after a failed check. A failed gate prevents only the protected promotion transition. The system must never silently forge, downgrade or bypass an accepted/reviewed promotion.

### 4.2 Assurance is dimension-specific

A promotion record carries separate outcomes for at least the dimensions that apply to that transition. Candidate dimensions include:

- artifact/provenance integrity;
- source authority/quality;
- claim/source suitability;
- citation identity/integrity;
- temporal/version validity;
- numeric validity;
- retrieval correctness;
- semantic support/refutation/insufficiency;
- authorization/actor attribution;
- human review.

A dimension may be `not_applicable`, `not_run`, `pass`, `fail`, or an explicitly richer domain-specific result. No aggregate field may imply that passing one dimension proves another.

### 4.3 Determinism before stochastic judgment

Where identity, authorization, timestamps, versions, citations, calculations or state transitions can be checked deterministically, implement those checks before adding model-based judgment.

### 4.4 Evidence authority is durable; indexes are projections

Graph/vector/search indexes are rebuildable access paths. They are not the sole authority for evidence identity or promotion history. Durable source snapshots, evidence artifacts, lineage and promotion events must remain independently auditable.

### 4.5 Human review is consequential and exact

Human review is reserved for consequential judgments that cannot be made deterministically or are explicitly policy-controlled. Review must be bound to exact candidate/evidence/configuration identities; changing those identities invalidates or supersedes the review rather than silently carrying it forward.

### 4.6 Reuse must be empirically bounded

Existing systems are integrated through narrow adapters and tested against the behavior this project actually relies on. Marketing scope or intended scope is not treated as proof of fitness.

### 4.7 Hidden evaluation remains hidden

Development benchmarks may be public to implementers. Confirmatory/hidden evaluation material must be isolated from adaptive implementation work. Results from hidden evaluation are recorded after the implementation under test is frozen.

## 5. Proposed project artifacts

Before implementation expands beyond a thin vertical slice, create and maintain the following project artifacts:

1. **Problem and scope specification** — promotion boundary, protected transitions, non-goals and domain assumptions.
2. **Assurance model specification** — dimension vocabulary, result semantics, evidence references and non-collapse rules.
3. **Promotion state-machine specification** — legal transitions, authorization rules, supersession and replay behavior.
4. **Evidence/promotion receipt schema** — exact identities for candidate, evidence, checks, component versions, datasets, configuration and review.
5. **Finance policy pack/specification** — source authority, temporal/version rules, numeric checks and required review for the initial domain.
6. **Adapter contracts** — minimal interfaces for FOSSIL Core, Source Ranker, Retrieval Benchmarker and the finance application.
7. **Failure-mode register** — hypotheses, severity, detection, mitigations, tests and residual risk.
8. **Evaluation plan** — layer-specific datasets, public/hidden split, metrics, baselines, ablations and kill/no-benefit criteria.
9. **Reproducibility manifest format** — source commits/digests, dataset manifests, environment lock, seeds/configuration and generated artifacts.
10. **Operational handoff/decision log** — current milestone, frozen decisions, unresolved questions and exact next work.

These are living engineering artifacts, not ritual documents: each exists only because it defines an executable boundary, testable invariant, reproducibility requirement or continuity need.

## 6. Proposed repository/component structure

The implementation repository should remain small and composition-oriented. A provisional layout is:

```text
research-assurance/
  docs/
    problem-and-scope.md
    assurance-model.md
    promotion-state-machine.md
    finance-policy.md
    failure-modes.md
    decisions/
  schemas/
    promotion-receipt.schema.json
    evidence-reference.schema.json
    dataset-manifest.schema.json
  src/
    core/
      promotion.py
      dimensions.py
      receipts.py
    checks/
      identity.py
      citation.py
      temporal.py
      numeric.py
      authorization.py
    adapters/
      fossil.py
      source_ranker.py
      retrieval_benchmarker.py
    policy/
      finance.py
    cli/
      assess.py
      replay.py
  eval/
    manifests/
    public/
    runners/
    reports/
  tests/
    unit/
    contract/
    integration/
    property/
    fault/
  examples/
    finance/
  RUNBOOK.md
  CHANGELOG.md
```

This is a starting hypothesis, not a requirement to create every directory immediately. The core package owns promotion semantics and receipts; existing systems retain their own responsibilities.

## 7. Core data and state model

### 7.1 Candidate promotion

A candidate promotion should identify:

- `promotion_id`;
- `promotion_kind` (`conclusion`, `benchmark_result`, `architecture_decision`, `shared_knowledge`, extensible);
- exact candidate content identity/digest plus a human-readable label;
- domain/policy pack identity and version;
- evidence references with durable artifact/source identity;
- requested promotion target/state;
- initiating actor/service identity;
- creation timestamp and parent/superseded promotion where applicable.

### 7.2 Assurance result

Each applicable check produces a result containing:

- dimension and check identifier;
- check implementation/version;
- deterministic vs fallible classification;
- exact inputs/configuration;
- status/result and machine-readable findings;
- evidence/artifacts generated by the check;
- timestamp/runtime identity;
- residual uncertainty when applicable.

### 7.3 Promotion receipt

A promotion receipt is append-only evidence of an attempted or completed transition. It should contain the candidate identity, all required dimension results, policy/version identity, actor/authorization evidence, review bindings, transition disposition, and references to immutable artifacts needed for replay.

The receipt does not state universal truth. It states what was assessed, under which policy and evidence, by which mechanisms, and what transition was authorized.

### 7.4 State transitions

A minimal state model should distinguish exploratory/candidate state from protected promoted state. One workable starting model is:

```text
DRAFT/EXPLORATORY
  -> CANDIDATE
  -> ASSESSED
  -> REVIEW_PENDING   (when policy requires human judgment)
  -> ACCEPTED         (protected promotion)
  -> SUPERSEDED       (newer accepted state references predecessor)

CANDIDATE/ASSESSED/REVIEW_PENDING
  -> REJECTED_FOR_PROMOTION
```

A failed check may produce `REJECTED_FOR_PROMOTION` while leaving the underlying research artifact available for continued exploration. `ACCEPTED` requires all policy-mandated checks/reviews to be satisfied for the exact candidate/evidence identities.

## 8. Build-versus-reuse decisions

### 8.1 FOSSIL Core — reuse as provenance substrate, conditionally

Use FOSSIL Core for durable immutable artifacts/source snapshots, exact citations, append-only history/lineage and reviewed promotion boundaries if contract/integration tests confirm the specific behaviors relied upon.

Do not duplicate its storage/history model in the new project. Build only a narrow adapter plus project-specific promotion receipt/schema logic not already supplied.

Before relying on it, empirically test the research packet's open integrity questions: whole-artifact integrity verification, review-reference authority, orphan storage after failed ingest, crash/partial-batch behavior, caller/service attribution, and whether role/quality metadata is provenance-bound strongly enough for this use case.

### 8.2 Source Ranker — reuse behind an empirical boundary

Integrate source suitability/quality capabilities only behind a narrow adapter. Separate source authority/quality from claim/source suitability in the assurance model. Establish measured performance for the specific finance tasks used by this project before treating ranker outputs as promotion evidence.

If the measured benefit is weak or unstable, retain deterministic source-policy rules and omit the ranker from mandatory promotion.

### 8.3 Retrieval Benchmarker — reuse as evaluation infrastructure

Use the existing retrieval benchmarker for immutable corpora/queries/qrels, configuration identity, persisted rankings and reports. Do not reimplement a retrieval evaluation stack.

Use it to evaluate sparse/dense/hybrid/rerank alternatives and composition effects, with finance datasets where appropriate. Retrieval metrics remain retrieval metrics; they do not certify semantic correctness of final claims.

### 8.4 Financial application — use as first domain consumer

Use the financial analysis application as the initial realistic integration target because it has SEC/financial evidence, temporal/version semantics and consequential research workflows. Keep assurance core transport/application-neutral so the app is a consumer, not a hard dependency.

### 8.5 Claim verification — evaluate before building a bespoke subsystem

Start with deterministic claim checks where possible and benchmark existing/simple claim-evidence approaches on public development sets before committing to a bespoke verifier. FEVER, SciFact and AVeriTeC are candidate support/refute datasets; RAGTruth and ALCE are candidate grounding/citation behavior datasets. Finance-specific claims require domain-specific evaluation rather than assumed transfer.

### 8.6 GraphRAG/ontology/meta-system — defer

Do not include graph retrieval or ontology/meta-system infrastructure in the first implementation. Add only if a defined failure mode cannot be solved adequately by simpler retrieval/provenance mechanisms and an ablation demonstrates material benefit.

### 8.7 Agent/harness research-state layer — optional experiment

Keep agent/harness integration outside the core critical path. After deterministic state/restart/idempotency/review-binding tests are green, run a bounded experiment on frozen local research microworlds with interruption/restart and cross-model handoff. Accept `NO_MEASURABLE_BENEFIT` as a successful experimental outcome and do not promote the layer to a core dependency without evidence.

## 9. Finance vertical slice

The first end-to-end scenario should be deliberately narrow: promote a finance research conclusion derived from versioned SEC/financial evidence.

The slice should exercise:

1. ingest/reference immutable evidence through FOSSIL Core;
2. create exact citations into evidence;
3. construct a candidate conclusion with explicit evidence references;
4. run deterministic identity, citation, temporal/version, numeric and authorization checks;
5. optionally run source suitability/retrieval/semantic checks only where the chosen scenario requires them;
6. require human review for a consequential judgment defined by the finance policy;
7. issue an accepted promotion receipt only when all required checks bind to the exact candidate/evidence set;
8. replay the assessment from recorded identities/configuration;
9. demonstrate that a failed gate prevents promotion but does not destroy/block exploratory work;
10. demonstrate supersession when newer/restated evidence changes the accepted conclusion.

Mechanically generated cases should include wrong filing/version, restatement, stale temporal evidence, numeric corruption, broken citation, evidence-root mismatch and unauthorized promotion attempts.

## 10. Validation and benchmark strategy

### 10.1 Deterministic checks

For core deterministic behavior, require:

- unit tests for identity/digest, citation bounds, temporal rules, numeric calculations and authorization;
- contract tests for every reused-system adapter;
- integration tests for promotion receipts and replay;
- property/state-machine tests for legal/illegal promotion transitions and supersession;
- mutation testing on critical deterministic gates to show tests fail when gate logic is weakened;
- fault injection for storage/network/process failures at persistent boundaries;
- crash/restart/replay/rebuild tests where state durability matters;
- deterministic corruption campaigns for evidence, citations, actor identity and receipts.

PR CI should be deterministic and no-network where feasible. Network/data-fetch preparation should occur out of band and produce immutable, versioned test fixtures/manifests.

### 10.2 Retrieval evaluation

Use TREC/BEIR for general retrieval behavior where useful and FinanceBench/FinQA/TAT-QA for finance-oriented retrieval/reasoning. Record corpus/query/qrel identity, retrieval configuration and ranking output. Compare sparse, dense, hybrid and reranked configurations as appropriate.

Metrics may include Recall@k, nDCG@k and MRR where supported by the dataset. Do not combine them into a project-wide assurance score.

### 10.3 Semantic/grounding evaluation

Evaluate claim/evidence support separately from retrieval. Candidate public development sets include FEVER, SciFact, AVeriTeC, RAGTruth and ALCE, with finance-specific mechanically generated or curated cases for temporal/numeric/version semantics.

Track task-appropriate measures such as support/refute classification, evidence sufficiency, citation precision/recall or unsupported-claim rate. Preserve per-dataset results and error taxonomy rather than one universal number.

### 10.4 Public development versus hidden confirmation

Create two evaluation channels:

- **development**: public/frozen datasets and visible failure analysis used to improve implementation;
- **confirmatory**: held-out/hidden material unavailable to implementation agents until the evaluated implementation/configuration is frozen.

Every confirmatory run records implementation commit/digest, dependency lock, model/provider/version where applicable, dataset manifest identity, configuration, seeds and generated outputs. No post-hoc tuning in the same confirmatory run.

### 10.5 Composition and ablation

Test layers independently before composition. At minimum compare:

- deterministic policy only;
- deterministic policy + retrieval improvements;
- deterministic policy + source ranking/suitability where applicable;
- deterministic policy + semantic verifier where applicable;
- full candidate composition.

A layer earns mandatory inclusion only if it improves the defined target behavior enough to justify cost/latency/complexity without creating unacceptable new failure modes.

### 10.6 Kill/no-benefit criteria

For optional fallible mechanisms, predefine outcomes that justify omission. Examples:

- no statistically/practically meaningful gain on the target error class;
- gain disappears on held-out finance cases;
- increased protocol-induced failure or false rejection exceeds benefit;
- operational cost/latency is disproportionate to risk reduction;
- simpler deterministic/domain policy achieves equivalent protection.

Document residual risk when a mechanism is killed rather than hiding the unresolved failure mode.

## 11. Failure-mode register seed

The initial register should include at least:

| Failure mode | Why it matters | Primary detection/validation |
| --- | --- | --- |
| Evidence artifact altered or mismatched | Promotion no longer refers to reviewed evidence | digest/integrity checks; corruption tests |
| Citation points to wrong span/version | Apparent support is not exact support | deterministic citation identity/bounds; wrong-version cases |
| Stale/restated financial evidence used | Conclusion may be temporally invalid | finance temporal policy; generated restatement cases |
| Numeric value/calculation incorrect | Consequential factual error | deterministic calculation/reconciliation checks; mutation/corruption tests |
| Source is authoritative generally but unsuitable for claim | Source-quality score masks claim mismatch | separate source-authority and suitability dimensions; benchmark |
| Retrieval finds plausible but incomplete evidence | Claim may be under-supported | qrels-based retrieval evaluation; evidence-sufficiency evaluation |
| Semantic verifier overclaims support | False assurance | public + hidden support/refute evaluation; adversarial review |
| Review refers to a prior candidate/evidence set | Human approval silently detached from actual promotion | exact review binding; state/property tests |
| Unauthorized service/caller can promote | Trust boundary bypass | actor/authorization contract tests; fault/adversarial tests |
| Failed ingest leaves ambiguous/orphan state | Replay/storage integrity uncertainty | FOSSIL contract/fault tests |
| Crash/partial batch forges or loses accepted state | Durable history cannot be trusted | crash/restart/partial-commit testing |
| Index differs from durable evidence authority | Search projection masquerades as source of truth | rebuild tests; compare projection to immutable source |
| Hidden confirmatory material leaks | Evaluation becomes adaptively tuned | access separation; run attestations/manifests |
| Generic agent protocol blocks useful exploration | Repeats prior failure pattern | keep gate at promotion boundary; protocol failure-rate experiment |

Each item must gain owner, severity, test reference, mitigation, and residual-risk disposition during Milestone 0/1.

## 12. Milestones and exit criteria

### Milestone 0 — Scope, contracts and reproducibility foundation

Deliver specifications for scope, assurance dimensions, state machine, receipt schema, finance policy, adapter contracts, failure-mode register and evaluation split.

Exit when:

- protected promotion transitions and non-goals are explicit;
- no universal verification score/flag exists;
- schemas can represent separate dimension results and exact review binding;
- public versus hidden evaluation process is defined;
- component/dataset/version manifest format is defined;
- first finance scenario and generated negative cases are specified.

### Milestone 1 — Deterministic promotion substrate + FOSSIL boundary proof

Implement the minimal core state machine/receipt path, deterministic checks and FOSSIL adapter. Execute the identified FOSSIL integrity probes rather than assuming behavior.

Exit when:

- illegal promotion transitions cannot produce accepted state;
- failed gates leave exploration possible;
- receipts replay against immutable test fixtures;
- critical deterministic checks survive mutation testing;
- crash/corruption/authorization tests are green for the scoped path;
- FOSSIL boundary findings are recorded with explicit workarounds or stop conditions.

### Milestone 2 — Finance end-to-end vertical slice

Integrate the financial application and finance policy for one consequential conclusion workflow.

Exit when:

- correct, wrong-version, stale/restated, numeric-corruption, citation-corruption and unauthorized cases behave as specified;
- required human review is bound to exact candidate/evidence identity;
- supersession/replay works;
- a reproducibility bundle can reconstruct the promotion assessment.

### Milestone 3 — Retrieval/source/semantic empirical layers

Use Retrieval Benchmarker and, where justified, Source Ranker; evaluate a minimal semantic/grounding approach only after deterministic substrate is stable.

Exit when:

- each layer has a stated target failure mode and baseline;
- evaluation datasets are mapped to the correct layer;
- results are reported separately by dimension/dataset;
- composition/ablation results identify mandatory, optional and rejected layers;
- weak/no-benefit layers are removed from mandatory promotion.

### Milestone 4 — Adversarial and confirmatory evaluation

Freeze implementation/configuration, run adversarial review and hidden confirmatory evaluation without exposing hidden material to implementers.

Exit when:

- run manifests make the evaluation reproducible;
- hidden data was not available during adaptive development;
- consequential residual risks and failure cases are documented;
- no failed dimension is obscured by aggregate scoring.

### Milestone 5 — Optional agent/harness continuity experiment

Only after the core is green, test a small local research-state/HITL layer on frozen microworlds with forced restart and cross-model handoff.

Exit with one of:

- measured benefit sufficient to justify a thin adapter/integration path; or
- `NO_MEASURABLE_BENEFIT`, with the experiment closed and no core dependency introduced.

### Milestone 6 — Hardening and first release

Consolidate runbook, compatibility/version policy, reproducibility checks, deterministic CI, residual-risk register and release evidence.

Exit when a fresh maintainer can reproduce the finance slice and understand every accepted promotion's evidence/check/review lineage without conversational memory.

## 13. Ownership model

Assign ownership by responsibility rather than by technology novelty:

- **Assurance core owner** — state model, receipt schema, invariants, deterministic gates.
- **Provenance integration owner** — FOSSIL adapter/contracts/fault tests.
- **Evaluation owner** — dataset manifests, benchmark harness integrations, hidden-eval separation, reports.
- **Finance domain owner** — source authority, temporal/version/numeric policy and finance gold cases.
- **Human review owner** — review criteria, reviewer instructions and review-binding semantics.
- **Optional experiments owner** — source-ranker/semantic/agent layers, each with explicit kill criteria.

A small team may combine roles, but each deliverable and decision still needs a named accountable owner in the issue tracker.

## 14. Reproducibility and provenance requirements

Every benchmark, promotion assessment and release evidence bundle must record as applicable:

- repository commit or content digest for every component;
- dependency/environment lock identity;
- dataset/corpus/query/qrel manifest with source/version/digest/license notes;
- model/provider/model-version and prompt/config identity for fallible checks;
- random seeds and nondeterminism notes;
- policy/schema/check versions;
- durable evidence artifact/source identities;
- exact command/config used for replay;
- generated rankings/reports/receipts as immutable outputs;
- human review identity/time and exact reviewed candidate/evidence digest.

If an upstream mutable identifier cannot guarantee replay, snapshot or content-address the material before it can support an accepted promotion.

## 15. CI and engineering foundations

Initial engineering foundation should include:

- pinned/locked dependencies;
- formatting/lint/type checks appropriate to implementation language;
- deterministic unit/contract tests on every PR;
- no-network PR test path with vendored/generated immutable fixtures;
- schema validation for receipts/manifests;
- property/state-machine tests for protected transitions;
- mutation testing target for critical gates, run on scheduled or pre-release cadence if too expensive for every PR;
- fault/crash/rebuild suite on scheduled/pre-release cadence;
- benchmark runners separated from ordinary PR CI so large/network/model-spend jobs cannot silently become correctness gates;
- artifact retention sufficient to inspect failed benchmark/fault runs.

Model-spend experiments start only after deterministic state/restart/idempotency/review-binding behavior is green.

## 16. Decision gates before expanding scope

New mechanisms enter the core only if all of the following are answered:

1. What specific failure mode does this mechanism address?
2. Why is an existing maintained system or deterministic check insufficient?
3. What benchmark/gold cases measure the intended benefit?
4. What is the baseline without the mechanism?
5. What cost, latency, operational and new failure modes does it add?
6. What threshold constitutes material benefit?
7. What kill/no-benefit outcome removes it from the mandatory path?
8. How will its exact version/configuration be preserved for replay?

This gate applies especially to semantic verifiers, graph retrieval, ontology/meta-systems and agent/harness layers.

## 17. First-release acceptance criteria

The project is ready for an initial assurance release when all of the following hold:

- one finance promotion workflow is end-to-end and reproducible;
- a failed assurance check prevents accepted promotion while preserving exploratory work;
- accepted promotion cannot be forged through an unreviewed/unauthorized transition in the tested scope;
- evidence/citation/version/numeric/authorization checks have deterministic test coverage and critical mutation resistance;
- FOSSIL behaviors relied on by the project have empirical contract/fault-test evidence;
- retrieval/source/semantic layers included in the mandatory path have measured benefit for defined failure modes;
- public development and hidden confirmatory evaluation are separated and provenance-recorded;
- every accepted promotion exposes dimension-specific results, not a universal verified state;
- indexes can be rebuilt without becoming the sole evidence authority;
- a fresh session can resume from repository artifacts, issue state and run manifests without hidden conversational context.

## 18. Open questions to resolve during Milestone 0

These are project decisions, not reasons to expand scope before work starts:

- What exact storage/receipt primitives already exist in FOSSIL Core versus what must live in the assurance layer?
- What is the minimal finance policy needed for the first consequential conclusion workflow?
- Which source-authority decisions can be deterministic and which require ranking or review?
- Which claim/evidence task best represents the first semantic-support failure mode, if any?
- What hidden confirmatory cases can be held by an evaluator without contaminating development?
- What severity threshold requires human review versus deterministic acceptance/rejection?
- What replay guarantee is required when a fallible model/provider is no longer available exactly?

Resolve these through explicit contracts, experiments and recorded decisions; do not answer them by importing untested architecture preferences.
