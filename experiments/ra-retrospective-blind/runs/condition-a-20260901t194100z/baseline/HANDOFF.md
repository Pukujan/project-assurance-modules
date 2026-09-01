# Baseline continuation handoff

## Run identity

- Condition: A (baseline candidate planner)
- Run ID: `condition-a-20260901t194100z`
- Frozen input revision: `8f4737fc212e6b09f8066d90e178aa8760e619fb`
- Output branch: `experiment/ra-retrospective-blind/condition-a-20260901t194100z`
- Output directory: `experiments/ra-retrospective-blind/runs/condition-a-20260901t194100z/baseline/`

## What this baseline proposes

The project is a narrow promotion-assurance system, not a universal agent-control framework. It protects consequential transitions from exploratory/candidate research into accepted/reviewed/shared state. Failed assurance gates block only the protected promotion; they do not block continued research.

The central representation is a promotion receipt that binds an exact candidate to exact evidence, dimension-specific assurance results, policy/version identity, actor/authorization evidence, human review where required, and replay metadata. The system intentionally does not collapse provenance, citation, temporal, numeric, source, retrieval, semantic, authorization, and review judgments into one `verified` flag or universal score.

## Planned architecture

Keep the new implementation small and composition-oriented:

- a core promotion state machine and receipt model;
- deterministic checks for identity/integrity, citations, temporal/version rules, numeric rules, and authorization;
- a finance domain policy for the first vertical slice;
- narrow adapters to existing FOSSIL Core, Source Ranker, and Retrieval Benchmarker capabilities;
- a finance application integration boundary;
- reproducibility/evaluation manifests and runners;
- no mandatory GraphRAG, ontology/meta-system, or agent/harness layer in the initial core.

Indexes are rebuildable projections and must not become the sole evidence authority.

## Build-versus-reuse decisions

- **FOSSIL Core:** reuse conditionally as provenance/history substrate. Before depending on it, empirically test whole-artifact integrity, review-reference authority, orphan storage after failed ingest, crash/partial-batch behavior, caller/service attribution, and provenance binding of role/quality metadata.
- **Retrieval Benchmarker:** reuse for immutable retrieval evaluation and persisted rankings/reports; do not rebuild retrieval benchmarking.
- **Source Ranker:** integrate only behind a narrow adapter and only make it mandatory if scoped finance evaluation shows material benefit over deterministic/domain-policy baselines.
- **Financial application:** use as first realistic domain consumer, while keeping assurance core application-neutral.
- **Semantic verifier:** benchmark a minimal/simple approach before building bespoke infrastructure.
- **Graph/ontology mechanisms:** defer pending a demonstrated unmet failure mode and positive ablation.
- **Agent/harness continuity layer:** optional experiment after deterministic substrate is green; `NO_MEASURABLE_BENEFIT` is a valid terminal result.

## Milestone sequence

1. Scope/contracts/reproducibility foundation.
2. Deterministic promotion substrate and FOSSIL boundary proof.
3. Finance end-to-end vertical slice.
4. Empirical retrieval/source/semantic layers with ablations and kill criteria.
5. Adversarial review and hidden confirmatory evaluation after implementation freeze.
6. Optional research-state/HITL continuity experiment off the core critical path.
7. Hardening, deterministic CI, runbook, and first release evidence bundle.

The detailed executable work graph is in `ISSUES.md`; project rationale, invariants, acceptance criteria, validation strategy, and proposed structure are in `PLAN.md`.

## Immediate next actions for an implementation session

A fresh implementation session should start at Milestone 0 and should not begin by building fallible/expensive mechanisms.

First actions:

1. Write the problem/scope specification and protected promotion boundary.
2. Define the dimension-specific assurance model.
3. Specify the promotion state machine, especially illegal transitions, review invalidation, and supersession.
4. Define evidence-reference, promotion-receipt, and reproducibility/dataset manifest schemas.
5. Specify the first finance scenario and finance policy, including mechanically generated wrong-version/restatement/numeric/citation/authorization cases.
6. Create the failure-mode register with owners/severity/tests/residual risk.
7. Define FOSSIL, Source Ranker, and Retrieval Benchmarker adapter contracts without assuming untested behavior.
8. Define public-development versus hidden-confirmatory evaluation separation before adaptive benchmark work begins.

Only after these contracts exist should implementation proceed to the deterministic state machine/checks and FOSSIL boundary probes.

## Critical invariants to preserve

- Never create an accepted/reviewed promotion after a mandatory failed/missing check or missing required review.
- Never silently reuse review after candidate/evidence identity changes.
- Never destroy/block exploratory work solely because promotion failed.
- Never equate exact citation/provenance integrity with semantic truth.
- Never equate retrieval quality with claim correctness.
- Never equate general source quality with claim/source suitability.
- Never make a graph/vector index the sole evidence authority.
- Prefer deterministic checks for numeric, temporal, identity, citation, and authorization properties where possible.
- Keep hidden confirmatory material unavailable to adaptive implementation agents until the tested implementation/configuration is frozen.
- Preserve exact component, dataset, policy, schema, configuration, and model identities needed for replay.
- Do not broaden scope merely because adversarial review exposes an out-of-scope risk; make scope expansion an explicit decision.

## Validation order

1. Unit/contract tests for deterministic primitives and adapters.
2. Property/state-machine tests for protected transitions.
3. Mutation testing for critical deterministic gates.
4. Fault injection/crash/replay/rebuild tests for persistent boundaries.
5. Finance vertical-slice negative cases.
6. Retrieval/source/semantic public development benchmarks, independently and in composition.
7. Adversarial review.
8. Freeze implementation/configuration.
9. Hidden confirmatory evaluation with no same-run tuning.

Model-spend experiments for an optional agent/harness layer should occur only after deterministic state/restart/idempotency/review-binding behavior is green.

## Release evidence expected

A first release should be supported by an end-to-end reproducible finance promotion workflow, deterministic gate tests, empirical FOSSIL boundary evidence, separated retrieval/source/semantic results for any mandatory fallible layers, adversarial findings/dispositions, hidden-confirmatory manifests/results, residual-risk documentation, and a runbook that lets a fresh maintainer resume without conversational memory.

## Deliberately unresolved decisions

The following must be resolved by Milestone 0 contracts/experiments rather than guessed:

- which receipt/storage primitives already exist in FOSSIL versus belong in this project;
- the exact minimum finance policy for the first workflow;
- which source decisions are deterministic versus ranker/reviewer-assisted;
- whether a semantic verifier is necessary for the first release and, if so, which task best represents the target failure mode;
- the hidden confirmatory case design and custody mechanism;
- the severity threshold for mandatory human review;
- replay semantics when an external fallible model/provider cannot be reproduced bit-for-bit.

## Scope warning for future sessions

This baseline was produced under a blind experiment restriction. Future benchmark continuation of this run must honor the run's access attestation and must not introduce finished-project/reference information into the frozen baseline artifacts. Once `RUN_MANIFEST.json` is marked complete, these artifacts are frozen and must not be edited in this run.
