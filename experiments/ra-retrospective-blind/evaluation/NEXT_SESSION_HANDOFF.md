# Next-session handoff — Project Assurance Modules after RA retrospective v0

## Why this handoff exists

The Research Assurance retrospective benchmark has reached diminishing returns. The next session should **not reopen the retrospective, repair the blind evaluator bundle, or generate more A/B/C/D runs by default**. Preserve the frozen evidence, then continue PAM as a reusable methodology with bounded changes and a second/unseen adopter path.

This document is the durable continuation point for a fresh session.

---

## 1. Product identity

Repository: `Pukujan/project-assurance-modules`

PAM is a **versioned engineering/research methodology registry + deterministic router/composer + evidence-state model** for turning mature research/discussion into a properly scoped, engineered, validated, tracked project.

PAM is not:

- Research Assurance runtime;
- a universal agent-control or compliance service;
- a monolithic checklist;
- a template dump;
- a checked-box correctness system;
- a universal `verified=true` mechanism.

Core intended lifecycle:

```text
research / discussion
human decides "mature enough to consider building"
        ↓
project-assurance preflight
        ↓
research handoff
        ↓
build-vs-reuse
        ↓
scope boundary
        ↓
classify project/task + claims/risks/state/interfaces
        ↓
route applicable versioned methodology modules
        ↓
gap analysis
        ↓
human review
        ↓
freeze project-owned Project Assurance Manifest
        ↓
repo / project / issues / milestones / implementation
```

Human judgment remains authoritative for ambiguous/consequential projectization decisions. Agents may propose routing and evidence but should not silently convert uncertainty into `not_applicable` or self-attest completion.

Stable methodology identity is `PAM repository SHA + module_id + module version`.

---

## 2. Frozen PAM v0 input

The retrospective benchmark and current bootstrap methodology are pinned to:

`8f4737fc212e6b09f8066d90e178aa8760e619fb`

Branch:

`bootstrap/v0-methodology`

**Do not rewrite this SHA or mutate the frozen candidate runs.** Any methodology improvement starts a new revision/branch.

Bootstrap PR:

- PR #2: `feat: bootstrap versioned project-assurance methodology and projectization preflight`
- base: `main`
- head: `bootstrap/v0-methodology`
- frozen head: `8f4737fc212e6b09f8066d90e178aa8760e619fb`
- last checked before this handoff: open, mergeable, not merged

Do not merge PR #2 unless the owner explicitly asks.

Current v0 modules:

- `projectization.build-vs-reuse@0.1.0`
- `projectization.scope-boundary@0.1.0`
- `continuity.structured-handoff@0.1.0`

Requirement states remain separate from module routing disposition.

Routing disposition:

- `required`
- `recommended`
- `conditional`
- `not_applicable`

Requirement state:

- `pending`
- `satisfied`
- `not_applicable`
- `deferred`
- `blocked`

Never introduce a universal `verified=true`.

---

## 3. Deterministic substrate already present

Core methodology/contracts:

- `specs/PDD.md`
- `docs/ARCHITECTURE.md`
- `docs/ROUTING.md`
- `docs/MODULE_ROADMAP.md`
- `docs/PROJECTIZATION_GATE.md`
- `docs/IMPLEMENTATION_PLAN.md`
- `schemas/module.schema.json`
- `schemas/project-assurance-manifest.schema.json`
- `examples/PROJECT_ASSURANCE.example.json`
- `AGENTS.md`

Deterministic implementation:

- `scripts/pam_core.py`
- `scripts/pam_validate.py`
- `scripts/pam_route.py`
- `tests/test_pam_core.py`
- `pyproject.toml`
- `Makefile`
- `.github/workflows/ci.yml`

`make check` runs lint, formatting, strict typing, manifest/module validation, and tests.

The frozen v0 branch previously reached green CI. A fresh session must re-fetch current CI before claiming it is green; do not rely on remembered status.

---

## 4. PAM / FOSSIL boundary

PAM/Git owns live methodology, requirement, routing, and evidence-reference state.

FOSSIL is optional durable lineage/provenance for consequential decisions. Do not ingest every thought/checklist transition.

Existing decision-lineage pack:

`knowledge-packs/pam-projectization-decision-chain/`

Pack ID:

`pack_pam_projectization_decisions_v1`

Pinned FOSSIL schema source:

- repo: `Pukujan/fossil-core`
- revision: `92eb44c96c87a4b7d93ab3c8ba5e85c496ba44b8`
- schema: `schemas/knowledge-pack/v1.schema.json`

