# AGENTS.md

This repository defines reusable project-assurance methodology. It is not itself the live project state of every adopter.

## Read order

1. `specs/PDD.md`
2. `docs/ARCHITECTURE.md`
3. `docs/PROJECTIZATION_GATE.md`
4. `docs/ROUTING.md`
5. `docs/IMPLEMENTATION_PLAN.md`
6. active GitHub issue/PR
7. relevant schema(s)
8. relevant module/profile definitions
9. `docs/MODULE_ROADMAP.md` only as candidate future scope

For the blinded Research Assurance retrospective, the experiment-specific handoff overrides the normal read order and defines a strict allowlist/denylist.

## Core rules

- Do not add a methodology requirement solely because it is generally considered a best practice.
- Every module must state applicability, non-scope, requirements, acceptable evidence, and a not-applicable rule.
- Do not make every module mandatory.
- Do not use agent self-report as closure evidence when objective evidence is available.
- Markdown checkboxes may be generated views; authoritative requirement state belongs in a validated project manifest.
- Do not silently turn uncertainty into `not_applicable`.
- Do not generate a large repository/issue/project backlog before reviewed projectization preflight.
- For nontrivial software projectization, do not assume `build_new`; route/evaluate build-vs-reuse first when plausible existing systems may satisfy the requirement.
- New scope, red-team findings, and attractive technologies require explicit admission/disposition; they do not automatically become current implementation work.
- Do not expose hidden benchmark answers through modules, fixtures, manifests, handoffs, knowledge packs, or experiment prompts.
- Do not collapse integrity, correctness, empirical quality, security, provenance, and review into one `verified` state.
- Keep runtime systems (Research Assurance, FOSSIL, agent plugins) outside this repository; this repo may define methodology for using them.
- FOSSIL is optional durable lineage for consequential decisions, not PAM's live checklist/task store.
- New modules should be extracted from demonstrated repeated need, established methodology, or observed failure—not speculation alone.
- Deterministic schemas/router/validators own structural consistency; humans still own consequential projectization and methodology-waiver judgments.

## Module change contract

A material module addition/change should include:

- stable module ID/version;
- source precedent or motivating failure;
- applicability criteria;
- explicit non-scope;
- requirements;
- closure evidence kinds and rules;
- not-applicable rule;
- dependencies/conflicts if any;
- positive and negative validation fixtures before stable release;
- compatibility/versioning impact.

Changing requirement semantics, applicability, or closure evidence requires an appropriate module version change.

## Project adoption boundary

An adopting project should pin an exact repository revision plus module/profile versions in its own `PROJECT_ASSURANCE` manifest. Historical manifests are not rewritten because this repository evolves.

The adopting project's human/agent orchestrator owns project facts, reviewed routing, and evidence references. This repository owns the reusable methodology contract.

Normal projectization sequence:

```text
research mature enough
 -> research handoff
 -> build-vs-reuse
 -> scope boundary
 -> route modules
 -> reviewed/pinned PROJECT_ASSURANCE manifest
 -> only then project/spec/repo/issue/CI/benchmark bootstrap
```

## Deterministic check lane

Before claiming the current v0 substrate is green, run:

```bash
make check
```

The check lane covers lint, format, strict typing, module/manifest validation, and deterministic tests. Do not claim a check passed without current evidence.

## Benchmark integrity

The retrospective experiment under `experiments/ra-retrospective-blind/` is a development/conformance benchmark. PAM was extracted from Research Assurance, so a high score is not generalization evidence.

For candidate runs:

- obey the exact condition handoff;
- never access the finished `Pukujan/research-assurance` reference project;
- freeze task packet/methodology revision before paired baseline/PAM runs;
- do not edit PAM methodology during a candidate run;
- record access attestation;
- freeze candidate output before evaluator/reference comparison;
- improvements after evaluation require a new run/version.

## Bootstrap status

Issue `#1` is the v0 bootstrap parent. Until the bootstrap is validated and used by at least two real projects, treat schemas/modules as experimental and pin exact SHAs.

`Pukujan/research-assurance` is the first reference source/adopter. Do not copy its every mechanism into universal scope; extract only portable methodology with routing conditions.
