# Handoff — continue RPP projectization

Run: `condition-d-grok-4.6-opencode-20260901-174255`
Condition: blinded baseline (Condition D)
Frozen packet revision: `8f4737fc212e6b09f8066d90e178aa8760e619fb`

## Who you are

A fresh session continuing **Replayable Promotion Program (RPP)** projectization. You do not have conversational memory. Do not invent a different product name or reopen non-scope unless the owner files a new decision.

## What already exists

This directory is the planning bundle:

| File | Use |
|---|---|
| `RUN_MANIFEST.json` | identity of this frozen run |
| `ACCESS_ATTESTATION.json` | what was read; contamination status |
| `PLAN.md` | product, invariants, reuse, phases |
| `ISSUES.md` | executable decomposition |
| `DECISIONS.md` | proposed decisions awaiting owner accept |
| `FAILURE_MODES.md` | v0 failure-mode register |
| `CANDIDATES.md` | not-current work |
| `VALIDATION.md` | which techniques apply where |
| `CONTINUITY.md` | how to resume later implementation work |

This run is **frozen**. Do not edit these files to chase evaluator feedback. If the owner wants a revised plan, start a new revision in a real RPP repository (or a new run id if still inside the benchmark).

## Allowed vs forbidden (benchmark)

If you are still inside the blinded benchmark:

- Read this bundle and the original `TASK_PACKET.md` / `BASELINE_HANDOFF.md`.
- Do not read PAM methodology, `OUTPUT_CONTRACT.md`, other condition outputs, or evaluator results.
- Do not access `Pukujan/research-assurance`. If you encounter it, stop and mark `CONTAMINATED`.

If the benchmark is over and the owner has moved to ordinary engineering, follow the owner’s then-current repo rules. Still do not silently copy an unseen reference project.

## What to do next (ordinary engineering, after owner accept)

1. Confirm `DECISIONS.md` items D1–D12 (accept/amend).
2. Create the RPP program repository skeleton (`ISSUES.md` E0-2).
3. Collect real SHAs for FOSSIL, Retrieval Benchmarker, Source Ranker, finance app (E1-1).
4. Implement the FOSSIL adapter and integrity campaigns before claiming any accepted promotion (E1).
5. Implement kernel + deterministic checkers with no LLM (E2–E3).
6. Only then wire one finance promote path (E4).
7. Keep Source Ranker and the agent plugin behind go/no-go issues (E6, E8).

## Hard rules to preserve

- Exploration is ungated; accept is gated.
- No universal `verified=true`.
- Indexes are projections.
- Hidden confirmatory answers never enter implementer context.
- Do not recreate a universal agent stamp layer.
- Do not rebuild FOSSIL or Retrieval Benchmarker.
- Do not open deferred candidates as issues without admission.
- Prefer empirical kill/no-benefit over architectural enthusiasm.

## Open owner actions

The planner cannot honestly pin component SHAs from the packet (they were omitted on purpose). Filling lockfiles requires access to the owned repositories, not to any forbidden finished “research assurance” project.

Language/runtime for the kernel is also unpinned; choose for adapter fit, keep the kernel boring.

## Contamination

This run attests `clean`. If you use finished-project details not in the packet, you contaminate a *new* session; do not retroactively edit this run.
