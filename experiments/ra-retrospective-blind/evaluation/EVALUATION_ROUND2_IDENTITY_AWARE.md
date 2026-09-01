# RA retrospective benchmark — identity-aware robustness evaluation

## Status

This is a **second evaluator pass** over the already-frozen `ra-retrospective-blind/v0` runs. It extends the original A/B evaluation with:

- Condition C: GPT-5.6 Terra + PAM, Codex local agent
- Condition D: Grok 4.6 without PAM, OpenCode

This pass is explicitly **identity-aware and non-blind**. Two attempted vendor-blind evaluator launches failed before scoring because the anonymous bundle was incomplete and then leaked identity-bearing text from a substantive candidate artifact. Those aborted evaluator attempts produced no scores and are not used as evidence.

The vendor-awareness hypothesis therefore remains unresolved by a valid blinded evaluator experiment. Do not relabel this report as vendor-blind evidence.

Frozen PAM methodology input:

`8f4737fc212e6b09f8066d90e178aa8760e619fb`

No frozen candidate output was modified for this evaluation.

## Frozen candidate set

| Label | Condition | Planner / harness | PAM | Frozen commit |
| --- | --- | --- | --- | --- |
| A | baseline | GPT-5.6 Sol / ChatGPT | no | `0da5a62529f7e665421b3389a941d1f70f895286` |
| B1 | primary treatment | GPT-5.6 Sol / ChatGPT | yes | `0d5b6f254dc199c2be5f552b77724f3dc966a44d` |
| B2 | treatment replication | GPT-5.6 Sol / ChatGPT | yes | `658e219e46b60a1a6fe954712cba94cc846394ab` |
| C | robustness | GPT-5.6 Terra / Codex local agent | yes | `7be21dbd6735c84bd500ce4c4d5bb531d07582b4` |
| D | heterogeneous baseline | Grok 4.6 / OpenCode | no | `017a2c5516fb98e0ae40ad6bed1e3d7f2876df5e` |

C and D are **not a causal pair** because planner and harness both differ. `score(C)-score(D)` must not be called a PAM effect.

## Frozen rubric

The original 12-dimension / 100-point rubric is unchanged.

| Dimension | Weight | A | B1 | B2 | C Terra+PAM | D Grok no-PAM |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Problem/product scope and explicit non-goals | 8 | 8 | 8 | 8 | 8 | 8 |
| Build-vs-reuse / existing-system decision discipline | 8 | 8 | 8 | 8 | 8 | 8 |
| System/component ownership boundaries | 12 | 10 | 11 | 11 | 11 | 10 |
| Milestone/phase sequencing and dependency logic | 10 | 9 | 9 | 9 | 9 | 10 |
| Executable issue decomposition and closure evidence | 10 | 10 | 10 | 9 | 9 | 10 |
| SWE/CI foundation | 8 | 8 | 8 | 8 | 8 | 8 |
| Invariants, failure modes, and fail-closed negative validation | 12 | 12 | 12 | 12 | 11 | 12 |
| Benchmark/dataset/holdout methodology | 10 | 10 | 10 | 10 | 10 | 10 |
| Scope control and mechanism entry/kill discipline | 7 | 6 | 7 | 7 | 7 | 7 |
| Provenance/FOSSIL decision-lineage boundary | 5 | 3 | 4 | 4 | 4 | 4 |
| Multi-repo orchestration and exact revision/evidence identity | 5 | 3 | 5 | 5 | 5 | 5 |
| Structured handoff/continuity | 5 | 3 | 4 | 4 | 4 | 3 |
| **Total** | **100** | **90** | **96** | **95** | **94** | **95** |

Original controlled Sol contrast remains:

`B1 - A = +6`

B2 replication relative to A remains:

`B2 - A = +5`

No causal delta is assigned to C versus D.

## Condition C — Terra + frozen PAM

**Score: 94/100.**

Terra retained nearly all material obligations recovered by the Sol+PAM runs while using a different planner/harness. The planning bundle has strong explicit scope, build-vs-reuse disposition, multi-repository ownership, exact composition identity, phased gates, benchmark/holdout separation, bounded mechanism admission, and machine-readable handoff state.

### Strengths

