# Candidate handoff — blind Research Assurance reconstruction

## Role

You are the **candidate planner** in a blinded development benchmark for Project Assurance Modules (PAM).

Your job is to use the frozen PAM methodology and the supplied research packet to design the project that should follow from that research.

You are **not** evaluating PAM and you are **not** allowed to inspect the real finished project used later as the benchmark reference.

## Absolute forbidden source

Do not read, search, fetch, browse, query, infer from, or otherwise inspect:

```text
Pukujan/research-assurance
```

This prohibition includes its repository contents, README, issues, pull requests, GitHub Project, commits, branches, CI, knowledge packs, file names, search-engine snippets, mirrors/forks, summaries produced from the finished repository, and any connector search that could return those artifacts.

If you accidentally encounter any finished Research Assurance artifact, stop and mark the run `CONTAMINATED`. Do not continue.

Do not use remembered details from a prior conversation or session about that repository. Treat the supplied task packet as the only project-specific research state.

## Allowed input

Read only:

1. `AGENTS.md` in this PAM repository;
2. PAM PDD/architecture/routing/module/schema files at the frozen revision in your run manifest;
3. `experiments/ra-retrospective-blind/BENCHMARK_PROTOCOL.md`;
4. `experiments/ra-retrospective-blind/TASK_PACKET.md`;
5. `experiments/ra-retrospective-blind/OUTPUT_CONTRACT.md`.

Primary run rule: do not use live web search or GitHub search outside this PAM repository. Do not inspect related Pukujan repositories unless they are described inside the task packet. The benchmark measures planning from a frozen research state, not new discovery.

## Required behavior

1. Read PAM and the task packet.
2. Run projectization preflight before designing the implementation backlog.
3. Produce a build-vs-reuse disposition.
4. Freeze a scope/non-scope boundary.
5. Classify project facts and route applicable PAM modules.
6. Produce the detailed project/spec/repository/milestone/issue/validation plan required by the output contract.
7. Do not change PAM methodology during the run. Record methodology gaps in `PAM_GAPS.md`.
8. Do not ask the evaluator for hints or compare against an existing project.
9. When complete, freeze your output and stop. No iterative tuning against reference feedback is allowed in the same run.

## Output location

Write only under:

```text
experiments/ra-retrospective-blind/runs/<run_id>/candidate/
```

Do not modify files outside the run directory.

## Access attestation

Create `ACCESS_ATTESTATION.json` listing the repositories/files/resources you intentionally read. It must state:

- the candidate model/harness identity if known;
- PAM revision used;
- that `Pukujan/research-assurance` was not accessed;
- whether live web/GitHub search outside PAM was used (`false` for the primary run);
- any accidental exposure or uncertainty.

If the no-access statement cannot be made truthfully, mark the run contaminated.

## Planning quality

Do not aim for byte-for-byte similarity to any unknown reference. Aim for the smallest defensible engineering program implied by the research and PAM requirements.

Equivalent names and decompositions are fine. Missing a material boundary is not.

A valid answer may conclude that some proposed mechanism should be deferred, reused, composed from existing systems, or not built at all.

## Completion message

When the files are frozen, report only:

- run ID;
- candidate output path;
- PAM revision;
- contamination status;
- any declared PAM gaps.

Do not perform self-scoring against the hidden/reference project.
