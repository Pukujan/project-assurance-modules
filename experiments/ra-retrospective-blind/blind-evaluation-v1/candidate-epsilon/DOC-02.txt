# Build vs reuse disposition

## Decision criteria

Every material capability is compared against the same scoped criteria: required assurance behavior, exact identity/version preservation, deterministic testability, fail-closed promotion semantics, maintenance burden, security/authorization surface, licensing/operational fit, integration cost, performance/latency, replay/rebuild behavior, hidden-evaluation separation, and whether the capability is runtime-critical or evaluation-only.

A cheap contract test, spike, compatibility probe, or benchmark precedes prose-only rejection when uncertainty is material and testable. `build_new` is limited to unmet responsibilities that the supplied existing systems do not own.

## Dispositions

| Capability | Serious existing options from packet | Cheap evidence before commitment | Disposition | Rationale / reconsideration trigger |
| --- | --- | --- | --- | --- |
| Durable evidence artifacts, citations, event/history, decision lineage, replay/redaction/rebuild provenance | FOSSIL Core | Contract/integrity campaign for whole-artifact verification, review-reference authority, failed-ingest orphan behavior, crash/partial batch, actor attribution, metadata binding, retry/replay/rebuild | `reuse` | These are stated FOSSIL responsibilities. Do not duplicate storage/lineage. Reconsider only if a scoped contract probe demonstrates an unmet hard requirement that cannot be wrapped or extended safely. |
| Promotion-assurance record, dimension-specific state, deterministic policy evaluation, and fail-closed promotion decision | FOSSIL promotion boundaries plus selective SACM/PROV/SLSA-style precedent | First define the required record/state contract, then probe whether FOSSIL can carry the required references/receipts without becoming the policy engine | `build_new` | A small pure-library/schema layer is justified because no supplied capability is described as owning the cross-dimension promotion contract while the packet explicitly forbids collapsing dimensions. It must not implement persistence, retrieval, domain application logic, or a universal agent-control service. If the FOSSIL probe shows the whole contract already exists, change to `configure`/`wrap` rather than build duplicate logic. |
| Source quality and claim/source suitability scoring | Source Ranker | Freeze a scoped finance claim/source task; compare deterministic/source-authority baseline versus Source Ranker on public development data; measure incremental quality, calibration, cost, and false blocking | `more_research` | The packet states surrounding scope is broader than proven implementation. It is not a vertical-slice prerequisite. If measurable benefit is demonstrated, prefer `wrap` or `extend` over replacement. |
| Retrieval quality evaluation | Retrieval Benchmarker | Compatibility probe for selected finance corpora/query/qrels manifests and persisted report identity; establish sparse/dense/hybrid/rerank baselines | `reuse` | Evaluation machinery already exists. Keep it research/CI-only unless a future runtime requirement is separately justified. |
| Finance-domain adoption, SEC evidence handling, temporal/version semantics, user workflow | Financial analysis application | Thin adapter contract and end-to-end promotion fixture using immutable SEC-derived evidence; verify app can preserve exact evidence identity and receive promotion outcome without surrendering domain ownership | `wrap` | Use the application as first adopter; do not fork/rebuild the product into the assurance core. |
| Hidden confirmatory evaluation | Restricted evaluator-owned storage/execution plus dataset manifests; implementation agents receive only public development material and opaque manifest/version identifiers | Dry-run access-control/process test using non-secret dummy fixtures; prove build agents cannot read evaluator-only payloads | `configure` | This is primarily an access/process boundary, not a new runtime service. Use existing repository/storage/CI controls where available; do not create a bespoke secrecy platform. |
| Claim verification / semantic support model | FEVER, SciFact, AVeriTeC, RAGTruth, ALCE as candidate evaluation precedents/data; no proven runtime system supplied | Only after baseline vertical slice: quantify unsupported-synthesis residual, then run a bounded offline verifier experiment and ablation | `more_research` | Semantic correctness is distinct from provenance. Add a verifier only if it materially improves a named residual without unacceptable cost/false confidence. |
| Graph retrieval / GraphRAG | Candidate future mechanism only | Compare against existing retrieval baseline on the exact query class where graph structure is hypothesized to help | `more_research` | No current claim requires graph retrieval. Entry requires measured benefit on a scoped failure class. |
| Ontology/meta-system and cross-domain assurance packs | Candidate future mechanisms only | None in current horizon; first establish one finance-domain vertical slice and characterize what is genuinely domain-generic | `more_research` | Premature abstraction would hide domain validity assumptions. Reconsider after at least one additional materially different domain has a concrete adoption need. |
| Agent/harness local research-state/HITL layer | Plugin-first transport-neutral experiment concept; later thin adapters for harnesses | Deterministic restart/idempotency/review-binding tests first, then frozen microworld interruption/cross-model experiment with protocol-induced failure metric | `more_research` | Explicitly experimental and may conclude `NO_MEASURABLE_BENEFIT`. It must not become a core dependency or universal stamp protocol. |
| Standards interoperability/export | SACM, W3C PROV, RO-Crate, in-toto/SLSA concepts | Map only the chosen promotion record/receipt fields to a target standard when an external interchange requirement exists | `compose` | Reuse concepts and, where useful, export adapters. Do not import an entire standard merely for architectural prestige. |

## Bespoke implementation boundary

The only presently justified `build_new` capability is the smallest deterministic promotion-assurance contract/policy layer needed to keep assurance dimensions separate and bind them to exact evidence/review references. Its authorization is conditional on the first FOSSIL contract probe: if the reusable substrate already exposes equivalent semantics, the bespoke layer must shrink or be replaced by configuration/wrapping.

Concrete unmet scoped responsibilities that justify this thin layer from the supplied packet are:

1. a project-owned dimension-specific promotion record rather than one universal verified state;
2. deterministic evaluation of required fields/check results and promotion transition preconditions;
3. a fail-closed promotion outcome that still leaves exploration available;
4. extension points for domain-specific deterministic checks without moving domain logic into the core;
5. exact binding to external provenance/benchmark/review evidence without owning those systems.

No new persistence engine, retrieval engine, graph store, model verifier, workflow control plane, or generic agent-governance service is authorized.

## Residual uncertainty and review gate

This candidate preflight records dispositions but does not invent empirical probe results or human approval. Before implementation starts, the project owner must review the material dispositions, and the cheap probes identified above must be executed where they determine whether a bespoke or reusable boundary is correct.