Important: the pack is contract-shaped but **actual FOSSIL runtime ingest has not been established by this benchmark**. Never claim accepted/promoted FOSSIL claims unless an actual ingest/receipt exists.

---

## 5. Retrospective benchmark — frozen results

Benchmark:

`experiments/ra-retrospective-blind/`

Classification:

**development/conformance benchmark only** — not clean generalization evidence because PAM was extracted from Research Assurance planning.

Frozen task/methodology context is methodology-rich, which creates a high no-PAM baseline and reduces treatment sensitivity.

### Candidate results

| Condition | Planner / harness | PAM | Score | Frozen commit |
| --- | --- | --- | ---: | --- |
| A | GPT-5.6 Sol / ChatGPT | no | 90 | `0da5a62529f7e665421b3389a941d1f70f895286` |
| B1 primary | GPT-5.6 Sol / ChatGPT | yes | 96 | `0d5b6f254dc199c2be5f552b77724f3dc966a44d` |
| B2 replication | GPT-5.6 Sol / ChatGPT | yes | 95 | `658e219e46b60a1a6fe954712cba94cc846394ab` |
| C robustness | GPT-5.6 Terra / Codex local agent | yes | 94 | `7be21dbd6735c84bd500ce4c4d5bb531d07582b4` |
| D heterogeneous baseline | Grok 4.6 / OpenCode | no | 95 | `017a2c5516fb98e0ae40ad6bed1e3d7f2876df5e` |

Original valid controlled contrast:

`B1 - A = +6`

Treatment replication relative to same baseline:

`B2 - A = +5`

**Do not compute C-D as a PAM effect.** C and D differ in model and harness.

Second-pass evaluation artifacts:

- `evaluation/EVALUATION_ROUND2_IDENTITY_AWARE.md`
- `evaluation/EVALUATION_ROUND2_IDENTITY_AWARE.json`

The second pass is deliberately labeled identity-aware/non-blind.

### Main interpretation

1. Sol+PAM improved formal projectization over matched Sol baseline, especially scope/reuse gating, multi-repo exact-state discipline, and structured continuity.
2. Terra+PAM at 94 shows strong methodology portability across a different planner/harness.
3. Grok/OpenCode without PAM at 95 shows that a powerful planner can independently reconstruct nearly all obligations from this methodology-rich task packet.
4. Therefore PAM should not be sold as necessary for every powerful model; its value proposition is durable, deterministic, transferable operationalization rather than magical methodology discovery.
5. The RA retrospective is now low-information for further tuning. Move to unseen-project evidence.

---

## 6. Vendor-awareness / blind-evaluator attempt

The owner raised a legitimate concern that evaluator/vendor familiarity might bias evidence interpretation toward same-vendor outputs.

A vendor/model/harness-blind evaluator protocol was attempted but **did not produce valid scores**.

Observed failures:

1. first evaluator correctly stopped because opaque candidate artifacts were not actually supplied;
2. an anonymous bundle was then prepared;
3. a later evaluator correctly stopped before scoring because a permitted substantive artifact still contained an identity-bearing run identifier.

No blind evaluator scores were frozen. Therefore:

- vendor-awareness bias is **not proven**;
- vendor-awareness bias is **not disproven**;
- do not claim the blind experiment succeeded;
- do not spend more time repairing this retrospective blind bundle by default.

The identity-aware evaluator gave cross-vendor Grok no-PAM a 95/100, which is inconsistent with a simplistic claim that the evaluator automatically discounts all cross-vendor work, but it is not a controlled vendor-bias test.

Future unseen-project benchmarks may revisit this with proper sanitization from the start:

- neutral candidate IDs;
- no model/provider/harness/run identifiers in substantive files;
- deterministic denylist/pattern scanner;
- separate semantic leak review;
- reveal mapping outside evaluator-visible branch;
- scores frozen before reveal.

Treat blind-packaging as benchmark infrastructure, not core PAM functionality.

---

## 7. Newly observed protocol gaps

### Fresh-workspace bootstrap

Terra initially entered an empty workspace and correctly stopped because `CANDIDATE_HANDOFF.md` did not exist.

The eventual run bootstrapped only the exact frozen PAM SHA and recorded the first stop as `PRE_RUN_BOOTSTRAP_ABORT`, not contamination.

This exposes a reusable PAM requirement:

```text
fresh worker + empty workspace
    -> acquire exact PAM repository revision
    -> verify revision
    -> locate start/handoff contract
    -> only then route/projectize
```

