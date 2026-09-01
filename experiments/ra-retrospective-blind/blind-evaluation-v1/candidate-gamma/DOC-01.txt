# Research handoff — promotion assurance program

## Problem and intended outcome

Create the smallest defensible software/research program that makes a consequential promotion — a conclusion, benchmark result, architecture decision, or shared knowledge item — carry replayable evidence for the particular assurance dimensions it claims. A failed gate must not stop exploration, but it must not create an accepted or reviewed promotion by omission or forgery.

The first outcome is a finance-domain vertical slice that composes existing provenance and application capabilities with a thin promotion-policy layer. It records distinct results for source/artifact identity, citation binding, temporal/numeric/identity checks where applicable, semantic support, and human review. It deliberately does not emit one universal trust flag.

## Assumptions promoted into planning

- Artifact/provenance integrity is distinct from semantic support; retrieval quality is distinct from synthesis/claim quality.
- FOSSIL Core is the candidate authority for immutable evidence snapshots, event history, exact citations, promotion boundaries, and rebuild/replay behavior; its edge behavior is still a probe, not an assertion.
- Search indexes are rebuildable projections. Immutable evidence identity remains the authority.
- Numeric, temporal, identity, citation, and authorization propositions should prefer deterministic checks. A human resolves consequential judgment without a deterministic oracle; an agent assertion is not closure evidence.
- Finance is a first domain opportunity, not proof of cross-domain transfer.

## Candidate-system and evidence context

FOSSIL Core is the candidate durable evidence/lineage substrate. Source Ranker may supply bounded advisory source-suitability or claim/source-fit signals. Retrieval Benchmarker remains an evaluation-only system using immutable corpora, queries, qrels, rankings, and reports. The financial analysis application is the first real workflow integration. TREC/BEIR, finance datasets, claim/evidence datasets, grounding datasets, and mechanical SEC cases are candidate evidence sources only when assigned to a specific validation question.

## Open questions

1. Does a pinned FOSSIL interface meet whole-artifact, review-reference, cleanup, crash/replay, actor-attribution, and provenance-bound metadata needs?
2. Which finance promotion type, source authority rule, and human review authority are in the first slice?
3. Which checks are deterministic for that workflow, and what remains empirical or reviewed judgment?
4. Does Source Ranker add measured value beyond deterministic checks and review?
5. Does a retrieval configuration improve the end-to-end claim task independently of synthesis quality?
6. Does the optional agent/harness continuity experiment show enough benefit to earn inclusion?

## Constraints, non-goals, alternatives

This run performs no live discovery. Exact component refs, licenses, and interfaces are M0 owner inputs. CI should be deterministic and no-network where feasible. Hidden confirmatory material is never agent-visible where adaptation can contaminate it. The program does not govern every model response, create a generic compliance stamp, or make GraphRAG, ontology systems, claim verification, cross-domain packs, or harness adapters first-slice prerequisites. Retained alternatives and their kill triggers are in `BUILD_VS_REUSE.md` and `SCOPE.md`.
