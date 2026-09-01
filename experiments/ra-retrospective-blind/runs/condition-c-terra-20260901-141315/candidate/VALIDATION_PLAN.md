# Validation plan

Validation is claim-specific. A passing integrity check does not establish semantic support, retrieval quality, source suitability, or human approval; no aggregate `verified` state is permitted.

| Claim or failure surface | Required evidence and validation class | Closure / fail-closed rule |
| --- | --- | --- |
| Evidence root and artifact identity | Deterministic unit/contract tests for digest, immutable locator, citation binding, and exact version; negative altered-root/missing-citation fixtures | A promotion cannot enter accepted state when any required evidence reference fails identity or binding validation. |
| Numeric, temporal, identity, and authorization assertions | Deterministic parsing/rules and contract fixtures for wrong period, restatement/wrong version, mismatched entity, malformed number, unauthorized actor | Unknown or invalid result is explicit `blocked`/`rejected` for acceptance, never silently coerced to pass. |
| Promotion state transition | Property/state-machine testing over exploratory, proposed, reviewed, accepted, rejected, and recovery states; illegal-transition negatives | Exploration remains available; accepted cannot be reached without the policy-required receipts and exact review reference. |
| Rebuildable projections and replay | Metamorphic tests: rebuilding from the same immutable root preserves authority references and policy outcome; changing irrelevant projection ordering does not create acceptance | Projection is never authority. A replay mismatch is an investigation/blocker, not a reissued acceptance. |
| Critical deterministic controls | Mutation testing for evidence-root, authorization, temporal/version, review-binding, and acceptance-transition checks | Define a mutation score/escaped-mutant review threshold before execution; surviving critical mutations block closure or require documented risk acceptance. |
| Persistent failure boundaries | Fault injection for interrupted ingest/batch, partial write, retry/idempotency, crash/restart, redaction/rebuild, and orphan storage; integration replay tests | No partial/ambiguous record may masquerade as accepted. Recovery result and residual storage behavior are recorded. |
| FOSSIL composition contract | Version-pinned integration fixtures for whole-artifact verification, review reference authority, actor attribution, metadata provenance binding, and replay | Any unmet current invariant causes wrap/extend/more-research disposition; do not assume behavior from documentation alone. |
| Adversarial / red-team review | Separate review of bypass paths: stale review, wrong review-to-claim binding, substituted root, replay drift, actor spoofing, hidden-data leakage | Findings enter the scope-admission rule: mitigate now, measure first, defer, or not applicable. They are not auto-backlog items. |
| Retrieval quality | Frozen corpus/query/qrels manifests; deterministic benchmark configuration; sparse/dense/hybrid/rerank comparison; layer ablations; persisted report | Report only retrieval metrics for their declared population. It cannot satisfy semantic-support or promotion-integrity requirements. |
| Source-ranker / semantic-support quality | Dataset admission card, frozen development split, baseline and ablation, calibration/error analysis, and separate claim-evidence task report | Treat as advisory until evidence supports a narrowly stated use. If tuning is adaptive, confirm only on protected data. |
| Dataset/holdout integrity | Immutable dataset/version/label manifests; provenance/license record; access boundary; hidden seed/label policy; public-development versus confirmatory split where adaptation threatens contamination | Hidden material is not in implementation-agent handoffs, fixtures, logs, or prompts. No empirical release claim without declared input identity. |
| Composition effects | End-to-end test with and without optional ranker/retrieval components; ablation report; exact component revisions | A component earns continued inclusion only for measured scoped benefit, acceptable cost, and no violation of authority boundaries. |
| Reproducibility | Pinned dependency/composition receipt; fixture manifest; deterministic no-network check lane; replay report with policy version | The claimed result must identify code/policy/data/evidence revisions. A result that cannot be replayed is not a completed assurance record. |
| Cost and friction | Record latency, operator/reviewer actions, false blocks, recovery work, model spend where used, and protocol-induced failures | High friction or no measured benefit triggers simplify/defer/kill review rather than ritual expansion. |

## CI and evidence lanes

1. **Fast deterministic lane:** format/lint/type checks, schema validation, unit/contract/property/metamorphic tests, and synthetic fixtures with no network.
2. **Persistent-boundary lane:** fault injection, mutation campaign, replay/rebuild, and adversarial fixtures; run before a milestone claim that depends on the boundary.
3. **Research-evaluation lane:** versioned datasets/configurations/reports and ablations. It is not a merge-time runtime dependency and it does not expose hidden confirmatory content.
4. **Human-review lane:** consequential policy/source-authority decisions and acceptance waivers. Human review references are evidence, not a substitute for deterministic failures that can be tested.

## Explicitly conditional or non-applicable techniques

- Formal proof/model checking is not yet required: the selected state machine may justify it after M1, but value is unknown. State-machine/property tests are the current lower-cost control.
- Hidden holdouts are conditional: required before making adaptive empirical claims, not invented for deterministic integrity tests or if no adaptive tuning occurs.
- Model-based semantic evaluation, graph retrieval, and cross-domain datasets are deferred until they have a scoped claim, dataset authority, and measured-entry case.
- Live-network CI is not applicable to the primary deterministic lane; acquisition/integration environments, if later needed, must be separately reproducible and recorded.

## Residual-risk discipline

The first slice cannot prove general semantic truth, domain transfer, or absence of all provenance implementation defects. Each milestone retains a residual-risk register with affected claim, severity/likelihood rationale, evidence, owner, mitigation/defer decision, and reconsideration trigger. No residual risk is silently compressed into an acceptance boolean.
