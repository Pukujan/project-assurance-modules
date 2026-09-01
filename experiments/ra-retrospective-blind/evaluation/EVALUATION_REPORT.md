# RA retrospective blind benchmark — evaluator report

## Status

Development/conformance evaluation only. This report does **not** establish PAM generalization because PAM was extracted from Research Assurance planning work.

Frozen methodology input:

- PAM revision: `8f4737fc212e6b09f8066d90e178aa8760e619fb`
- benchmark: `ra-retrospective-blind/v0`

Frozen candidate runs:

- Condition A / Sol baseline: branch `experiment/ra-retrospective-blind/condition-a-20260901t194100z`, commit `0da5a62529f7e665421b3389a941d1f70f895286`
- Condition B1 / Sol + PAM primary: branch `experiment/ra-retro-condition-b-20260901-154700-gpt56sol`, commit `0d5b6f254dc199c2be5f552b77724f3dc966a44d`
- Condition B2 / Sol + PAM replication: branch `candidate/condition-b-issue3-20260901-1552-retry1`, commit `658e219e46b60a1a6fe954712cba94cc846394ab`

All three runs supplied clean access attestations and were frozen before evaluator comparison with the finished Research Assurance reference.

B1 is the primary treatment because it is the earliest valid Condition B run. B2 is retained as a replication. The later retry is not substituted for B1 post hoc.

## Frozen rubric scores

| Dimension | Weight | A baseline | B1 + PAM | B2 + PAM |
| --- | ---: | ---: | ---: | ---: |
| Problem/product scope and explicit non-goals | 8 | 8 | 8 | 8 |
| Build-vs-reuse / existing-system decision discipline | 8 | 8 | 8 | 8 |
| System/component ownership boundaries | 12 | 10 | 11 | 11 |
| Milestone/phase sequencing and dependency logic | 10 | 9 | 9 | 9 |
| Executable issue decomposition and closure evidence | 10 | 10 | 10 | 9 |
| SWE/CI foundation | 8 | 8 | 8 | 8 |
| Invariants, failure modes, and fail-closed negative validation | 12 | 12 | 12 | 12 |
| Benchmark/dataset/holdout methodology | 10 | 10 | 10 | 10 |
| Scope control and mechanism entry/kill discipline | 7 | 6 | 7 | 7 |
| Provenance/FOSSIL decision-lineage boundary | 5 | 3 | 4 | 4 |
| Multi-repo orchestration and exact revision/evidence identity | 5 | 3 | 5 | 5 |
| Structured handoff/continuity | 5 | 3 | 4 | 4 |
| **Total** | **100** | **90** | **96** | **95** |

Primary paired effect:

`score(B1) - score(A) = +6 points`

Replication effect relative to the same baseline:

`score(B2) - score(A) = +5 points`

The two treatment runs are close enough to support a stable qualitative conclusion for this development benchmark: PAM improved planning formalization and continuity/ownership discipline, but the strong research packet plus Sol already recovered most engineering methodology without PAM.

## Dimension rationale

### Scope and non-goals

All runs strongly recovered the narrow promotion boundary, exploration-vs-promotion distinction, rejection of universal `verified=true`, finance-first scope, and deferral of GraphRAG/claim-verifier/agent-harness mechanisms. No meaningful PAM delta is credited here because the frozen research packet already stated these constraints explicitly.

### Build-vs-reuse

All runs made strong reuse decisions for FOSSIL Core, Retrieval Benchmarker, Source Ranker, and the financial application. PAM made the pre-build disposition mechanically explicit, but the baseline independently recovered the same discipline from the research packet. Therefore the score is tied while the treatment still has operational advantages in manifest state.

### Ownership and multi-repo coordination

The baseline preserved component boundaries but was less explicit about multi-repository producer/consumer change rules and exact tested-composition identity. Both PAM runs emitted an explicit repository map, runtime-vs-evaluation distinctions, must-not-own boundaries, exact revision rules, and cross-repository contract closure requirements.

Neither treatment receives full ownership credit because both propose a new thin promotion-assurance runtime/core, while the finished reference evolved primarily as an integration/control-plane superproject. The candidate design is defensible but adds a potentially unnecessary runtime abstraction that should have to earn itself through the build-vs-reuse gate.

### Milestones and issue decomposition

All runs were strong. The baseline produced a large dependency-aware issue hierarchy with acceptance criteria. PAM did not create a large gain in issue quality, although it made owner review and preflight authorization more explicit. B2 is one point lower on issue decomposition because its issue set is somewhat coarser than A/B1 while remaining materially adequate.

### SWE/CI and validation

All runs recovered deterministic/no-network PR CI, lint/type/test foundations, property/state-machine tests, metamorphic relations, mutation testing, fault injection, adversarial review, replay/rebuild, and negative/fail-closed testing. The research packet itself already contained these techniques, so this benchmark cannot attribute their presence to PAM.

### Benchmark and holdout discipline

