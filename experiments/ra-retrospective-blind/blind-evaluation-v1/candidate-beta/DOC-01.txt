# Research handoff

## Problem and intended outcome

Build the smallest assurance-oriented research/software program that can make a consequential **promotion** of evidence into a conclusion, benchmark result, architecture decision, or shared-knowledge item explicit, evidence-backed, and replayable.

The program is not a universal model-response governor. Exploration must continue if assurance infrastructure is unavailable or a gate fails; only the transition into an accepted/reviewed promotion must fail closed.

## Assumptions promoted into project planning

1. Assurance is multidimensional. Provenance/citation integrity, source suitability, retrieval correctness, temporal/numeric validity, semantic support, authorization, and human review must remain distinguishable.
2. No single `verified=true` or generic trust score may substitute for dimension-specific evidence.
3. Deterministic checks should replace stochastic judgment where a deterministic oracle exists, especially for numeric, temporal, identity, citation, and authorization rules.
4. Persistent evidence authority belongs in durable source/artifact systems; vector/graph indexes are rebuildable projections.
5. Adaptive empirical work can contaminate evaluation, so public development material and hidden confirmatory material require an explicit separation boundary.
6. Domain validity does not automatically transfer. The first vertical slice should use finance because the packet supplies an existing financial application plus candidate finance datasets and temporal/version semantics.
7. Complex mechanisms must demonstrate scoped incremental benefit before becoming runtime or project dependencies.
8. Exact component, dataset, configuration, and evidence identities are required for tested compositions and replay claims.

These are planning inputs from the frozen packet, not claims that the eventual implementation already satisfies them.

## Existing candidate-system context

- **FOSSIL Core**: serious existing provenance/lineage substrate for immutable artifacts, exact citations, append-only history, reviewed promotion boundaries, redaction, rebuild, and replay behavior. Candidate integrity boundaries still require empirical contract probes.
- **Retrieval Benchmarker**: serious existing evaluation system for immutable corpora/queries/qrels and sparse/dense/hybrid/rerank evaluation. It should be reused as evaluation infrastructure rather than duplicated or made a mandatory production runtime dependency.
- **Source Ranker**: serious candidate for source-quality/suitability work, but its proven scope is narrower than the surrounding research ambition. Treat inclusion as an empirical question.
- **Financial analysis application**: first domain integration target and owner of real finance workflow/domain semantics; do not rebuild it inside the assurance core.

## Unresolved questions that become explicit gates

- Which exact revisions/interfaces of the existing systems are suitable for the first tested composition? The frozen packet intentionally omits component pins.
- Do FOSSIL Core behaviors at the candidate boundaries actually satisfy whole-artifact integrity, review-reference authority, failed-ingest/orphan handling, crash/partial-batch behavior, actor attribution, and provenance binding of role/quality metadata?
- What is the smallest promotion-state model that can fail closed without blocking exploration?
- Which deterministic finance checks belong in the domain application versus the coordinator interface?
- Does Source Ranker provide incremental benefit over simpler source-policy features on a bounded finance development benchmark?
- Which empirical metrics are meaningful per layer without collapsing retrieval, source suitability, citation grounding, and semantic correctness into one score?
- What hidden/confirmatory evaluation protocol provides contamination resistance without making ordinary development impractical?
- What residual risks require human review because they do not have a reliable deterministic or benchmark oracle?

## Constraints and non-goals

- Do not access or copy the finished reference project.
- Do not rebuild FOSSIL Core, Retrieval Benchmarker, Source Ranker, or the financial application merely to centralize ownership.
- Do not require graph retrieval, claim verification, ontology/meta-systems, cross-domain assurance packs, or agent/harness adapters for the first vertical slice.
- Do not make FOSSIL the live task/checklist store or treat provenance as semantic correctness.
- Do not expose hidden confirmatory labels, seeds, answers, or equivalent leakage in implementation-agent handoffs.
- Do not require human review for trivial deterministic facts; reserve it for consequential judgments.
- Prefer deterministic, no-network PR CI where feasible.
- Preserve the ability to resume work from durable repository state instead of conversational memory.

## Alternatives and precedents already considered

External methods and standards in the packet are interoperability/design precedents, not wholesale dependency requirements: PRISMA-style research trails, dimension-specific evidence/risk approaches, SACM-style claim/evidence structure, W3C PROV/RO-Crate packaging concepts, in-toto/SLSA-style identity receipts, and TREC-style evaluation methodology.

The prior universal agent stamp/compliance design is a negative precedent and is explicitly rejected for this program.
