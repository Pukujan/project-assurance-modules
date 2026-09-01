# Repository map

## Decision: multi-repository composition

Use a multi-repository program because the supplied capabilities already have independent ownership, release cadence, data/benchmark responsibilities, and failure surfaces. Create at most one new core repository for the first vertical slice: the thin assurance coordinator. Do not collapse existing systems into it.

Exact repository URLs/revisions for existing systems are not present in the frozen packet. Integration work must therefore begin by resolving and pinning exact revisions without changing ownership boundaries.

## Components

### 1. `assurance-coordinator` — new repository, proposed name only

**Owns**

- project PDD/SDD, invariants, failure-mode register, and promotion-state semantics;
- dimension-specific evidence requirement/decision schema;
- fail-closed transition logic for proposed -> reviewable -> accepted/rejected (exact vocabulary may change in design);
- exact composition/replay descriptor for component revisions, datasets, configurations, policies, and evidence locators;
- thin interfaces/adapters to existing systems;
- deterministic validators that are coordinator-owned (identity/reference/state/authorization contract checks);
- project-level benchmark manifests, composition/ablation orchestration, validation reports, and residual-risk/release evidence;
- structured handoff schema/current state for the coordinator program.

**Must not own**

- FOSSIL durable artifact/event storage internals;
- retrieval algorithms/ranking implementations already owned by Retrieval Benchmarker;
- Source Ranker algorithms beyond a thin optional adapter;
- finance application business logic, SEC ingestion, or domain-authority policy that belongs to the application;
- graph/vector indexes as evidence authority;
- model/harness transport implementations unless later admitted as a separate bounded experiment.

**Runtime dependencies**

- FOSSIL Core through a narrow pinned contract when promotion uses durable provenance/lineage.
- Financial application contract only at the integration boundary used by the first-domain workflow.

**Research/CI-only dependencies by default**

- Retrieval Benchmarker.
- Benchmark datasets and evaluation harnesses.
- Source Ranker until empirical entry criteria are satisfied.

### 2. FOSSIL Core — existing independently versioned system

**Owns**

Immutable artifacts/source snapshots, exact citations, append-only event/history, lifecycle/lineage, reviewed promotion/provenance behavior, redaction, rebuild, and replay capabilities within its actual tested contract.

**Must not own**

Semantic correctness, retrieval quality, source suitability, finance-domain validity, coordinator task state, or generic PAM/checklist state.

**Integration rule**

Pin the exact tested revision and record contract evidence. Do not claim candidate integrity/authority properties until the specified corruption/retry/crash/rebuild/actor/review-reference probes pass.

### 3. Retrieval Benchmarker — existing independently versioned evaluation system

**Owns**

Immutable corpora/queries/qrels, retrieval configurations, persisted rankings, and retrieval reports.

**Must not own**

Production promotion authorization, semantic claim correctness, source authority, or application workflow state.

**Dependency class**

Research/CI-only for the first slice. Its reports may be evidence referenced by a promotion/release decision; the benchmarker itself is not required in the production acceptance path.

### 4. Source Ranker — existing independently versioned candidate system

**Owns**

Its actual implemented source suitability/quality and claim-source-fit behavior.

**Must not own**

Universal trust, promotion authorization, retrieval correctness, provenance authority, or semantic correctness.

**Dependency class**

Conditional experiment/research dependency until a bounded benchmark demonstrates incremental benefit. If admitted later, integration is via a thin pinned adapter.

### 5. Financial analysis application — existing independently versioned domain application

**Owns**

User-facing finance workflow, SEC/financial evidence semantics, and domain-specific temporal/version/source-authority policy exposed by its stable interfaces.

**Must not own**

Generic assurance methodology or cross-domain promotion semantics.

**Integration rule**

Use it as the first domain integration target. Pin the exact tested revision and require an explicit contract for source identity, as-of time/version/restatement semantics, numeric evidence, and promotion inputs/outputs.

### 6. Agent/HITL continuity experiment — no repository now

If admitted later, keep local semantic state/review operations in a small separate experimental package/repository with thin transport adapters. It must not become a dependency of the core coordinator until deterministic restart/idempotency/review-binding tests and the predeclared continuity experiment show measurable benefit.

## Cross-repository identity contract

Every integration/benchmark/release evidence bundle must record, as applicable:

- repository identity and exact commit/release revision;
- dependency lock/adapter version;
- dataset manifest/hash/version and split identity;
- policy/schema version;
- benchmark configuration and persisted report/artifact identity;
- source/artifact citations or receipts;
- current coordinator revision;
- validation run/CI identity.

A moving branch name or unpinned “latest” component cannot close a replay or composition requirement.

## Orchestration rule

The coordinator issue tracker may hold cross-repository dependency links, but issues that change an existing system belong in that system's own repository. Cross-repository parent work closes only when it references exact child revision/PR plus the coordinator integration evidence. Agent self-report is never sufficient closure evidence.