This should become a bounded bootstrap/acquisition contract in the next methodology revision.

### Working-tree hashes

Terra produced a different task-packet SHA-256 than earlier runs despite reading the same Git revision, likely due to checkout/line-ending representation. Future benchmark identity should prefer Git blob identity/content-addressed bytes rather than platform-transformed working-tree bytes.

### Blind-evaluation packaging

Removing manifests and attestations is insufficient. Identity may exist in handoff prose/JSON/YAML/run IDs. Future blind packaging must fail closed on leakage.

---

## 8. Confirmed PAM v0 methodology gaps

The benchmark repeatedly identified these gaps:

1. only three executable modules exist despite broader methodology vocabulary;
2. `continuity.structured-handoff` expects a generic handoff-state contract, but PAM does not yet ship a generic handoff schema + validator;
3. profiles are conceptual but concrete profile definitions/schema/selection are missing;
4. planning foundation, SWE/CI, benchmark/holdout integrity, and decision-lineage/provenance are largely prose/roadmap rather than routable versioned requirement IDs;
5. fresh-workspace exact-version bootstrap/acquisition is missing;
6. benchmark blind-packaging/leak validation is missing if PAM later owns benchmark infrastructure.

Do **not** respond by mass-extracting every roadmap item. Add only modules with repeated demonstrated need and bounded applicability.

---

## 9. Recommended next branch/revision

Do not modify frozen `8f4737fc...`.

After the owner decides what to do with PR #2/#4, create a new branch/revision for bounded PAM evolution. Suggested name:

`develop/v0.2-bounded-extractions`

Do not call it stable v1.

### Highest-confidence v0.2 work, in order

#### A. Generic structured-handoff schema + validator

Extract from the working Research Assurance implementation, but do not immediately replace RA's local contract.

Target semantics:

- authority/trigger rules;
- machine-readable current state;
- deterministic validation;
- live-state reconciliation;
- explicit current-state vs historical-checkpoint distinction;
- hidden-evaluation exclusion;
- exact next action/blockers/current phase;
- exact methodology/component identities where relevant.

Migration rule: RA keeps its local `ra-handoff/1.0.0` implementation until generic PAM parity is proven and migration is explicit/versioned.

#### B. Bootstrap/acquisition contract

Add a minimal fresh-workspace protocol:

- repository locator;
- exact commit/tag/version;
- acquisition mechanism;
- detached/reproducible revision verification;
- start document/profile locator;
- fail-safe behavior if unavailable;
- content identity rules that avoid platform line-ending ambiguity.

Do not turn this into a general deployment tool.

#### C. Profiles

Implement profile schema/selection so adopting projects do not manually enumerate arbitrary modules.

Profile selection must remain explainable and route modules by project facts, not make every module required.

#### D. Small repeated module extraction

Only after A–C, extract a small set with strong repeated evidence:

- planning foundation: PDD/SDD/invariants/failure register;
- SWE/CI foundation;
- benchmark/dataset/holdout integrity;
- decision-lineage/provenance boundary.

Each module needs:

- stable ID/version;
- motivating precedent/failure;
- applicability;
- non-scope;
- requirements;
- acceptable closure evidence;
- N/A rule;
- dependencies/conflicts;
- positive and negative fixtures;
- compatibility/versioning impact.

Avoid importing Research Assurance-specific mechanisms as universal requirements.

---

## 10. Second adopter

Best next real adopter candidate:

`Pukujan/RA-plugin`

Use it to test whether generic handoff/profile/selected modules work without bespoke methodology edits.

Record exceptions as PAM defects or explicit domain/project-specific non-applicability, not as silent divergence.

Do not make PAM a runtime dependency unless the adopting project actually needs runtime code; normal adoption is methodology/config/schema/evidence state.

---

## 11. First real generalization test

The next genuinely new project that **did not shape PAM** is the important benchmark.

Do not use historical architecture similarity as the primary oracle.

Prefer downstream/projectization outcomes such as:

- missed requirements discovered after implementation starts;
- issue/backlog churn caused by planning omissions;
- duplicate rebuild of existing OSS/internal capabilities;
- scope expansions after preflight;
- ownership/interface ambiguity;
- invalid/unreproducible CI or benchmark evidence;
- hidden-holdout contamination;
- cross-session resume failure;
- time/cost to first validated vertical slice;
- number/severity of post-projectization boundary corrections.

