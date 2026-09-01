# Blind retrospective planning benchmark — Research Assurance

## Status

Development/conformance benchmark only. This is **not** a clean generalization benchmark because Project Assurance Modules was itself extracted from planning work performed on Research Assurance.

The benchmark asks two narrower useful questions:

1. Given the same frozen pre-project research packet, does PAM improve a fresh planner's recovery of material engineering obligations versus a blinded planner without PAM?
2. After PAM is frozen, how much planning quality survives when the planner/harness is weaker or different?

A positive result supports PAM's operational usefulness as a planning scaffold. It does not prove generalization to unrelated projects.

## Anti-overfitting boundary

Every candidate planner must not read, search, fetch, browse, infer from, or otherwise inspect `Pukujan/research-assurance`, its forks/mirrors, issues, pull requests, GitHub Project, docs, code, knowledge packs, CI, commit history, or search-engine snippets containing its finished project structure.

For the primary runs, live web/GitHub search outside the explicitly allowlisted experiment/PAM input is disabled by protocol. A separate exploratory run may test live external discovery, but it must not be mixed with the primary result.

Any access to the forbidden reference project invalidates the run. Every run includes an access attestation.

## Separation of roles

Three roles are separated:

- **Benchmark designer** — freezes the task packet, benchmark protocol, scoring dimensions, condition instructions and PAM revision before candidate runs.
- **Candidate planner** — fresh session/model instance that sees only the inputs allowed for its condition and produces a frozen project plan.
- **Evaluator** — receives frozen candidate output and only then compares it with the real Research Assurance reference state.

The candidate must not receive evaluator feedback before its output is frozen. No same-run tuning against reference failures is allowed.

Using Sol for designer/evaluator and a fresh cloud Sol session as candidate is permitted for this development benchmark, but the candidate must have no finished-project context. A later unseen project is required for generalization evidence.

## Experimental conditions

### Condition A — blinded Sol baseline

Purpose: estimate what a strong planner can recover from the research packet without PAM.

Candidate receives only:

- `TASK_PACKET.md`;
- `BASELINE_HANDOFF.md`;
- no PAM methodology/spec/module/router files;
- no finished Research Assurance artifacts.

The baseline is deliberately not given a PAM-shaped checklist or required file tree. It produces a free-form but durable engineering project plan bundle in its run directory.

### Condition B — blinded Sol + PAM

Purpose: estimate incremental planning value of PAM with planner capability held approximately constant.

Candidate receives:

- the same `TASK_PACKET.md`;
- exact frozen PAM revision;
- `CANDIDATE_HANDOFF.md`;
- PAM PDD/architecture/routing/schemas/modules/validators;
- `OUTPUT_CONTRACT.md`;
- no finished Research Assurance artifacts.

Primary effect estimate:

```text
PAM planning effect = score(Sol + PAM) - score(Sol baseline)
```

The benchmark should report both total score delta and dimension-level deltas. A strong absolute score with no improvement over baseline is weak evidence that PAM itself helped.

### Condition C — weaker/different planner + PAM

Run only after A/B are frozen. Terra/Luna or other lower-cost planners receive the exact same PAM revision and task packet as Condition B.

Purpose: test whether PAM reduces dependence on planner quality.

Useful diagnostics include:

- score retention relative to Sol + PAM;
- critical-boundary omission rate;
- unnecessary complexity;
- protocol-induced failure/bureaucracy;
- ability to produce valid manifests/handoffs;
- whether the weaker planner stays inside routed scope.

A lower byte-level similarity is irrelevant. Material obligation coverage is what matters.

### Optional Condition D — weaker/different planner baseline

If cost permits, run the same weaker planner without PAM. This allows a second difference estimate and helps distinguish a generally strong prompt from methodology transfer.

## Why byte-for-byte reproduction is not the target

The reference repository contains historical naming, ordering, and incidental choices. A planner can be materially correct while choosing different filenames, issue numbers, or equivalent decomposition.

