# Blind retrospective planning benchmark — Research Assurance

## Status

Development/conformance benchmark only. This is **not** a clean generalization benchmark because Project Assurance Modules was itself extracted from planning work performed on Research Assurance.

The benchmark asks a narrower useful question:

> Given a frozen pre-project research packet and a frozen PAM revision, can a fresh planner recover the material engineering obligations and project structure that an experienced planning process produced, without reading the finished Research Assurance repository?

A positive result supports PAM's ability to make its own extracted methodology operational. It does not prove that PAM generalizes to unrelated projects.

## Anti-overfitting boundary

The candidate planner must not read, search, fetch, browse, infer from, or otherwise inspect `Pukujan/research-assurance`, its forks/mirrors, its issues, pull requests, GitHub Project, docs, code, knowledge packs, CI, commit history, or search-engine snippets containing its finished project structure.

The candidate may read only:

1. the frozen PAM revision named in the run manifest;
2. the frozen task packet under this experiment directory;
3. explicitly supplied research artifacts listed by that task packet;
4. no other project-planning output for Research Assurance.

For the primary run, live web/GitHub search outside the allowlisted PAM paths is disabled by protocol. A separate exploratory run may test live external discovery, but it must not be mixed with the primary result.

Any access to the forbidden reference project invalidates the run. The run must include an access attestation.

## Separation of roles

Three roles are separated:

- **Benchmark designer** — prepares/finalizes the task packet, output contract, scoring dimensions, and frozen PAM revision before the candidate run.
- **Candidate planner** — fresh session/model instance that sees only the allowlisted inputs and produces the project plan.
- **Evaluator** — receives the frozen candidate output and only then compares it with the real Research Assurance project/reference state.

The candidate must not receive evaluator feedback before its output is frozen.

Using the same model family in designer/evaluator and candidate roles is permitted for this development benchmark, but the candidate must be a fresh session without the finished project context. Confirmatory generalization later requires projects not used to design PAM.

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
- making a benchmarker a mandatory runtime dependency without justification;
- creating speculative subsystems before entry criteria are met;
- omitting hidden-holdout discipline where adaptive empirical claims require it;
- collapsing component ownership into a monorepo without evidence.

## Frozen input

Primary candidate input is `TASK_PACKET.md` plus the exact PAM commit recorded in `RUN_MANIFEST.json`.

The task packet intentionally contains research conclusions, constraints, candidate systems, and unresolved questions, but excludes the finished repository tree, issue hierarchy, milestone list, final docs, CI configuration, exact component pins, and final project-tracking state.

## Candidate output

The candidate writes only under:

```text
experiments/ra-retrospective-blind/runs/<run_id>/candidate/
```

Required output is defined by `OUTPUT_CONTRACT.md` and includes at least:

- `RUN_MANIFEST.json`;
- `ACCESS_ATTESTATION.json`;
- `PROJECT_ASSURANCE.json` or YAML equivalent;
- `PROJECT_PLAN.md`;
- `REPOSITORY_MAP.md`;
- `ISSUE_PLAN.yaml`;
- `VALIDATION_PLAN.md`;
- `SCOPE.md`;
- `BUILD_VS_REUSE.md`;
- `HANDOFF_STATE.json` or equivalent structured continuation artifact.

The candidate must not modify PAM methodology files during the run. Any methodology deficiency it discovers is written to `PAM_GAPS.md` rather than patched mid-benchmark.

## Scoring dimensions

Freeze these dimensions before a candidate run. The evaluator compares candidate output with material reference obligations, not filename identity.

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

## Hard failures

Regardless of numerical score, mark the run invalid or failed when any of the following occurs:

- forbidden Research Assurance reference access;
- candidate output is influenced by evaluator feedback before freeze;
- candidate edits PAM methodology to fit the known case during the run;
- hidden/reference answer material is copied into the candidate output;
- the plan treats agent self-report as closure evidence for objective requirements;
- projectization authorizes bespoke implementation without any build-vs-reuse disposition;
- the plan has no explicit current scope/non-scope boundary for a project of this complexity.

## Interpretation bands

These are provisional development thresholds, frozen before first run:

- `90–100`: strong material reconstruction;
- `80–89`: useful but important planning gaps remain;
- `65–79`: partial transfer; PAM or planner requires substantial improvement;
- `<65`: benchmark does not support the current methodology as a reliable planning scaffold.

A high retrospective score is not a release claim. At least one later project that did not shape PAM is required before making a generalization claim.

## Generalization follow-up

After the RA retrospective is complete, freeze PAM and evaluate an unseen project using the same preflight/output/evidence concepts. The unseen case must not have been used to extract the tested module versions. That second stage is where generalization begins to be measurable.
