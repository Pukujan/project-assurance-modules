# Blind benchmark runbook

Run the conditions as separate fresh sessions. Prefer a temporary/no-memory session if available. Do not reuse the benchmark-design conversation as candidate context.

Freeze the PAM branch/head and `TASK_PACKET.md` before Condition A. Do not edit the task packet or scoring dimensions between A and B.

## Condition A — Sol baseline

Start a fresh cloud Sol session and give only this instruction:

> You are a blinded candidate planner. Read only `Pukujan/project-assurance-modules/experiments/ra-retrospective-blind/BASELINE_HANDOFF.md` and `TASK_PACKET.md` at the exact frozen revision I provide. Do not read any other PAM methodology files. You are explicitly forbidden from accessing `Pukujan/research-assurance` or any artifact derived from its finished repository. Do not use prior-chat/memory details about that project. If any such details are exposed, stop and mark the run contaminated. Follow the baseline handoff, write the frozen result only under a new `experiments/ra-retrospective-blind/runs/<run_id>/baseline/` directory, and stop without self-scoring.

Supply the frozen PAM repository revision separately. The baseline may use that revision only to fetch the two allowlisted experiment files; it must not inspect methodology files.

## Condition B — Sol + PAM

Start a second fresh cloud Sol session and give only this instruction:

> You are a blinded candidate planner testing Project Assurance Modules. Read `Pukujan/project-assurance-modules` at the exact frozen revision I provide. Begin with `experiments/ra-retrospective-blind/CANDIDATE_HANDOFF.md` and obey its allowlist/forbidden-source rules. You are explicitly forbidden from accessing `Pukujan/research-assurance` or any artifact derived from its finished repository, and you must not use prior-chat/memory details about that project. If any such details are exposed, stop and mark the run contaminated. Use PAM plus the frozen `TASK_PACKET.md` to perform projectization preflight and write the required frozen output only under a new `experiments/ra-retrospective-blind/runs/<run_id>/candidate/` directory. Do not edit PAM methodology during the run and do not self-score.

Use the same frozen task packet and PAM revision selected before Condition A.

## Condition C — Terra/Luna + PAM

Only after A and B are frozen, give a local planner the same Condition B instructions and the same revision/task packet. This is not expected to reproduce Sol byte-for-byte. It measures how much material planning quality PAM preserves under a weaker/different planner.

If desired, run Terra and Luna separately rather than allowing them to collaborate, so planner identity remains interpretable.

## Evaluation

After each candidate output is committed/frozen:

1. verify access attestation and contamination status;
2. record exact candidate commit/run identity;
3. only then allow the evaluator to inspect `Pukujan/research-assurance`;
4. score all valid runs with the frozen dimensions in `BENCHMARK_PROTOCOL.md`;
5. compare Sol baseline versus Sol+PAM first;
6. then compare Terra/Luna+PAM against Sol+PAM as a planner-robustness diagnostic.

Do not reveal individual reference misses to a candidate and continue editing the same run. Improvements after evaluation require a new PAM/task/run version.
