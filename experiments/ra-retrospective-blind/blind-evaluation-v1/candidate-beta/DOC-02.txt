# Build vs reuse disposition

## Decision criteria

Every material capability is compared against the same bounded criteria before bespoke implementation:

- fitness for the current promotion/assurance claim;
- ability to preserve exact identity/replay evidence;
- deterministic versus stochastic failure surface;
- maintenance and independent ownership;
- integration complexity and coupling;
- security/authorization implications;
- testability and no-network CI feasibility;
- whether a cheap probe can resolve material uncertainty;
- whether the capability must be runtime, research/CI-only, or a bounded experiment.

The disposition is provisional until project-owner review. Existing-system revisions are intentionally absent from the frozen packet and must be pinned before integration evidence is accepted.

## Capability register

| Capability | Serious options from packet | Cheap probe before commitment | Disposition | Rationale / boundary |
| --- | --- | --- | --- | --- |
| Durable artifacts, exact citations, event lineage, replay/redaction provenance | FOSSIL Core | Yes: contract/integrity campaign for whole-artifact verification, review authority, failed ingest/orphans, crash/partial batch, actor attribution, metadata binding, replay/rebuild | **compose** | Do not rebuild durable provenance. Depend only on empirically confirmed contracts and pin the exact tested revision. Provenance evidence never closes semantic-correctness claims by itself. |
| Retrieval evaluation and persisted rankings/reports | Retrieval Benchmarker | Yes: compatibility probe using a small immutable finance corpus/query/qrel fixture and persisted ranking/report identity | **reuse** | Reuse as research/CI evaluation infrastructure. It is not a mandatory production-runtime dependency of promotion decisions unless later evidence requires it. |
| Source quality / claim-source suitability | Source Ranker; simpler deterministic/domain source policy | Yes: bounded development-set comparison and ablation on finance claims/sources | **more_research** | Do not assume the broader research ambition is already implemented or beneficial. Admit only if it improves a predeclared metric without unacceptable calibration/friction cost. |
| Real finance workflow and SEC/domain semantics | Existing financial analysis application | Yes: thin integration contract for exact source/version/time identity and promotion inputs | **compose** | Use as the first domain consumer/producer. Domain policy remains owned by the application; the assurance core must not absorb the application. |
| Cross-system promotion semantics: dimension-specific evidence requirements, fail-closed acceptance, exact replay descriptor, human-review binding | FOSSIL promotion boundaries plus bespoke composition logic; no supplied system owns the complete scoped cross-system contract | Yes: paper/state-machine contract plus minimal adapter spike against pinned existing interfaces | **build_new** | A thin coordinator is justified because the supplied systems own provenance, ranking, source suitability, or domain workflow separately. The unmet requirement is the explicit cross-system promotion decision contract that preserves those ownership boundaries. It must remain small and transport-neutral. |
| Claim/evidence semantic verification | Candidate claim-verification techniques/datasets | Yes, but only after the core separates deterministic/provenance/retrieval dimensions and defines a bounded claim task | **more_research** | Not needed to prove the first coordinator/replay boundary. Any later mechanism needs a task-specific benchmark, hidden confirmation if adaptively tuned, and a kill/no-benefit result. |
| Graph retrieval / GraphRAG | Graph/vector projections and future graph mechanisms | Yes: layer ablation against simpler retrieval on a scoped task | **more_research** | Deferred. Graph/vector indexes are rebuildable projections and cannot become sole evidence authority. No first-slice claim requires graph retrieval. |
| Ontology/meta-system and cross-domain assurance packs | Conceptual future mechanisms | Not yet; no scoped current requirement | **more_research** | Deferred until a second domain exposes repeated requirements that cannot be handled by current contracts. |
| Local research-state/HITL agent continuity layer and harness adapters | Proposed plugin-first, transport-neutral experiment | Yes: deterministic restart/idempotency/review-binding microworld before any model spend | **more_research** | Keep as a bounded experiment, separate from the core runtime. `NO_MEASURABLE_BENEFIT` is an acceptable terminal outcome. |
| External provenance/assurance standards | W3C PROV, RO-Crate, SACM, in-toto/SLSA concepts | Contract/serialization mapping only if interoperability is requested | **reuse** | Reuse concepts/identifiers selectively; do not import whole standards stacks without a concrete interoperability requirement. |

## Why the thin coordinator earns `build_new`

The current program needs one capability not assigned to any supplied system: a dimension-specific promotion contract that can say, for a particular claim/task/transition, which evidence dimensions are required, which are satisfied by deterministic evidence, which require empirical reports or human review, and whether the promotion may transition to accepted state. It must also carry exact component/dataset/config identities for replay.

The coordinator **must not** duplicate immutable storage, source ranking, retrieval evaluation, domain workflow logic, or model execution. If the first adapter spike shows an existing supplied system already exposes the complete required promotion contract without violating these ownership boundaries, the disposition must be revisited from `build_new` to `wrap`/`extend`/`compose`.

## Mandatory pre-implementation probes

1. Pin exact candidate revisions of FOSSIL Core, Retrieval Benchmarker, Source Ranker (if tested), and the financial application.
2. Run the FOSSIL integrity/authority/recovery contract campaign before depending on those properties in a promotion claim.
3. Run a minimal Retrieval Benchmarker compatibility fixture before designing duplicate benchmark infrastructure.
4. Run the financial-application integration contract for exact source/time/version identity.
5. Keep Source Ranker conditional until a bounded benchmark/ablation demonstrates incremental value.
6. For the coordinator, prove the state/promotion contract with deterministic tests before adding stochastic verification or model dependencies.

## Reconsideration triggers

- Any supplied system demonstrates the full coordinator contract with stable interfaces: reconsider `build_new`.
- A candidate system cannot satisfy a required exact-identity/fail-closed contract and cannot be safely wrapped: reconsider composition or isolate it to research-only use.
- An expensive mechanism shows no predeclared incremental benefit: kill/defer it rather than expanding architecture.
