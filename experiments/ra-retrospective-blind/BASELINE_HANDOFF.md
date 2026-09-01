# Baseline candidate handoff — blind Research Assurance reconstruction

## Role

You are the **baseline candidate planner** in a blinded project-planning benchmark.

You receive a frozen research packet and must design the engineering project that should follow from it. This baseline intentionally does **not** give you Project Assurance Modules methodology, schemas, router, modules, or checklist structure.

## Forbidden reference

Do not read, search, fetch, browse, query, infer from, or otherwise inspect:

```text
Pukujan/research-assurance
```

This includes repository files, issues, pull requests, GitHub Project, commits, branches, CI, knowledge packs, search-engine snippets, mirrors/forks, or prior summaries derived from the finished project.

Do not use remembered project-specific details from earlier chats/sessions. If you recognize or encounter finished-project details not present in `TASK_PACKET.md`, stop and mark the run `CONTAMINATED`.

## Allowed input

Read only:

- this file;
- `TASK_PACKET.md`;
- the run instructions supplied by the human launching the benchmark.

Do not read PAM PDD/architecture/routing/modules/schemas/validators or the PAM-condition `OUTPUT_CONTRACT.md`.

Primary-run rule: no live web/GitHub search outside the supplied files.

## Task

From the research packet, produce the detailed project plan you believe should exist before implementation begins.

You decide the appropriate project artifacts and decomposition yourself. Cover repository/component structure, product/design/specification needs, milestones/phases, issue hierarchy, engineering foundations, validation/benchmark strategy, scope/non-scope, continuity, provenance/reproducibility and any build-vs-reuse decisions **only if you independently judge them necessary**.

Do not optimize toward an unknown reference structure. Do not ask for evaluator hints.

## Output location

Write only under:

```text
experiments/ra-retrospective-blind/runs/<run_id>/baseline/
```

At minimum create:

- `RUN_MANIFEST.json` — run/model/harness identity and timestamps;
- `ACCESS_ATTESTATION.json` — sources actually read and contamination status;
- `PLAN.md` — complete proposed project plan;
- `ISSUES.md` or structured equivalent — executable work decomposition;
- `HANDOFF.md` — what a fresh session should know to continue the proposed projectization work.

You may add additional artifacts if your planning process requires them.

## Freeze rule

Once the run manifest is marked complete, freeze the output and stop. No reference feedback/tuning is allowed within the same run.

## Completion message

Report only the run ID, output path and contamination status. Do not self-score against the finished project.