All runs separated retrieval/source/semantic/temporal dimensions, public development from hidden confirmation, exact dataset/config identities, layer ablations, and no-benefit outcomes. Again, the task packet was already unusually strong in this area, limiting treatment contrast.

### Scope control

PAM produced a clearer operational admission gate: current-claim impact, build-vs-reuse disposition, cheapest credible validation, ownership, entry/exit criteria, and explicit defer/kill outcomes. The baseline had good scope warnings and kill criteria but less machine-operational structure.

### Provenance and FOSSIL decision lineage

All runs understood FOSSIL as provenance/lineage rather than semantic proof. However, none fully reproduced the finished reference project's project-decision-chain knowledge-pack/governance depth. PAM's research handoff and manifest improve the promotion boundary, but v0 does not yet provide a portable decision-lineage module that closes this gap.

### Structured continuity

The baseline supplied a high-quality prose handoff but no machine-valid project-state contract. Both PAM runs emitted `HANDOFF_STATE.json` and explicit stale-state reconciliation semantics. They do not receive full credit because PAM v0's `continuity.structured-handoff` module requires a pinned handoff schema, but the frozen methodology did not actually ship a generic handoff-state schema. Both treatment runs correctly left relevant requirements pending rather than fabricating closure.

## Non-scoring diagnostics

### Unnecessary complexity

The main common risk is the proposed new thin promotion-assurance core/runtime. The finished reference demonstrates that a control-plane/integration superproject can carry much of the program without necessarily introducing a new runtime coordinator. Future PAM routing should require the new runtime/core itself to pass an explicit reuse/composition/necessity gate before project bootstrap treats it as authorized architecture.

### Protocol-induced bureaucracy

No hard protocol failure occurred. PAM did increase artifact count substantially, but the additional artifacts were mostly non-duplicative: machine manifest, build-vs-reuse disposition, scope boundary, repository map, validation plan, and structured handoff. The treatment runs did not appear blocked by the methodology.

The main bureaucracy risk is future module proliferation. PAM should not respond to this result by making every methodology concern a mandatory standalone document/module for every project.

### Benchmark contrast weakness

The frozen `TASK_PACKET.md` contains many conclusions that are themselves methodology-rich: PDD/SDD, invariants, mutation/metamorphic/fault testing, hidden holdouts, scope control, build-vs-reuse preferences, exact identities, FOSSIL boundary questions, and resumability. As a result, Condition A is an unusually strong baseline and the +5/+6 treatment effect should be interpreted as improvement in operationalization rather than discovery of those concepts.

### Evaluator uncertainty

This is a single-evaluator semantic score against a historically evolved reference project. Absolute scores should be treated as approximate (roughly a few points of judgment uncertainty). The paired pattern is more useful than claiming exact psychometric precision. A later evaluation can use a second independent evaluator or more deterministic subcriteria if the benchmark becomes release-significant.

## PAM gaps confirmed by the experiment

The treatment runs independently surfaced the same material v0 gaps:

1. only three executable modules exist despite a broader routing vocabulary;
2. the structured-handoff module lacks a shipped generic handoff-state schema;
3. profile composition is described but no profile definitions are shipped;
4. planning/SWE/validation/benchmark/provenance obligations can be described in prose but cannot yet be routed and tracked through versioned module requirement IDs.

These are observed methodology gaps, not authorization to mass-extract every planned module.

## Decision

Development result: **PROMISING / CONTINUE, WITH BOUNDED EXPANSION**.

This benchmark supports the narrower claim that PAM can improve formal projectization, cross-repository ownership discipline, scope/reuse gating, and resumable evidence-backed planning for its reference-style project. It does not support a claim that PAM generalizes to unrelated projects or that it improves every planner.

Do not tune the frozen v0 run. Any methodology changes become a new PAM revision and future benchmark version/run.

## Recommended next sequence

1. Preserve this result and candidate commits unchanged.
2. Add the missing generic handoff-state schema/validator as the highest-confidence extraction because Research Assurance already has a working reference adoption.
3. Implement profile schema/selection so modules can be composed without manual enumeration.
4. Extract only a small next group of repeatedly demonstrated obligations: planning foundation (PDD/SDD/invariants/failure register), SWE/CI foundation, benchmark-integrity/holdout, and decision-lineage/provenance boundary.
5. Adopt the generic handoff and selected modules in `RA-plugin` as the second real adopter; record any bespoke exceptions as methodology defects.
6. Run a cheaper/different planner + PAM robustness test after the new revision is frozen if useful.
7. Most importantly, use the next genuinely new project that did not shape PAM as the first transfer/generalization benchmark before claiming stable v1.

## What this evaluation does not authorize

- no stable-v1/generalization claim;
- no mass generation of modules solely to increase checklist coverage;
- no requirement that every project use FOSSIL, hidden holdouts, mutation testing, or multi-repo orchestration;
- no claim that the proposed new runtime/core architecture is required;
- no modification of the frozen candidate outputs after seeing this evaluation.
