# Repository and component map

## Program shape

This is a multi-repository composition program, not a monolith. Existing independently developed systems retain their own versioning and ownership. The proposed new `promotion-assurance` repository is the only new first-slice codebase, and it pins every composition reference. Exact repository URLs and revisions are intentionally unresolved pending owner-supplied M0 inputs.

| Repository/component | Ownership | Must own | Must not own | Role |
| --- | --- | --- | --- | --- |
| `promotion-assurance` (proposed new) | Assurance program team | typed promotion contract; deterministic policy evaluator; adapter interfaces; evidence receipts; composition lock; fixtures; project-local handoff; no-network CI | raw immutable storage; source-ranker internals; retrieval engine; finance UX/business interpretation; generic agent control | Runtime integration/policy layer |
| FOSSIL Core (existing) | Existing FOSSIL owner | immutable artifacts/snapshots, citation identity, append-only history, lifecycle/lineage, rebuild/replay provenance behavior | slice-specific policy, finance workflow, benchmark evaluation | Runtime dependency through a narrow adapter |
| Financial analysis application (existing) | Existing application owner | user-facing research workflow and finance-specific interpretation | generic assurance substrate, raw provenance store, benchmarker | Runtime integration peer; receives thin adapter |
| Retrieval Benchmarker (existing) | Existing benchmarker owner | immutable evaluation corpora/queries/qrels; configurations; rankings/reports | runtime promotion decision, evidence authority, finance UX | CI/research-only dependency |
| Source Ranker (existing) | Existing ranker owner | source-suitability/claim-source research or bounded signals | universal trust decision, policy authority, storage | Optional evaluation/advisory composition |
| Dataset and holdout store (to be selected) | Dataset steward / evaluation owner | immutable manifests, access separation, labels/qrels, licensing record | runtime source of truth or agent-visible hidden answers | Research-only evidence source |
| Optional local continuity experiment | Experiment owner | frozen microworld protocol, local state/restart tests, adapter experiments | production gate or generic harness control plane | Bounded experiment, separate from core runtime |

## Cross-repository rules

- `promotion-assurance` records exact revisions/receipts for all composition tests and never claims an unpinned dependency behavior.
- A change to an existing owner is proposed as a narrow, evidence-backed issue; it is not silently forked into the new component.
- Runtime may depend only on the approved evidence substrate and approved financial adapter. Benchmarker, source-ranking experiments, datasets, and harness experiments do not become serving dependencies by convenience.
- CI has a deterministic no-network lane using committed synthetic fixtures. Network/dataset acquisition, if later necessary, is a separately identified reproducibility step with immutable manifests.
