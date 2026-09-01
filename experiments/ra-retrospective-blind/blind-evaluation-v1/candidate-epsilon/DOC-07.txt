# Validation plan

## Validation doctrine

Validation is claim- and boundary-specific. Deterministic oracles are preferred when available; stochastic/empirical evaluation is used only for fallible quality claims; human review is reserved for consequential judgments that cannot be reduced to an objective oracle. Provenance, correctness, empirical quality, security/authorization, and review remain distinct.

A failed assurance dependency must fail closed for **promotion** while preserving an **exploration** path. No test may treat agent self-report as closure evidence when an objective artifact/test/report can exist.

## Claim/failure-surface map

| Claim or failure surface | Primary validation | Negative/fail-closed evidence | Residual risk |
| --- | --- | --- | --- |
| Promotion record/schema is structurally valid and dimension states are not collapsed | Schema validation; positive/negative fixtures; serialization round-trip | Missing dimensions/IDs, invalid state vocabulary, duplicated/conflicting evidence refs, forbidden universal verified flag | A valid structure can still contain incorrect evidence or judgments. |
| Promotion lifecycle cannot forge acceptance | Deterministic transition tests; property/state-machine testing | Invalid transition sequences, acceptance without prerequisites, unauthorized reviewer/actor, stale review binding, retry/idempotency attacks | Mis-specified policy could consistently enforce the wrong rule. |
| Evidence/source identity is exact and replayable | Hash/version/reference checks; FOSSIL contract tests; replay/rebuild tests | Altered artifact, missing root, mismatched revision, changed citation target, unavailable/partial persistence | Correct identity does not prove semantic support. |
| FOSSIL composition meets required integrity boundary | Contract/integration probe against exact FOSSIL revision | Whole-artifact corruption, failed-ingest orphan cases, crash/partial batch, retry, actor attribution mismatch, role/quality metadata tampering, redaction/rebuild cases | Probe coverage may miss storage/runtime failures outside tested conditions. |
| Exploration continues when assurance infrastructure fails | Integration/fault tests with FOSSIL/validator unavailable | Assert exploratory draft/output remains possible while accepted promotion cannot be emitted | Application code may accidentally couple exploration UX to unavailable assurance services. |
| Finance temporal/version semantics are enforced where deterministic | Generated SEC/financial fixtures; deterministic temporal/version validators | Wrong filing/version, restatement mismatch, future/stale period, identity collision | Ambiguous real-world corporate events may require domain judgment. |
| Finance numeric claims use deterministic checks where possible | Golden calculations, parser/normalization contracts, tolerance policy | Unit/scale/sign mismatch, rounding edge cases, missing denominator, wrong-period arithmetic | Extraction or semantic interpretation before calculation can still be wrong. |
| Citation/root binding is valid | Deterministic locator/span/root checks and immutable evidence fixtures | Wrong document, wrong span/root, mutated source snapshot, citation points to projection rather than authority | A perfectly bound citation can fail to support the claim semantically. |
| Retrieval quality is measured independently | Retrieval Benchmarker on immutable corpus/query/qrels manifests | Wrong corpus/config/qrels identities; result/report mismatch | Dataset representativeness and domain drift. |
| Source suitability provides incremental value | Public-development benchmark and calibration/error slices; ablation | Compare deterministic/source-authority baseline vs Source Ranker; reject if no benefit or excess false blocking | Benchmark may not represent all workflows. |
| Semantic-support/unsupported-grounding quality is bounded | Claim/evidence datasets and task-specific human/gold evaluation where applicable | Unsupported/refuted evidence, citation-supported but semantically wrong claim, adversarial distractors | No verifier/dataset establishes universal truth. |
| Hidden confirmatory material stays uncontaminated | Access/process tests with dummy restricted fixtures; evaluator-owned run | Attempted implementation-agent access; hidden IDs/labels/seeds in repo/handoff/logs; post-holdout adaptive tuning without new split | Operational access-control mistakes outside code. |
| Multi-repo report identity is reproducible | Exact composition manifest; clean-environment rerun | Mismatched component revision, unpinned config/data, report from stale dependency | Supply-chain/environment variation not captured by pins. |
| Optional mechanisms earn scope | Composition tests/ablations plus cost/friction measurement | Mechanism improves one metric but worsens false blocks, cost, latency, or protocol-induced failure beyond threshold | Threshold choice remains a project judgment. |

## Deterministic unit and contract testing

Required for:

- schema parsing/validation and evidence-reference normalization;
- exact commit/artifact/dataset/report identity handling;
- state-transition preconditions;
- authorization/review-reference binding;
- finance temporal/version and numeric checks with deterministic oracles;
- citation/root identity checks;
- adapter compatibility and incompatible-version behavior;
- handoff schema/state validation;
- local no-network check lane.

Tests must assert outputs and failure modes, not merely successful execution.

## Negative and fail-closed testing

Negative fixtures are first-class. At minimum test:

- missing, malformed, stale, or mismatched evidence identities;
- evidence content changed under the same logical description;
- wrong component/dataset revision;
- review references that do not authorize the exact proposed promotion;
- unauthorized caller/service/reviewer identity;
- replayed or duplicated request IDs;
- invalid state transitions and partial prerequisite sets;
- FOSSIL/validator outage, timeout, partial failure, and retry;
- hidden-evaluation material accidentally placed in agent-visible state;
- projection/index evidence presented as authoritative source material;
- deterministic check failure followed by an attempted silent bypass.

Expected behavior is explicit: exploratory work may continue, but no accepted/reviewed promotion artifact may be emitted without required evidence.

## Property/state-machine testing

**Applicable** because promotion and provenance interactions are stateful.

Properties include:

- acceptance is unreachable from states lacking required deterministic/review prerequisites;
- retries are idempotent or produce explicit distinct events without duplicating accepted state;
- exact evidence/review identity used by an accepted promotion remains recoverable;
- a stale/revoked/superseded review cannot silently authorize a new evidence identity;
- failures cannot skip required transitions;
- replay over the same immutable inputs yields the same deterministic gate result;
- exploration state is not destroyed merely because promotion fails.

Concurrency-specific property testing is conditional on the actual core/FOSSIL contract. Do not invent distributed/concurrent behavior if the first slice is single-process.

## Metamorphic testing

**Applicable** where exact gold outputs are hard but relations are stable.

Candidate relations:

- reordering independent evidence references does not change a deterministic decision when order has no semantic meaning;
- semantically irrelevant metadata changes do not change the decision;
- changing an evidence identity/hash/revision does invalidate a previously bound review/promotion unless explicitly re-reviewed;
- equivalent numeric representation within the declared normalization/tolerance policy preserves result;
- switching to a wrong temporal/version identity changes validity as expected;
- adding an optional Source Ranker signal cannot alter a deterministic integrity failure into acceptance.

Metamorphic relations must be documented per validator; no generic requirement applies where no trustworthy relation exists.

## Mutation testing

**Applicable** to critical deterministic gate and validator code because ordinary unit tests can pass while failure checks are accidentally weakened.

Targets:

- authorization/review binding;
- state-transition guards;
- exact identity/hash/revision comparison;
- finance temporal/version and numeric validators;
- fail-closed adapter error handling.

A mutation report should identify surviving mutations. No arbitrary universal score is required; critical surviving mutations must be reviewed and either killed with tests or accepted with rationale.

Mutation testing is **not applicable** to prose artifacts or opaque third-party systems where source mutation is unavailable; use contract/fault testing instead.

## Fault injection, crash, replay, rebuild, and redaction

**Applicable** at persistent/provenance boundaries, especially the FOSSIL integration.

Campaigns should include:

- failure before/after artifact ingest and before/after promotion receipt binding;
- partial batch/crash recovery;
- retry after ambiguous outcome;
- orphan storage behavior on failed ingest;
- replay from immutable evidence and append-only history;
- rebuild of projections/indexes from authoritative artifacts/history;
- redaction/rebuild semantics and citation/reference behavior after redaction;
- actor/service attribution under failure/retry;
- dependency unavailable or incompatible revision.

The campaign records observed behavior; it must not convert hypotheses in the research packet into assumed defects.

## Adversarial review

**Applicable** and separate from ordinary validation. Reviewers should attempt to:

- forge or bypass accepted promotion;
- bind a review to different evidence/claim/revision;
- exploit stale state or retry ambiguity;
- present provenance as semantic correctness;
- smuggle hidden confirmatory information into agent-visible state;
- use a high empirical score to override a deterministic integrity/authorization failure;
- expand an optional mechanism into mandatory runtime scope without entry evidence;
- cross repository ownership boundaries or use unpinned composition results.

Findings receive `mitigate_now`, `measure`, `defer`, `not_applicable`, or `reject` disposition under the scope-admission rule; discovery alone does not expand current scope.