If multiple planners/vendors are used, pre-plan the experimental matrix before exposing candidate outputs. Vendor-blind evaluation should be built into packaging from the start if it is a release-significant hypothesis.

Only after multiple adopters plus an unseen-project result should PAM make stable-v1/generalization claims.

---

## 12. Research Assurance reference boundary

`Pukujan/research-assurance` is a reference source/adopter, not the universal architecture PAM should reproduce.

Important historical architecture lesson:

- RA evolved as a program/control-plane/superproject coordinating independently owned repositories;
- multiple benchmark candidates independently proposed a new thin promotion runtime/kernel;
- that is a defensible alternative but must earn itself through build-vs-reuse/necessity evidence;
- PAM should preserve obligations/decision discipline rather than force RA's exact repo names/topology.

Reference RA structured handoff currently demonstrates the strongest generic extraction opportunity:

- machine schema;
- durable state JSON;
- deterministic validator/tests;
- resume protocol: validate -> read handoff -> re-fetch live state -> reconcile -> mutate;
- hidden evaluation excluded.

Fresh-check RA live PR/branch state before making claims or extracting code/contracts.

---

## 13. GitHub state to verify at session start

Always re-fetch live state rather than trusting this handoff for mutable GitHub facts.

At handoff creation:

- PR #2 is open, mergeable, not merged; head `8f4737fc212e6b09f8066d90e178aa8760e619fb`.
- PR #4 is the evaluation PR, base `bootstrap/v0-methodology`, and is open/not merged. It now contains the original first-pass result plus second-pass robustness evaluation and this handoff.
- issue #3 is the retrospective benchmark tracking issue; update/close it only after preserving the final result/comment.

Do not merge PR #2 or PR #4 without explicit owner instruction.

---

## 14. Exact next-session execution order

A fresh capable session should do the following:

1. Read this handoff.
2. Fetch live PR #2, PR #4, issue #3, and current CI/status checks.
3. Confirm the frozen PAM SHA and candidate commits remain unchanged.
4. Read `EVALUATION_ROUND2_IDENTITY_AWARE.md` and `.json`.
5. Do **not** reopen blind-evaluator work or produce more RA retrospective candidates unless the owner explicitly asks.
6. Preserve/close the retrospective tracking issue if not already closed; no candidate edits.
7. Ask/resolve whether PR #4 evaluation should be merged into `bootstrap/v0-methodology` and whether PR #2 should be merged into `main`. Never infer approval.
8. Once repository state is decided, create a new bounded v0.2 development branch rather than editing the frozen v0 SHA.
9. Implement generic structured-handoff schema/validator first, with negative tests.
10. Implement fresh-workspace exact-revision bootstrap/acquisition contract.
11. Implement profiles/schema/selection.
12. Extract only the small repeated module set justified above.
13. Use RA-plugin as second adopter.
14. Freeze the next methodology revision before any new transfer benchmark.
15. Use an unseen project for genuine generalization evidence.

---

## 15. Claims that are currently justified

Reasonable narrow claims:

- PAM v0 produced a +6 matched Sol planning-score improvement on its RA-derived development benchmark, with a +5 treatment replication.
- Terra+PAM retained high semantic planning quality (94/100), close to Sol+PAM (95–96), suggesting robustness across a different planner/harness.
- A different strong planner, Grok/OpenCode, achieved 95/100 without PAM on the methodology-rich task packet, demonstrating that PAM is not necessary for strong planning when the input already carries most methodology.
- PAM's strongest observed benefits are operationalization: explicit preflight, scope/reuse dispositions, exact composition identity, durable requirement/evidence state, cross-repository closure, and structured continuity.
- The benchmark surfaced concrete missing methodology/infrastructure: generic handoff schema, profiles, fresh-workspace bootstrap, and robust blind-packaging if needed.

Claims **not** justified:

- PAM improves every model or planner;
- PAM adds a fixed score delta across vendors;
- Terra versus Grok is a causal PAM comparison;
- vendor evaluator preference has been proven or disproven;
- RA architecture is the objectively correct project topology;
- the RA retrospective demonstrates unrelated-project generalization;
- stable v1 is ready.

---

## 16. Stop condition for the next session

Do not let PAM become a self-referential methodology research project that continuously benchmarks itself against RA.

The next session has succeeded when it has:

- preserved v0;
- made a bounded next revision with high-confidence missing contracts;
- exercised it on a second adopter;
- prepared an unseen-project test that measures real downstream engineering outcomes.

That is more informative than another retrospective planner run.
