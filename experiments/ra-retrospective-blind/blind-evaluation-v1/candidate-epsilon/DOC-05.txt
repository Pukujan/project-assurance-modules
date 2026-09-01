# Repository map

## Program shape

Use a **multi-repository composition**, not a monorepo. The supplied systems are independently developed capabilities with different ownership, release cadence, trust boundaries, and runtime/evaluation roles. Collapsing them would obscure provenance identity, contaminate hidden evaluation boundaries, and make optional research components look mandatory.

Only one new runtime repository is proposed for the current horizon. Names below are logical/proposed names, not claims that repositories already exist.

## Ownership map

| Repository/component | Ownership in this program | Relationship | Runtime status | Must not own |
| --- | --- | --- | --- | --- |
| `promotion-assurance-core` (new, proposed) | Promotion record/schema; independent assurance-dimension vocabulary; deterministic transition/policy engine; evidence-reference contracts; adapter interfaces; deterministic validators that are domain-generic; project-local handoff schema/validator | New thin core | Runtime library, not service/control plane | Durable evidence storage/history; retrieval engine; financial product logic; hidden labels; generic agent governance; universal semantic verifier; graph store |
| FOSSIL Core (existing) | Immutable artifacts/source snapshots, exact citation/provenance identities, append-only history/lineage, reviewed promotion-boundary receipts, replay/redaction/rebuild behavior within its demonstrated contract | Pinned dependency behind a thin adapter | Runtime provenance dependency for accepted/reviewed promotion lineage | Semantic correctness judgment; finance-domain policy; live PAM checklist/task state; retrieval ranking |
| Source Ranker (existing) | Candidate source-suitability/quality and claim/source-fit signals | Optional adapter only after empirical entry gate | Not required in first runtime slice; research first | Universal source truth; provenance authority; promotion authorization; retrieval benchmark ownership |
| Retrieval Benchmarker (existing) | Immutable corpus/query/qrels evaluation, rankings, reports, retrieval configuration comparison | Pinned research/CI integration | **Research/CI-only**, never required merely to execute a promotion | Runtime authorization; semantic correctness; application state; FOSSIL lineage |
| Financial analysis application (existing) | First adopter workflow; SEC/financial evidence acquisition/use; domain-specific temporal/version/numeric semantics; user-facing consequences | Thin adopter adapter/integration | Runtime application, independently versioned | Generic assurance methodology; FOSSIL internals; hidden evaluator data; universal cross-domain policy |
| Confirmatory evaluation authority (restricted store/repository chosen by evaluator/owner) | Hidden/confirmatory corpora, labels, qrels, seeds/configuration that would contaminate adaptive development; execution of final confirmatory evaluation | Access-controlled evaluator boundary; implementation agents see manifests/opaque identities and returned reports only | Evaluation-only | Runtime product behavior; implementation task state; agent-visible handoff payloads |
| PAM repository (existing methodology) | Frozen methodology contract selected by `PROJECT_ASSURANCE.json` | Pinned methodology input | Development/projectization dependency only | Project runtime state; FOSSIL persistence; adopter-specific implementation |

## New core internal component boundaries

A single new repository may contain these modules/packages without turning them into separately deployed services:

1. **model/schema** — promotion record, dimension result, evidence reference, review reference, exact revision/dataset/report identity.
2. **policy/state** — allowed promotion transitions and deterministic preconditions; no model inference.
3. **validators** — generic deterministic identity/integrity/reference/authorization checks and adapter result normalization. Domain-specific numeric/temporal logic remains in adopter/domain adapters.
4. **adapters/fossil** — contract boundary to FOSSIL; no persistence duplication.
5. **adapters/domain** — interface/fixture package; finance implementation may live partly in the financial application repo to preserve ownership.
6. **handoff** — project-specific resumable state schema/validator and instructions; not a universal PAM methodology change.
7. **tests/fixtures** — deterministic positive/negative, property/state-machine, metamorphic, mutation targets, and integration fixtures using local/frozen test assets.

No network service, database, message bus, vector store, or agent-control daemon is authorized for the first slice.

## Dependency direction

```text
Financial application
        |
        v
promotion-assurance-core  ---> FOSSIL Core
        |
        +---- optional signal adapter ---> Source Ranker (only after entry gate)

Research/CI:
promotion-assurance-core + Financial application fixtures
        |
        +----> Retrieval Benchmarker
        |
        +----> public development datasets
        |
        +----> evaluator-owned confirmatory runner (hidden payload inaccessible to implementers)
```

The core may consume opaque evidence/report identifiers from evaluation systems, but Retrieval Benchmarker and confirmatory infrastructure are not runtime authorization dependencies.

## Exact identity and composition rule

Every executable integration or empirical report must record the exact tested composition, including as applicable:

- Git commit/release identity for `promotion-assurance-core`;
- exact FOSSIL Core revision/version;
- exact Financial application revision;
- exact Source Ranker revision when tested;
- exact Retrieval Benchmarker revision/configuration when used;
- dataset/corpus/query/qrels manifest identities and checksums;
- validator/policy schema version;
- benchmark configuration and report artifact identity;
- review/receipt identity for consequential promotion decisions.

A green report for one composition does not silently bless a later revision.

## Cross-repository change rule

A change that modifies a contract across repositories must close with:

1. the owning repository's tests;
2. a pinned consumer/producer contract or integration fixture;
3. an integration run against exact revisions;
4. an updated composition manifest/report;
5. explicit rollback/compatibility notes when the previous contract is no longer valid.

No repository may reach into another repository's internal storage/schema as a shortcut around a versioned public contract.

## Hidden-evaluation boundary

Hidden confirmatory payloads must be controlled by an evaluator/owner identity that implementation agents cannot access. The implementation side may hold an evaluation manifest containing non-secret metadata such as dataset family, protocol version, expected output schema, and opaque corpus identity, but not labels/answers/seeds that would enable adaptive tuning. Final reports may be promoted back into durable lineage after evaluation without exposing hidden payloads.

## Why not one repository

A monorepo would create false ownership: provenance, retrieval evaluation, finance-domain logic, optional ranking research, and hidden evaluation have independent authorities and different release/access semantics. Multi-repo pins make tested composition identity explicit and let optional mechanisms be removed without destabilizing the core.
