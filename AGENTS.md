# AGENTS.md

This repository defines reusable project-assurance methodology. It is not itself the live project state of every adopter.

## Read order

1. `specs/PDD.md`
2. `docs/ARCHITECTURE.md`
3. `docs/ROUTING.md`
4. active GitHub issue/PR
5. relevant schema(s)
6. relevant module/profile definitions
7. `docs/MODULE_ROADMAP.md` only as candidate future scope

## Core rules

- Do not add a methodology requirement solely because it is generally considered a best practice.
- Every module must state applicability, non-scope, requirements, acceptable evidence, and a not-applicable rule.
- Do not make every module mandatory.
- Do not use agent self-report as closure evidence when objective evidence is available.
- Markdown checkboxes may be generated views; authoritative requirement state belongs in a validated project manifest.
- Do not silently turn uncertainty into `not_applicable`.
- Do not generate a large repository/issue/project backlog before reviewed preflight.
- Do not expose hidden benchmark answers through modules, fixtures, manifests, or handoffs.
- Do not collapse integrity, correctness, empirical quality, security, provenance, and review into one `verified` state.
- Keep runtime systems (Research Assurance, FOSSIL, agent plugins) outside this repository; this repo may define methodology for using them.
- New modules should be extracted from demonstrated repeated need, established methodology, or observed failure—not speculation alone.

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

## Bootstrap status

Issue `#1` is the v0 bootstrap parent. Until the bootstrap is validated and used by at least two real projects, treat schemas/modules as experimental and pin exact SHAs.

`Pukujan/research-assurance` is the first reference source/adopter. Do not copy its every mechanism into universal scope; extract only portable methodology with routing conditions.
