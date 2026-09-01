# Frozen research packet — projectization task

## Benchmark use

This packet is a deliberately bounded reconstruction of the research context available before a mature project plan existed. It is not the finished project, and it intentionally omits final repository structure, issue numbering, milestone numbering, CI configuration, exact documentation layout, final component pins, and final project-tracking state.

Treat the research conclusions below as planning inputs that still require explicit scope, ownership, validation, and build-vs-reuse decisions.

## Problem

Design an assurance-oriented research/software program that can answer a narrow question:

> When a research workflow promotes evidence into a consequential conclusion, benchmark result, architecture decision, or shared knowledge, what evidence and validation are required to justify that promotion and make it replayable?

The system should not try to govern every model response or every ordinary coding action. Exploration should remain possible even when a promotion/assurance gate fails.

## Existing systems already available

The owner has several independently developed repositories/capabilities that may be reused rather than rebuilt:

- **FOSSIL Core** — durable immutable artifacts/source snapshots, exact citations, append-only event/history, lifecycle/lineage, reviewed promotion boundaries, redaction/rebuild/replay-oriented provenance behavior.
- **Source Ranker** — research/runtime work around source suitability/quality and claim-source fit; scope is broader than current proven implementation and should be empirically bounded.
- **Retrieval Benchmarker** — independent retrieval evaluation using immutable corpora/queries/qrels, sparse/dense/hybrid/rerank configurations, persisted rankings and reports; supports finance datasets such as FinanceBench, FinQA and TAT-QA.
- **Financial analysis application** — candidate first domain application with SEC/financial evidence, temporal/version semantics and real user-facing research workflows.

Possible future mechanisms discussed in research include claim verification, graph retrieval/GraphRAG, ontology/meta-systems, cross-domain assurance packs, and an agent/harness integration. None should be assumed necessary merely because they are interesting.

## Important research conclusions/constraints

- Provenance/citation integrity and semantic correctness are different assurance dimensions.
- Source quality and claim/source suitability are related but not identical.
- Retrieval correctness and synthesis/claim correctness are separate empirical problems.
- Graph/vector indexes should be treated as rebuildable projections rather than sole evidence authority.
- Deterministic numeric, temporal, identity, citation and authorization checks should be preferred where they can replace stochastic judgment.
- No universal `verified=true` state should collapse source integrity, citation integrity, temporal validity, numeric validity, semantic support and human review.
- Hidden confirmatory material must not be exposed to implementation agents if adaptive tuning would contaminate the result.
- Domain validity does not automatically transfer across finance/legal/medical/etc.; domain-specific gold/policy/source authority may be required.
- Research work should continue when assurance infrastructure fails, but an accepted/reviewed promotion must not be forged or silently bypassed.
- Expensive or complex mechanisms should earn inclusion through scoped empirical benefit rather than architecture preference.

## Validation/research concerns

The owner wants the project to be made properly even if the first implementation is small. Candidate techniques discussed include:

- PDD/SDD and explicit invariants;
- failure-mode register;
- deterministic unit/contract/integration tests;
- property/state-machine testing where state transitions matter;
- metamorphic relations;
- mutation testing for critical deterministic checks;
- fault injection/crash/replay/rebuild tests for persistent boundaries;
- adversarial review distinct from ordinary validation;
- benchmark-first evaluation for fallible quality claims;
- public development sets versus hidden/confirmatory evaluation;
- dataset manifests/version identity;
- composition tests and layer ablations;
- explicit residual risk and kill/no-benefit outcomes.

The project should avoid turning all of these into ritual requirements when a technique is not applicable.

## External methodology/standards research considered

Potential precedent/interoperability ideas include:

- PRISMA-style transparent research discovery/selection trails;
- Cochrane RoB 2 / GRADE-style dimension-specific evidence/risk judgments rather than one generic trust score;
- OMG SACM claim/argument/evidence structure;
- W3C PROV and RO-Crate for provenance/research packaging concepts;
- in-toto/SLSA-style attestations/receipts for exact process and artifact identity;
- TREC qrels/evaluation methodology;
- claim/evidence datasets such as SciFact/FEVER/AVeriTeC and unsupported-grounding datasets such as RAGTruth/ALCE.

These are precedents/possible interoperability targets, not requirements to import entire standards or dependencies.

## Known benchmark/data opportunities

Research identified candidate evidence sources including:

- TREC/BEIR for retrieval behavior;
- FinanceBench, FinQA, TAT-QA for finance-oriented retrieval/reasoning;
- FEVER, SciFact, AVeriTeC for claim/evidence support/refute work;
- RAGTruth and ALCE for unsupported/grounding/citation behavior;
- mechanically generated SEC temporal/version/restatement/wrong-version/evidence-root cases;
- deterministic corruption/authorization/retry/recovery/redaction/rebuild campaigns for the provenance substrate.

The project must decide which belong to which layer and must not aggregate them into one universal score.

## FOSSIL integrity questions worth testing

Research surfaced possible boundaries that should be empirically checked rather than asserted, including whole-artifact integrity verification, review-reference authority, orphan storage on failed ingest, crash/partial batch behavior, caller/service actor attribution, and whether role/quality metadata is sufficiently provenance-bound.

These are candidate findings/hypotheses, not confirmed bugs.

## Agent/harness research idea

There is interest in a bounded experiment to test whether a small local research-state/HITL layer improves cross-session/cross-model research continuity. A proposed architecture is plugin-first and transport-neutral, with local semantic operations and later thin adapters for OpenCode, another harness, and possibly MCP/ChatGPT. It should be treated as an experiment that may return `NO_MEASURABLE_BENEFIT`, not as a mandatory core dependency.

Early experiment concepts include frozen local research microworlds, forced interruption/restart, cross-model handoff, explicit review binding to exact claim/evidence, and protocol-induced failure rate. Model spend should come only after deterministic state/restart/idempotency/review-binding tests are green.

## Negative prior experience

A prior universal agent "stamp"/compliance approach failed because agents gamed the stamps, got blocked from useful work, did not know what actions to take, and the protocol was simultaneously too strict and too loose. Do not recreate that as a generic agent-control layer.

Any assurance/checklist mechanism should attach to a specific task/claim/transition and close with evidence rather than self-attestation.

## Owner preferences/constraints relevant to projectization

- Prefer empirical validation over hype.
- Prefer existing maintained systems/thin composition when they satisfy the scoped need.
- Do not broaden scope merely because a red-team finding or new technology exists.
- Preserve exact version/provenance identities for tested compositions.
- Use deterministic/no-network PR CI where feasible.
- Human review should be reserved for consequential project/research judgments, not every trivial action.
- The resulting project must remain resumable across sessions/agents without depending on hidden conversational memory.

## Candidate task

Using only this packet and the frozen PAM methodology, perform projectization preflight and produce the project-planning artifact bundle required by `OUTPUT_CONTRACT.md`.

Do not inspect the real finished Research Assurance project. The evaluator will compare your frozen output to that reference only after the run is complete.
