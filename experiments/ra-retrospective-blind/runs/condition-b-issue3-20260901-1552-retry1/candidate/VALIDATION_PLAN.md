# Validation plan

## Validation principles

- Match evidence to the claim/failure surface; do not use provenance evidence to close semantic-quality claims or benchmark scores to close deterministic integrity claims.
- Prefer deterministic oracles where available.
- Make negative/fail-closed behavior first-class evidence for consequential promotion.
- Keep development benchmarks and hidden confirmation separate when adaptive tuning is possible.
- Pin exact component/dataset/config/policy identities for every composition claim.
- A failed experiment, killed mechanism, narrowed claim, or blocked release is valid evidence; self-attested success is not.

## Claim-to-validation map

| Claim / failure surface | Primary validation | Required negative evidence | Closure evidence |
| --- | --- | --- | --- |
| Required evidence cannot be bypassed at acceptance | Unit + contract + integration; promotion state-machine/property tests | Missing dimension, invalid type, stale locator, unresolved exact revision, unauthorized actor/reviewer, replay mismatch | Deterministic test IDs + CI run |
| Exploration continues after assurance failure without forging acceptance | Integration/state-machine tests | Assurance dependency unavailable, validator failure, rejected review; assert no accepted transition while exploratory output remains possible | Integration artifacts + CI |
| Replay identity is exact and reconstructable | Schema/contract tests; replay round-trip; component pin manifest | Moving branch/latest, mismatched hash/revision, missing dataset split/config/policy version, stale receipt | Replay artifact + exact commit/dataset/config identities |
| FOSSIL properties relied on by coordinator are real | Contract tests + corruption/fault/retry/crash/rebuild/redaction campaigns | Whole-artifact corruption, orphan/failed ingest, partial batch/crash, wrong actor, stale review reference, metadata tamper, rebuild mismatch as applicable | Pinned FOSSIL revision + contract report; failures explicitly dispositioned |
| Finance temporal/version/numeric/identity validity is deterministic where feasible | Deterministic domain contract tests; generated cases | Wrong filing/version, restatement mismatch, as-of leakage, wrong evidence root, numeric corruption/rounding-boundary cases | Test corpus manifest + CI |
| Human review is bound to exact evidence | Integration/authorization tests | Modify claim/evidence/policy/component after review; wrong actor/authority | Test IDs + reviewed policy |
| Retrieval quality is measured independently | Retrieval Benchmarker on immutable public dev corpora/queries/qrels | Corrupt qrel/dataset identity; missing persisted ranking/report; configuration mismatch | Dataset manifest + persisted ranking/report + exact benchmarker revision |
| Source Ranker adds value, if admitted | Predeclared bounded benchmark + baseline + ablation | No-benefit/calibration/friction regression must be reportable and kill admission | Benchmark/ablation report; `NO_MEASURABLE_BENEFIT` allowed |
| Semantic/grounding mechanism adds value, if later admitted | Task-specific claim/evidence benchmark; separate hidden confirmation if adaptive | Unsupported/refuted/mis-cited examples; contamination leakage | Task report only; cannot upgrade provenance/retrieval dimensions |
| Hidden confirmatory material remains hidden | Access separation + schema/fixture checks + evaluator separation | Attempt to place labels/answers/seeds/result-bearing fields in handoff/dev fixture | Negative tests + confirmatory-run attestation |
| Cross-repository composition is reproducible | Contract/integration tests on exact revisions; lock/manifest checks | Child revision drift, adapter mismatch, stale result identity | Composition manifest + child commit/PR/test evidence |
| Handoff resumes safely | Schema tests + deterministic resume reconciliation | Stale coordinator SHA, stale child revision/PR/CI, hidden-eval field | Handoff schema tests + resume test |
| Protocol overhead remains acceptable | Instrumented cost/friction measurement | Excessive blocked exploration, review frequency, latency, repeated manual reconciliation | Friction report and kill/redesign thresholds |

## Deterministic unit, schema, contract, and integration testing

Required for coordinator-owned structural and state claims. At minimum cover:

- evidence-dimension schema and state-transition legality;
- exact identity/reference resolution rules;
- authorization/reviewer binding;
- deterministic finance temporal/version/numeric contract;
- adapter contracts with each admitted existing system;
- replay descriptor round-trip;
- handoff schema and stale-state reconciliation.

Ordinary PR CI should be deterministic and no-network where feasible. Networked/system benchmark runs belong in separate integration/evaluation lanes with persisted artifacts.

## Negative and fail-closed testing

Required because the accepted-promotion boundary is consequential. Negative fixtures must prove that invalid, incomplete, stale, unauthorized, or unresolvable evidence cannot become accepted. Dependency failure may degrade assurance availability but cannot synthesize a successful receipt/review.

## Property/state-machine testing

Applicable to:

- promotion lifecycle;
- retry/idempotency around persistent adapter boundaries;
- review binding/invalidation after evidence mutation;
- current handoff lifecycle where stale-state transitions matter.

