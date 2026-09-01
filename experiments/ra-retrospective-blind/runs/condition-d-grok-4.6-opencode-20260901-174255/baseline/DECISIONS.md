# Proposed projectization decisions

Status: proposed by baseline planner; not owner-accepted until recorded outside this frozen run.
Run: `condition-d-grok-4.6-opencode-20260901-174255`

Each decision is independent. An owner may amend one without reopening all.

## D1. Program identity

**Decision:** Create a composition/program called Replayable Promotion Program (RPP). Existing FOSSIL, Retrieval Benchmarker, Source Ranker, and the financial analysis application remain separate repositories.

**Why:** The packet already has independently developed systems. Rebuilding them would violate reuse preference. A thin program repo can pin compositions and own the promotion contract.

**Rejects:** A new monolith that reimplements provenance, retrieval eval, or the finance UI.

## D2. Product is promotion, not agent control

**Decision:** The unit of assurance is a typed promotion (claim, benchmark result, architecture decision, shared knowledge). Ordinary exploration, coding, and model responses are ungated.

**Why:** A prior universal stamp/compliance layer failed (gaming, blockage, unclear actions, too strict and too loose). The packet forbids recreating it.

## D3. Dimensioned status, no universal verified flag

**Decision:** Persist independent dimension statuses. Forbid a collapsing `verified=true` in schema, API, and UI.

**Why:** Packet: provenance/citation integrity ≠ semantic correctness; retrieval ≠ synthesis; source quality ≠ claim-source fit; domain validity does not transfer.

## D4. FOSSIL is the durable evidence store

**Decision:** Reuse FOSSIL Core for immutable artifacts, citations, append-only history, lineage, redaction/rebuild/replay. RPP stores promotion records as FOSSIL artifacts (or equivalent identities returned by the adapter).

**Why:** Packet lists FOSSIL as the durable substrate. Build-vs-reuse says do not rebuild it.

**Caveat:** Integrity hypotheses in the packet are unconfirmed. Phase 1 tests them. Promotion-accept is blocked if identity/review-binding cannot be honestly recorded.

## D5. Indexes are projections

**Decision:** Vector/graph/search indexes may exist inside apps but are not citation targets and not sole evidence authority. Replay rebuilds them from immutable artifacts.

## D6. First domain is finance; other domains are not implied

**Decision:** v0 domain pack is finance only, using the existing financial analysis application as the first user-facing loop.

**Rejects:** Legal/medical/cross-domain packs in v0.

## D7. Retrieval Benchmarker is the retrieval reporting system

**Decision:** Do not write a new retrieval eval harness. Pin Retrieval Benchmarker. Its numbers are P-BENCH `layer=retrieval` only.

**Rejects:** Averaging retrieval, citation, and claim metrics into one score.

## D8. Source Ranker is not a v0 gate

**Decision:** Keep Source Ranker pinned as research. Admit into a promotion path only after E6 comparison against a simple authority baseline. Default if unrun: out of the accept path.

## D9. Agent/harness plugin is not a core dependency

**Decision:** Optional experiment after kernel+finance loop. Plugin-first, transport-neutral. Model spend after deterministic restart/idempotency/review-binding tests. Allowed result `NO_MEASURABLE_BENEFIT`.

**Rejects:** MCP/ChatGPT adapters as prerequisites; any stamp protocol.

## D10. Hidden confirmatory material stays out of implementer context

**Decision:** Public-dev fixtures may live in RPP. Hidden confirmatory sets live outside the implementation tree. `benchmarks/HIDDEN.md` describes process, not answers.

## D11. Deterministic CI, no network on PR

**Decision:** PR CI is no-egress: schema, unit, contract, property, public-dev fixtures only.

## D12. Deferred mechanisms must be admitted

**Decision:** GraphRAG, ontologies, claim-verification products, extra domain packs, standards importers, and red-team-inspired subsystems are candidates (`CANDIDATES.md`), not issues, until a written admission names question, cost bound, and kill rule.

## D13. Language/runtime unpinned at projectization

**Decision:** Do not freeze implementation language in this baseline. Choose at E0/E1 based on adapter cost to FOSSIL and the finance app. Kernel remains typed, testable, LLM-free.

## D14. Human review is reserved for consequential semantic/project judgments

**Decision:** P-CLAIM semantic support in v0 requires review bound to exact claim+evidence. Trivial actions do not require review. Reviewer identity is provenance.

## D15. Historical promotions are immutable

**Decision:** Corrections are new promotions that supersede by identity. Pins on a historical record do not get rewritten when dependencies evolve.
