# Scope boundary

## Current goal

Deliver a small, replayable assurance composition that governs **consequential promotion transitions**, not exploration. The first vertical slice uses an existing financial analysis workflow and existing provenance/retrieval infrastructure to show that a promoted item can carry dimension-specific evidence, exact identities, deterministic checks where available, empirical evidence where appropriate, and explicit human review where judgment remains.

## Current bounded claims/capabilities

The first release may claim only what its evidence supports:

1. **Promotion-state integrity** — an accepted/reviewed promotion cannot be created when a required current-horizon evidence dimension is missing, invalid, stale, unauthorized, or points to an unresolvable exact identity.
2. **Exploration remains available** — assurance failure prevents acceptance/promotion but does not fabricate success or require the research workflow itself to stop.
3. **Replay identity** — accepted promotions identify exact source/artifact evidence plus exact tested component, dataset, configuration, and policy identities needed to reproduce the decision path.
4. **Dimension separation** — provenance/citation integrity, temporal/numeric validity, source suitability, retrieval quality, semantic support, authorization, and human review are represented separately; no universal verification flag or aggregate score is authoritative.
5. **First-domain deterministic validity** — finance temporal/version/numeric/identity checks use deterministic or domain-authoritative oracles where feasible.
6. **Empirical separation** — retrieval behavior, source-ranking behavior, and synthesis/claim behavior use separate task-appropriate benchmarks and reports.
7. **Holdout integrity** — adaptive development agents cannot read hidden confirmatory labels/answers/seeds or equivalent result-bearing state.
8. **Resumability** — material work can resume from machine-readable repository state after reconciling referenced live repository/CI objects.

## Assurance horizon for the first vertical slice

Included now:

- PDD/system design, invariants, and failure-mode register for the new thin coordinator.
- Dimension-specific evidence/promotion schema and fail-closed promotion state machine.
- Exact component/dataset/config/policy identity in promotion and benchmark receipts.
- FOSSIL Core adapter plus empirical contract probes for the specific integrity/authority/recovery properties the program relies on.
- Financial-application integration contract for exact SEC/source/time/version identity and deterministic validators.
- Retrieval Benchmarker reuse for development evaluation and persisted reports.
- Public development benchmark manifests plus isolated hidden confirmatory evaluation.
- Deterministic/no-network PR check lane where feasible.
- Structured handoff policy/schema/current-state artifact and stale-state reconciliation.
- Composition/ablation evidence and explicit residual-risk report.
- Separate adversarial review of bypass/leakage/failure modes before a consequential release claim.

## Explicit non-goals

- Governing every model response, shell command, code edit, or exploratory thought.
- Recreating a generic agent stamp/compliance system.
- Replacing FOSSIL Core, Retrieval Benchmarker, Source Ranker, or the financial application.
- Treating provenance/citation integrity as proof of semantic correctness.
- Producing one universal trust, quality, or verification score.
- Making graph/vector indexes the evidence authority.
- Universal cross-domain validity from a finance result.
- Making claim verification, GraphRAG, an ontology/meta-system, cross-domain packs, or agent/harness transport adapters prerequisites for the first vertical slice.
- Requiring human review for deterministic low-consequence checks.
- Using hidden confirmatory evaluation as a development/tuning set.
- Making evaluation-only benchmark infrastructure a mandatory production runtime dependency without evidence.

## Deferred mechanisms and reconsideration triggers

| Mechanism | Current disposition | Reconsider when |
| --- | --- | --- |
| Source Ranker runtime inclusion | Deferred / empirical probe | A bounded finance development-set benchmark shows incremental benefit over simpler source policy, with acceptable calibration and friction. |
| Claim verification | Deferred | A specific semantic-support claim is admitted with a task definition, gold data, baseline, and contamination-safe evaluation plan. |
| GraphRAG/graph retrieval | Deferred | Simpler retrieval demonstrably fails a scoped task and graph-layer ablation shows material benefit. |
| Ontology/meta-system | Deferred | Repeated cross-component ambiguity appears in at least two real domains and cannot be handled by the current evidence schema. |
| Cross-domain assurance packs | Deferred | A second materially different domain is ready and exposes domain-specific gold/policy requirements. |
| Agent/HITL local research-state plugin | Bounded experiment only | Deterministic restart/idempotency/review-binding tests are green and a predeclared cross-session continuity experiment justifies model spend. |
| Additional harness/MCP/ChatGPT transports | Deferred | Core local semantic operations demonstrate measurable benefit; adapters remain thin and transport-specific. |

## Rejected mechanisms

- Universal agent stamps/checklist self-attestation: rejected due the supplied negative prior and conflict with evidence-backed closure.
- Universal `verified=true`: rejected because it collapses independently meaningful assurance dimensions.
- Monolithic assurance repository that absorbs existing systems: rejected because it destroys independent ownership/versioning and increases duplicated failure surface.
- Silent promotion bypass when assurance infrastructure fails: rejected; exploration may continue, accepted promotion may not be forged.
- Hidden-holdout content in agent-visible state or handoffs: rejected as contamination.

## Repository/component boundary

Use one **new thin coordinator repository** plus independently versioned existing systems. The coordinator owns only promotion/evidence contracts, deterministic transition logic, exact composition identity, thin adapters, and project-specific validation orchestration.

It must not own durable provenance storage, general retrieval ranking, source-ranking research, the financial product workflow, model-provider/harness transports, or future cross-domain packs. `REPOSITORY_MAP.md` defines the boundary in detail.

## Scope-admission rule

New work may enter the current assurance horizon only when all of the following are recorded:

1. a current claim/failure surface it changes;
2. why the existing scoped mechanisms cannot satisfy that claim;
3. build-vs-reuse disposition and exact candidate identity;
4. the cheapest credible validation/probe;
5. owner/repository and must-not-own boundary;
6. dependency/entry criteria;
7. exit evidence plus a kill/defer/no-benefit criterion;
8. project-owner review if the change materially expands scope or weakens a gate.

Red-team findings route to **mitigate now**, **measure**, **defer**, or **not applicable**; discovery alone does not admit implementation work.