Not required for stateless pure metric formatting or simple immutable manifest parsing when exhaustive fixture tests are cheaper and clearer.

## Metamorphic testing

Applicable where invariants should survive representation-preserving transformations, for example:

- reordering evidence dimensions must not change semantic promotion disposition;
- reordering independent manifest entries must not alter exact resolution result;
- replay/serialization round-trips preserve identities;
- retrieval report ordering/serialization transformations that should not change computed metrics.

Not a substitute for domain gold data when semantic correctness depends on external truth.

## Mutation testing

Apply selectively to critical deterministic gate code: missing-evidence checks, authorization/review binding, exact-identity matching, temporal/version checks, and accepted-transition guards.

Do **not** apply mutation scores to stochastic model quality as a proxy for semantic performance. Run mutation work after the deterministic core is stable enough that surviving mutants are actionable.

## Fault injection, crash/retry/rebuild, and adversarial review

Fault injection is required at persistent/composed boundaries where the program relies on recovery/replay behavior, especially the FOSSIL adapter and coordinator retry/idempotency logic.

Adversarial review is a separate lane after ordinary validation. It targets bypass, stale authority, forged/mismatched receipts, partial failure, hidden-holdout leakage, actor confusion, misleading aggregate reporting, and scope-expansion pressure. Findings do not automatically become current work; they receive an explicit scope disposition.

## Benchmark, dataset, and holdout methodology

### Dataset identity

Every dataset/evaluation slice must have a manifest recording source, version/hash, split, task definition, metric version, preprocessing/configuration, and license/usage constraints as applicable.

### Layer-specific development evaluation

- **Retrieval**: TREC/BEIR or finance-oriented corpora/qrels where they match the question; Retrieval Benchmarker is the evaluation engine.
- **Finance retrieval/reasoning**: bounded FinanceBench, FinQA, and/or TAT-QA tasks as justified by the exact claim.
- **Semantic claim support/refute**: FEVER/SciFact/AVeriTeC only if a claim-verification mechanism is admitted.
- **Unsupported/grounding/citation behavior**: RAGTruth/ALCE only if that layer is explicitly being evaluated.
- **Temporal/version integrity**: mechanically generated SEC wrong-version/restatement/as-of/evidence-root cases remain deterministic and are not merged into stochastic quality scores.
- **FOSSIL integrity/recovery**: deterministic corruption/authorization/retry/recovery/redaction/rebuild campaigns, not an LLM benchmark.

### Hidden confirmation

Use hidden/confirmatory material only for claims that were adaptively tuned or otherwise contamination-sensitive. Implementation agents may know the protocol and public development task but not hidden result-bearing data. Freeze the candidate composition before confirmation; no same-candidate tuning after results.

Hidden holdouts are **not applicable** to purely deterministic validators whose complete oracle is generated/known and not adaptively selected from a secret test set.

## Composition tests and layer ablations

Required for any claim that a composed mechanism adds value. Compare the smallest baseline against each added layer and report deltas per metric/failure surface. Source Ranker, claim verification, and graph retrieval each require an explicit incremental-benefit/kill result before becoming dependencies.

## Reproducibility evidence

Every material report/release should be replayable from:

- coordinator exact revision;
- exact revisions of admitted existing systems;
- dependency/adapter lock;
- dataset manifest and split identity;
- configuration/policy/schema versions;
- seed where stochastic behavior exists;
- persisted rankings/reports/artifact/receipt identities;
- CI/evaluation run identity.

A moving branch or an unpinned “latest” cannot close reproducibility.

## Cost, friction, and protocol-induced failure

Measure at least:

- added promotion latency;
- number/rate of human review interventions;
- assurance-infrastructure failure rate;
- rate of useful exploration blocked by protocol (target: none by design, except external system limitations);
- retry/reconciliation burden;
- benchmark/model compute cost for optional mechanisms;
- agent/harness continuity overhead if that experiment is run.

Kill/redesign a mechanism when its scoped quality/continuity benefit is absent or smaller than its protocol-induced failure/friction cost.

## Residual risk

Track separately:

- semantic claims without reliable gold/oracle;
- domain-authority judgments;
- external-system behavior outside the tested contract;
- hidden-evaluation leakage risk;
- stochastic reproducibility variance;
- human review error;
- exact-revision drift after evidence is produced.

Residual risk must narrow the release claim or require explicit human acceptance; it cannot be hidden inside a generic verification state.

## Techniques explicitly not required in the first slice

- **Formal verification/model checking**: not required initially because the proposed promotion state machine is small enough for exhaustive/property testing; reconsider only if concurrency/state complexity grows materially.
- **Graph-specific validation**: not applicable until graph retrieval enters scope.
- **Cross-domain benchmark packs**: not applicable until a second domain is admitted.
- **Stochastic semantic judge as sole oracle**: rejected where deterministic/gold evidence exists; may be supplementary only for an explicitly scoped task.