- `BUILD_VS_REUSE.md` distinguishes `reuse`, `build_new`, `wrap`, `configure`, `compose`, `more_research`, and defer decisions, with cheap probes and reconsideration triggers. The proposed new policy/adapter package is explicitly contingent on proving an unmet contract rather than assumed necessary.
- `REPOSITORY_MAP.md` keeps FOSSIL, the finance application, Retrieval Benchmarker, Source Ranker, datasets/holdouts, and the continuity experiment under separate owners and explicitly distinguishes runtime from research/CI dependencies.
- `PROJECT_PLAN.md` has clean M0–M4 phase gates. It requires owner review and exact component references before broad implementation; FOSSIL seam probes precede the first adapter slice; deterministic/fail-closed work precedes empirical mechanism expansion.
- `VALIDATION_PLAN.md` separates deterministic, empirical, and human-review evidence, including property/state-machine, mutation, metamorphic, fault/replay/rebuild, adversarial, dataset-manifest, ablation, hidden-evaluation, cost/friction, and residual-risk controls.
- `HANDOFF_STATE.json` supplies durable current phase, blockers, validation state, exact next action, resume reconciliation, and hidden-evaluation exclusion.

### Deductions

- **Invariants/failure modes 11/12:** the run has excellent fail-closed validation semantics but does not include a comparably explicit standalone failure-mode register as rich as the strongest A/B/D artifacts. The obligations are present across the plan/validation/issues rather than frozen as one detailed register.
- **Issue decomposition 9/10:** `ISSUE_PLAN.yaml` is executable and evidence-backed, but it is deliberately compact (PA-0 through PA-8) and therefore less granular than the strongest baseline/treatment decompositions.
- **Ownership 11/12:** like B1/B2, C assumes a new `promotion-assurance` runtime/integration repository. That is defensible from the task packet but is not proven necessary, and the historical reference shows that much of the program can live as a control-plane/superproject. The architecture should remain conditional on the M0 seam/reuse probe.
- **Provenance 4/5:** runtime provenance boundaries are strong, but the portable project-decision-lineage/FOSSIL knowledge-pack governance remains thinner than the finished reference.
- **Handoff 4/5:** machine-readable continuity is present, but PAM v0 still lacks the shipped generic handoff schema/validator that its structured-handoff requirement anticipates.

### Interpretation

C is useful **planner-robustness evidence**: frozen PAM did not collapse when used by Terra in a local-agent harness. At 94, it retains about the same semantic planning quality as the Sol+PAM runs (95–96) within ordinary evaluator uncertainty.

It is not evidence that PAM caused 94 points, because there is no matched Terra no-PAM run.

## Condition D — Grok 4.6 / OpenCode, no PAM

**Score: 95/100.**

D is the most important new diagnostic because it demonstrates that a different strong planner, given the methodology-rich frozen research packet but no PAM methodology, can independently produce an extremely strong projectization plan.

### Strengths

- `PLAN.md` defines a narrow Replayable Promotion Program, explicit promotion types, ten assurance dimensions, eleven invariants, build-vs-reuse boundaries, finance-first vertical slice, deterministic versus empirical validation, public-development/hidden-confirmatory separation, exact composition lockfiles, and killable optional mechanisms.
- `ISSUES.md` is exceptionally executable. It decomposes projectization, exact pins, FOSSIL integrity campaigns, promotion kernel, deterministic checkers, finance integration, retrieval reporting, Source Ranker go/no-go, CI, and optional continuity work with evidence and non-scope on almost every issue.
- `FAILURE_MODES.md` is a concrete 21-item register covering universal verified-state collapse, stamp gaming, blocked exploration, silent accept bypass, substrate outage, index-as-authority, temporal/restatement errors, citation mismatch, stale review binding, actor spoofing, partial ingest, hidden-eval leakage, domain-transfer assumptions, unproven ranker gates, plugin/stamp regression, scope explosion, stochastic-over-deterministic checks, replay failure, and self-attestation closure.
- `VALIDATION.md` gives an applicability map rather than ritualistically requiring every technique. It correctly separates deterministic integrity tests from retrieval benchmarks and semantic/human review.
- `CONTINUITY.md` defines durable vs non-durable state and a fresh-session read order rather than depending on chat memory.

### Deductions

- **Ownership 10/12:** D proposes a new RPP program repository with a promotion kernel/runtime package. Boundaries are good, but—like the PAM-assisted candidates—the new kernel is not demonstrated as necessary relative to a lighter control-plane/integration superproject.
- **Provenance 4/5:** D understands FOSSIL's authority/lineage role and even treats architecture/knowledge promotions as typed promotion classes, but it does not fully reconstruct the historical reference's project-decision-chain knowledge-pack governance.
- **Structured handoff 3/5:** continuity prose is strong, but there is no machine-valid current-state handoff contract equivalent to the PAM treatment runs or the finished RA handoff schema/state validator.