## Benchmark, dataset, and holdout methodology

### Layer separation

Do not aggregate heterogeneous layers into a single score.

- **Retrieval:** use Retrieval Benchmarker with immutable corpora/queries/qrels. Candidate finance datasets include FinanceBench, FinQA, and TAT-QA where task fit is established; TREC/BEIR may be used for general retrieval behavior but do not substitute for finance validity.
- **Finance reasoning/temporal correctness:** use finance datasets plus mechanically generated SEC temporal/version/restatement/wrong-version/evidence-root cases.
- **Claim/evidence support:** FEVER, SciFact, AVeriTeC are candidate evaluation sources where task alignment is justified.
- **Unsupported grounding/citation behavior:** RAGTruth/ALCE are candidate sources where their labels map to the scoped output claim.
- **Source suitability:** evaluate Source Ranker separately against a task-specific source/claim judgment set.

Every dataset use requires a manifest recording source/version/split/checksum, task mapping, exclusions, preprocessing, metric definition, and any license/access constraint.

### Public development versus hidden confirmation

Use public/development material for implementation, debugging, prompt/model/configuration tuning, and error analysis. If a reported empirical claim is adaptively optimized, a hidden/confirmatory suite is required and controlled by an evaluator/owner inaccessible to implementation agents.

Before hidden execution freeze:

- exact component revisions;
- configuration/model/prompt identifiers;
- dataset manifest/protocol version;
- metrics and decision thresholds;
- allowed report contents.

After hidden execution, do not tune on revealed failures and rerun the same hidden material as if it remained confirmatory. A changed system requires a new valid confirmatory split/run.

If a claim is purely deterministic and contamination is irrelevant, hidden holdout is **not applicable**; deterministic fixtures and independent review are sufficient.

## Composition tests and ablations

**Applicable** to optional fallible layers.

Evaluate at least:

1. deterministic/domain checks + FOSSIL provenance baseline;
2. retrieval improvements/configurations independently;
3. baseline plus Source Ranker only if its entry experiment is run;
4. any later claim verifier as a distinct layer;
5. end-to-end application composition after each layer is independently characterized.

Record incremental benefit, false acceptance/rejection effects, latency/cost, and protocol-induced failure. A layer that provides no measurable scoped benefit is killed/deferred rather than preserved for architecture completeness.

## Reproducibility evidence

Each material report must preserve:

- exact Git revisions/releases of all participating repositories;
- dependency/environment lock identity;
- test/benchmark command and configuration;
- dataset/corpus/query/qrels manifest checksums;
- random seeds where relevant and non-secret;
- produced ranking/report/artifact identity;
- FOSSIL receipt/reference identity where the report or decision is promoted;
- known nondeterminism and reproducibility tolerance.

At least one clean-environment rerun is required before release claims.

## Cost, friction, and protocol-induced failure

Measure the methodology as part of the product boundary. Relevant metrics include:

- runtime/validation latency added to a promotion;
- researcher/operator steps and interruptions;
- false block/reject rate where a reviewable ground truth exists;
- retry/recovery burden during dependency failure;
- Source Ranker/verifier/model spend when evaluated;
- rate of failures caused by the protocol rather than the research task;
- time/effort to resume from structured handoff.

Human review should remain focused on consequential judgments, not trivial transitions.

## Residual risk register categories

Release evidence must keep at least these residual-risk categories distinct:

- integrity/provenance identity;
- semantic correctness/support;
- retrieval/source suitability empirical uncertainty;
- temporal/numeric/domain validity;
- security/authorization/review authority;
- hidden-evaluation contamination;
- dependency/version drift;
- operational availability and fail-closed behavior;
- cross-session continuity/stale handoff risk.

A green category does not imply other categories are green.

## Techniques explicitly not universally required

- **Formal methods/model checking:** conditional. Apply only if the implemented state/concurrency problem becomes complex enough that state-machine/property tests leave material risk and the expected value justifies it.
- **Mutation testing of third-party code:** not applicable when source/control is unavailable; contract and fault testing substitute.
- **Hidden holdout for deterministic structural claims:** not applicable because adaptive contamination is not a meaningful threat.
- **Graph-specific validation:** not applicable while GraphRAG is out of scope.
- **Cross-domain benchmark packs:** not applicable until another domain is admitted.
- **Per-action human review:** rejected; reserve human judgment for consequential projectization, promotion, waiver, and release decisions.
