# Scope boundary

## Current goal

Deliver the smallest assurance program that can make one consequential research-promotion path replayable and evidence-backed without becoming a universal agent-control system. The first vertical slice is finance-oriented: a research result backed by versioned SEC/financial evidence is proposed for promotion, checked across independent assurance dimensions, reviewed where judgment remains, and bound to durable provenance/evidence identities.

## Current claims/capabilities

The present assurance horizon authorizes these claims only:

1. **Dimension separation.** The project can represent integrity/provenance, citation binding, temporal validity, numeric validity, source/claim suitability, semantic-support evidence, and human review as separate states/evidence rather than one `verified` bit.
2. **Deterministic gate behavior.** Missing/invalid deterministic prerequisites or authorization prevent an accepted promotion; the same failure does not prevent exploratory work from continuing.
3. **Replayable evidence identity.** A promotion record can bind exact source/artifact, validator, dataset/report, review, and component revision identities and can be replayed/rechecked against those identities.
4. **Provenance composition.** Durable artifact/history/lineage responsibilities are delegated to pinned FOSSIL Core behavior rather than reimplemented.
5. **Finance-first domain checks.** The first adopter can supply deterministic SEC/financial identity, temporal/version, numeric, citation-root, and authorization checks through a domain adapter.
6. **Separated empirical evaluation.** Retrieval, source-suitability, and semantic-support claims are evaluated independently with dataset manifests and layer-specific metrics; no universal score is produced.
7. **Adaptive-evaluation integrity.** Public development material and hidden/confirmatory material have separate authority/access, with hidden answers excluded from implementation-agent state and handoffs.
8. **Resumability.** Durable current state, exact pins, blockers, validation status, and next action allow a fresh worker to resume after reconciling live state.

## Explicit non-goals

- Governing every model response, edit, tool call, or ordinary coding action.
- Replacing FOSSIL Core or using PAM/FOSSIL as the live task tracker.
- Claiming that provenance or citation integrity proves semantic correctness.
- Producing a universal trust/quality/verified score.
- Building a new retrieval stack, graph/vector evidence authority, persistence engine, generic workflow service, or generic authorization control plane.
- Making Source Ranker, a claim verifier, GraphRAG, ontology/meta-systems, cross-domain packs, or agent/harness integration prerequisites for the first vertical slice.
- Claiming finance validity transfers to legal, medical, or other domains.
- Importing entire external standards when selective mapping/export is sufficient.
- Running hidden confirmatory evaluation from implementation-agent-visible infrastructure.
- Treating every red-team finding as current implementation scope.

## Current assurance horizon

### In horizon

- promotion record/schema and explicit dimension model;
- deterministic promotion state-transition and authorization rules;
- FOSSIL contract/integrity probe and thin adapter;
- finance domain adapter and deterministic temporal/numeric/identity/citation checks;
- deterministic/no-network PR CI for the new core where feasible;
- property/state-machine, metamorphic, mutation, negative/fail-closed, contract/integration, and fault/replay/rebuild validation where applicable;
- public development benchmarks and dataset manifests;
- restricted hidden confirmatory evaluation for adaptive empirical claims;
- composition/ablation and cost/friction measurement;
- adversarial review and explicit residual risk;
- structured handoff plus exact multi-repository/component pins.

### Complexity budget

For the first vertical slice:

- at most one new runtime library/repository is authorized;
- no new persistent store is authorized;
- FOSSIL remains the durable provenance authority;
- Retrieval Benchmarker remains research/CI-only;
- Source Ranker remains optional until an empirical entry gate passes;
- the financial application retains product/domain ownership;
- hidden evaluator assets remain outside implementation-agent access;
- external standard support is adapter/export-only unless a concrete interoperability requirement proves otherwise.

## Deferred mechanisms and reconsideration triggers

| Mechanism | Current disposition | Reconsider only when |
| --- | --- | --- |
| Source Ranker runtime use | Deferred pending empirical probe | A scoped finance claim/source-suitability benchmark shows material incremental benefit over simpler baselines at acceptable cost/false-block rate. |
| Claim-verification model/layer | Deferred | Measured residual unsupported/incorrect synthesis remains material after deterministic/provenance/domain/review layers, and an offline ablation shows useful reduction without creating false confidence. |
| Graph retrieval / GraphRAG | Deferred | A named retrieval failure class has a graph-structure hypothesis and benchmark evidence beats the existing retrieval baseline. |
| Ontology/meta-system | Deferred | Repeated concrete integration problems cannot be handled by the promotion schema plus domain adapters. |
| Cross-domain assurance packs | Deferred | A second materially different domain demonstrates repeated portable requirements and domain-specific obligations can be separated explicitly. |
| Agent/harness plugin/HITL layer | Deferred bounded experiment | Deterministic restart/idempotency/review-binding tests are green and a frozen microworld experiment can measure continuity benefit and protocol-induced failure. `NO_MEASURABLE_BENEFIT` is an acceptable terminal result. |
| Full external-standard adoption | Deferred | A specific consumer/interoperability contract requires more than selective mapping/export. |

## Rejected mechanisms

- **Universal agent stamp/compliance protocol:** rejected because the supplied prior experience showed gaming, blocked useful work, weak actionability, and inconsistent strictness.
- **Universal verified/trust score:** rejected because independent assurance dimensions have different oracles and residual risks.
- **Graph/vector index as sole evidence authority:** rejected because indexes must be rebuildable projections over authoritative evidence identities.

## Repository/component boundary

The program is intentionally multi-repository because the supplied systems are independently developed and have distinct ownership/lifecycles. The new promotion-assurance core owns only the dimension model, promotion contract/state transition logic, deterministic validation orchestration, evidence-reference contracts, and thin adapter interfaces. It must not own FOSSIL persistence/lineage, retrieval evaluation machinery, the finance application, hidden evaluation payloads, or optional research mechanisms.

Detailed boundaries are frozen in `REPOSITORY_MAP.md`.

## Scope-admission rule

New work may enter the current assurance horizon only if all of the following are true:

1. it closes a named current claim, observed failure mode, or required interoperability boundary;
2. the existing/reuse options and cheaper deterministic alternatives have been considered;
3. evidence shows the mechanism is necessary or likely to deliver measurable benefit relative to its complexity/cost;
4. ownership and must-not-own boundaries are explicit;
5. required validation and a kill/no-benefit outcome are stated;
6. the project owner reviews any material scope expansion.

Otherwise classify it as `measure`, `defer`, `not_applicable`, or `reject` with rationale. A new technology, benchmark result, or red-team finding alone is not admission evidence.

## Projectization review boundary

This candidate run freezes a proposed scope, not human approval of the real implementation start. Repository creation and implementation must remain blocked until the authorized owner reviews the material build-vs-reuse and scope dispositions. Cheap probes may then narrow the design before bespoke code expands.