Everything else earns full credit under the frozen rubric.

### Reference challenge / potential improvement

D is not merely a weaker imitation of the historical reference. Its explicit `P-CLAIM`, `P-BENCH`, `P-ARCH`, and `P-KNOW` promotion taxonomy is a defensible alternative conceptualization and could be useful design vocabulary. It should be treated as an `EQUIVALENT_ALTERNATIVE` or `POTENTIAL_IMPROVEMENT` where it clarifies promotion semantics, not penalized because Research Assurance used different names or repository structure.

## What the expanded benchmark now says

### 1. The original Sol A/B result remains real but narrow

For the matched Sol/ChatGPT comparison, frozen PAM improved the score from 90 to 96 (+6), mainly through operational scope/reuse gating, machine-readable project state, cross-repository closure discipline, exact identity handling, and structured continuity.

### 2. PAM appears portable across at least one different planner/harness

Terra+PAM scored 94, close to the two Sol+PAM scores (96 and 95). That is encouraging robustness evidence for the methodology representation itself.

### 3. PAM is not required for a powerful planner to do excellent work on this task packet

Grok/OpenCode without PAM scored 95. This is a critical finding, not a failure to hide.

The frozen research packet already contains a large amount of engineering methodology. A sufficiently capable planner can reconstruct most or all of the desired projectization from that packet alone. Therefore the RA retrospective is **low-sensitivity for proving broad PAM necessity**.

The correct interpretation is not "PAM adds +N for every model." It is:

- PAM can formalize and preserve projectization obligations;
- PAM appears usable by a different planner;
- but a strong planner can independently reach similar planning quality when the research packet itself is rich;
- future value must be tested on projects where methodology is *not already encoded in the input*.

### 4. The vendor-awareness hypothesis remains unresolved

The attempted vendor-blind evaluator protocol did not yield valid scores. One evaluator stopped because anonymous candidates were not actually supplied. A subsequent evaluator stopped because an allowed substantive document still contained an identity-bearing run identifier.

Those stops were correct and produced no score evidence.

This identity-aware score of Grok at 95 is at least inconsistent with a crude claim that an OpenAI evaluator necessarily discounts a cross-vendor plan. However, because evaluator identity awareness was present, it does **not** test same-vendor preference rigorously.

Do not spend more time repairing the RA blind bundle now. If evaluator-vendor bias becomes release-significant, design the blind packaging correctly from the start on a future unseen-project benchmark with deterministic leakage scanning.

## Protocol findings

The experiment surfaced two methodology/infrastructure gaps in addition to the original PAM gaps:

1. **Fresh-workspace bootstrap:** a capable fresh agent starting from an empty workspace needs an exact-revision acquisition/verification protocol. Terra correctly stopped before guessing.
2. **Blind-evaluation packaging:** removing manifests is insufficient. Identity can leak from substantive handoff/run text. A future blind benchmark needs a sanitizer/leak validator with fail-closed token/pattern scanning plus human semantic review before evaluator release.

These should be recorded as future methodology/benchmark infrastructure work, not patched into the already-frozen v0 experiment.

## Decision

**Close the RA retrospective development benchmark after preserving these results.**

The evidence is now sufficient for the purpose of v0 development:

- matched Sol A/B: 90 -> 96;
- Sol+PAM replication: 95;
- Terra+PAM robustness: 94;
- heterogeneous strong no-PAM Grok baseline: 95;
- fresh-workspace bootstrap failure exposed safely;
- blind-evaluator packaging failure exposed safely.

Further retrospective runs have sharply diminishing information value and increase the risk of tuning PAM to its own source project.

## Next methodological move

Start a new PAM revision only after the v0 result is preserved. The highest-confidence bounded changes are:

1. generic structured-handoff schema + validator, extracted from the working Research Assurance implementation;
2. first-class bootstrap/acquisition contract for an empty workspace using exact methodology revision verification;
3. profile schema/selection;
4. a small repeated set of modules for planning foundation, SWE/CI foundation, benchmark/holdout integrity, and decision-lineage/provenance—only where repeated evidence supports portability;
5. RA-plugin as the second real adopter;
6. then an **unseen project that did not shape PAM** as the first real transfer/generalization benchmark.

The unseen-project benchmark should emphasize downstream outcomes and independently specified obligations rather than similarity to a historical reference architecture.
