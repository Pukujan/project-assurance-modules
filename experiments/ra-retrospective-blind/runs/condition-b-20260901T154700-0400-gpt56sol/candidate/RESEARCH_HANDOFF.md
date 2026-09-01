# Research handoff

## Problem and intended outcome

The program must answer a bounded promotion question: when a research workflow proposes to promote evidence into a consequential conclusion, benchmark result, architecture decision, or shared knowledge, what evidence and validation justify that promotion and make the decision replayable?

The intended outcome is a small assurance-oriented research/software program with a finance-first vertical slice. It must preserve exploration even when assurance infrastructure fails, while making an accepted/reviewed promotion fail closed: a failed gate may block promotion, but must not forge acceptance, silently bypass review, or prevent ordinary exploratory work.

## Planning assumptions promoted from the frozen research packet

The following are treated as planning inputs, not as newly proven facts:

- Provenance/citation integrity and semantic correctness are separate assurance dimensions.
- Source quality and claim/source suitability are related but distinct.
- Retrieval quality and synthesis/claim correctness require separate empirical treatment.
- Numeric, temporal, identity, citation, and authorization checks should be deterministic where feasible.
- No universal `verified=true` state may collapse independently meaningful assurance dimensions.
- Graph/vector indexes are rebuildable projections, not sole evidence authority.
- Adaptive development must not expose hidden confirmatory labels/material to implementation agents.
- Domain validity does not automatically transfer across finance, legal, medical, or other domains.
- Expensive/stochastic mechanisms must earn entry through scoped empirical benefit.
- Exact revisions, artifact identities, dataset identities, and tested composition identities must be preserved.

## Existing capability context

### FOSSIL Core

Available as the primary candidate for durable immutable artifacts/source snapshots, exact citations, append-only event/history, lineage, reviewed promotion boundaries, and replay/redaction/rebuild-oriented provenance behavior. It should be reused rather than duplicated, subject to cheap contract/integrity probes for the specific boundaries raised by the packet.

### Source Ranker

Available for source suitability/quality and claim-source-fit work, but its proven implementation scope is narrower than the surrounding research ambition. It is an optional empirical layer, not a prerequisite for the first promotion path.

### Retrieval Benchmarker

Available for independent retrieval evaluation against immutable corpora/queries/qrels with persisted rankings/reports. It is a research/CI evaluation dependency, not a mandatory runtime dependency.

### Financial analysis application

Available as the preferred first adopter because the domain provides SEC/financial evidence, temporal/version semantics, and real research workflows. The assurance core must not absorb the application's domain or product responsibilities.

## Candidate external precedents

The packet identifies PRISMA-style selection trails, Cochrane RoB 2/GRADE-style dimension-specific judgments, SACM claim/argument/evidence structure, W3C PROV/RO-Crate packaging concepts, in-toto/SLSA-style exact process/artifact identity, TREC qrels methodology, and claim/evidence datasets. These are design/evaluation precedents and possible interoperability targets; none is assumed to require importing a whole standard, service, or dependency.

## Unresolved questions to answer empirically

1. Does FOSSIL Core satisfy the required whole-artifact integrity, review-reference authority, crash/partial-batch, orphan-on-failed-ingest, actor-attribution, and provenance-binding behavior for this composition?
2. What is the smallest promotion record/state machine that can keep integrity, temporal validity, numeric validity, semantic support, source suitability, and human review distinct without becoming a universal compliance layer?
3. Which finance-domain deterministic checks can be made authoritative, and which conclusions still require empirical or human judgment?
4. What retrieval baseline is achieved by the existing Retrieval Benchmarker on selected finance datasets, independent of synthesis correctness?
5. Does Source Ranker provide measurable incremental value for the scoped claim/source-suitability task after a deterministic/retrieval baseline exists?
6. What public-development/hidden-confirmatory split is required for any adaptive empirical claim, and who owns the hidden evaluator boundary?
7. Which failure modes remain after deterministic checks, provenance replay, domain checks, and review, and do any justify a later claim-verification mechanism?
8. Does the proposed agent/harness continuity experiment create measurable continuity benefit without recreating a gameable universal stamp protocol?

## Constraints and non-goals

- Do not govern every model response or ordinary coding action.
- Do not make assurance infrastructure failure block exploration; only consequential promotion is fail closed.
- Do not treat provenance as proof of semantic correctness.
- Do not aggregate heterogeneous benchmark/dataset results into one universal trust score.
- Do not expose hidden confirmatory labels, seeds, or answers to implementation agents or agent-visible handoffs.
- Do not make GraphRAG, claim verification, ontology/meta-systems, cross-domain packs, or agent/harness integration mandatory before they earn entry.
- Do not rebuild FOSSIL persistence/lineage, Retrieval Benchmarker evaluation machinery, Source Ranker functionality, or the financial application without an evidenced unmet requirement.
- Do not assume finance validation transfers to other domains.
- Do not depend on hidden conversational memory for continuity.

## Alternatives already considered

- A universal agent stamp/compliance layer is rejected based on prior negative experience: it encouraged gaming, blocked useful work, and was simultaneously too strict and too loose.
- Whole-standard adoption of SACM, W3C PROV/RO-Crate, SLSA/in-toto, PRISMA, or GRADE is not justified from the packet; selective compatibility/export may be reconsidered if it closes a concrete interoperability requirement.
- Graph/GraphRAG and claim-verification layers remain deferred until simpler layers leave a measured residual that they can plausibly reduce.
- Agent/harness integration is a bounded experiment that may legitimately conclude `NO_MEASURABLE_BENEFIT`; it is not core architecture.

## Projectization consequence

The smallest defensible program is a thin promotion-assurance contract/policy layer composed with existing independently versioned systems. It should first prove a finance-oriented vertical slice with deterministic checks, FOSSIL-backed replayable lineage, separate empirical evaluation, explicit review authority, and a hidden-confirmatory boundary. New mechanisms enter only through the scope-admission rule in `SCOPE.md`.