Score **semantic planning equivalence**, not textual imitation.

Examples of acceptable equivalence:

- `SYSTEM_DESIGN.md` versus `specs/SDD.md` if the same design obligations are covered;
- one parent issue plus four child issues versus two parent issues plus equivalent executable children;
- different milestone labels with equivalent dependency/phase gates.

Examples of material disagreement:

- treating provenance as semantic correctness;
- omitting fail-closed validation for a claimed integrity boundary;
- making an evaluation-only benchmarker a mandatory runtime dependency without justification;
- creating speculative subsystems before entry criteria are met;
- omitting hidden-holdout discipline where adaptive empirical claims require it;
- collapsing independently owned components into a monolith without a scoped reason.

## Frozen input

The task packet intentionally contains research conclusions, constraints, candidate systems, validation concerns and unresolved questions, but excludes the finished repository tree, issue hierarchy, milestone list, final docs, CI configuration, exact component pins and final project-tracking state.

Freeze the task packet bytes and PAM revision before Condition A starts. Do not alter them between A and B.

## Candidate output

PAM candidates write only under:

```text
experiments/ra-retrospective-blind/runs/<run_id>/candidate/
```

and follow `OUTPUT_CONTRACT.md`.

Baseline candidates write only under their run directory and follow `BASELINE_HANDOFF.md`.

Candidates must not modify benchmark/PAM methodology files during a run. PAM-condition methodology deficiencies go to `PAM_GAPS.md` rather than being patched mid-benchmark.

## Scoring dimensions

Freeze these dimensions before candidate runs. The evaluator compares candidate output with material reference obligations, not filename identity.

| Dimension | Weight |
| --- | ---: |
| Problem/product scope and explicit non-goals | 8 |
| Build-vs-reuse / existing-system decision discipline | 8 |
| System/component ownership boundaries | 12 |
| Milestone/phase sequencing and dependency logic | 10 |
| Executable issue decomposition and closure evidence | 10 |
| SWE/CI foundation | 8 |
| Invariants, failure modes, and fail-closed negative validation | 12 |
| Benchmark/dataset/holdout methodology | 10 |
| Scope control and mechanism entry/kill discipline | 7 |
| Provenance/FOSSIL decision-lineage boundary | 5 |
| Multi-repo orchestration and exact revision/evidence identity | 5 |
| Structured handoff/continuity | 5 |
| **Total** | **100** |

The evaluator also records non-scoring diagnostics for unnecessary complexity, missing critical boundaries, contradictory requirements, and protocol-induced bureaucracy.

## Hard failures / invalid runs

Regardless of numerical score, mark a run invalid or failed when any of the following occurs:

- forbidden Research Assurance reference access;
- candidate output is influenced by evaluator feedback before freeze;
- a PAM candidate edits PAM methodology to fit the known case during the run;
- hidden/reference answer material is copied into candidate output;
- the plan treats agent self-report as closure evidence for objective requirements;
- the run cannot truthfully complete its access attestation.

For PAM-condition quality evaluation, also flag as a material methodology failure when projectization authorizes bespoke implementation without a build-vs-reuse disposition or has no explicit current scope/non-scope boundary for a project of this complexity.

## Interpretation

Provisional development bands for each absolute score:

- `90–100`: strong material reconstruction;
- `80–89`: useful but important planning gaps remain;
- `65–79`: partial transfer; substantial improvement needed;
- `<65`: poor reconstruction.

More important than the bands is the paired result:

```text
Sol baseline score
Sol + PAM score
Delta overall
Delta by dimension
New protocol-induced failures caused by PAM
```

A high retrospective score is not a release/generalization claim.

## Generalization follow-up

After the retrospective A/B experiment is frozen, freeze PAM and evaluate at least one materially different project that did not contribute to the tested module definitions. That unseen project is the first meaningful test of generalization.
