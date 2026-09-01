# Scope boundary

## Current goal and claims

Deliver one finance-domain vertical slice that creates a proposed promotion from immutable evidence and either produces a replayable, dimension-separated assurance record or fails closed for acceptance while preserving exploration. The slice claims only the evidenced outcome of each named check, policy version, evidence reference, review reference, and replay/rebuild behavior. Semantic support and source suitability remain distinct results.

## Assurance horizon

One representative financial workflow; one explicit promotion type; owner-approved source/evidence authority; a version-pinned composition with FOSSIL Core and the financial analysis application; and deterministic/no-network-feasible validation. A result may remain `proposed`, `blocked`, or `rejected`; only an explicit reviewed transition accepts it.

## Non-goals

- A universal `verified` score, universal agent-control stamp, or gate on ordinary exploration/coding.
- Cross-domain policy; replacement of FOSSIL, Source Ranker, Retrieval Benchmarker, or the financial application.
- Treating retrieval rank, source score, or model judgment as semantic proof.
- GraphRAG, ontology/meta-systems, vector/graph serving, generic claim verification, runtime benchmarker coupling, or consequential external actions.
- Exposure of hidden labels, seeds, answers, or confirmatory reports to adaptive agents.

## Deferred / rejected mechanisms

| Mechanism | Disposition | Reason | Reconsider only when |
| --- | --- | --- | --- |
| Graph/vector projection | deferred | Not authority and no current benchmark proves benefit. | Frozen evaluation shows material value over simple version-pinned baseline with rebuild evidence. |
| General claim verifier | deferred | Semantic validity needs a concrete domain proposition, labels, policy, and holdout. | Those inputs and approval exist. |
| Ontology/meta-system | rejected for slice | No slice invariant requires it. | Repeated integration failures demonstrate a narrower schema cannot solve a stated vocabulary gap. |
| Cross-domain packs | deferred | Transfer is unproven. | A second domain has its own authority policy, gold/holdout design, and owner. |
| Agent/harness adapters | deferred experiment | Benefit is unknown and cannot delay core work. | Deterministic state/restart/review-binding checks pass and a fixed protocol is approved. |
| Source Ranker acceptance gate | deferred | Its calibration is not established for this policy. | Pinned evaluation shows incremental benefit and owner approves a limited role. |

## Boundaries and admission rule

The new `promotion-assurance` component owns typed promotion records, deterministic policy evaluation, adapter contracts, and replayable evidence receipts. It must not own raw evidence persistence, a general search index, finance UX/domain interpretation, benchmark corpus/qrels, or generic agent control. New scope enters only when it fixes a current-claim failure or has owner-approved measured necessity for the slice. It must identify claim, owner, evidence, cost, and a `mitigate_now`, `measure_first`, `defer`, or `not_applicable` outcome. Red-team findings are triage inputs, not automatic work; material scope changes require review and a new frozen plan revision.
