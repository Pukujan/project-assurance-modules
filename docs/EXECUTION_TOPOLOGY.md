# Assurance execution topology

## Status and purpose

This document defines a reusable execution policy for assurance work that combines design judgment, repeated local engineering loops, independent attestation, and checkpoint review.

It is a methodology policy, not a runtime scheduler and not a model-vendor prescription. Adopting projects remain responsible for their live execution state, exact actor identities, commands, CI systems, and checkpoint decisions.

The policy is motivated by a concrete Study-OS mutation-assurance run in which a persistent local executor converged efficiently through repeated edit/test/mutation loops while exact-revision CI and independent review remained necessary to establish the final assurance claim. The lesson is the execution topology, not the specific project or model.

## Core invariant

The actor optimizing toward an assurance gate must not have unilateral authority to redefine or approve that gate.

A valid topology separates four responsibilities when the work is material enough to justify them:

1. **Assurance architect** — defines what must be proven: product/design obligations, invariants, threat models, test oracles, mutation/fuzz policy, acceptance thresholds, and admissible evidence.
2. **Persistent executor** — performs repeated implementation and validation work against the frozen obligations: edit/run/inspect/fix loops, targeted tests, mutation/fuzz/property runs, service/database/container iteration, restart/recovery rehearsal, log inspection, and mechanical spec-conforming test additions.
3. **Independent attestation mechanism** — reproduces the candidate from a clean or otherwise independent boundary, normally CI where the applicable PAM module requires CI. Its purpose is reproducibility and independence, not interactive debugging efficiency.
4. **Checkpoint reviewer** — interprets the evidence, unresolved risks, and any requested gate changes, then decides whether the checkpoint claim is satisfied when judgment is required.

One person or organization may fill multiple roles in low-risk work, but the authority boundaries must still be explicit. For a material gate, the executor must not be the sole authority that defines, weakens, and approves the same gate.

## Authority boundary

### Assurance architect may

- define or revise the claim under test;
- define invariants and failure expectations;
- define test oracles and acceptance thresholds;
- decide which mutation, fuzz, property, benchmark, integration, or adversarial techniques are required;
- approve a justified change to gate semantics;
- decide whether a survivor/failure is equivalent, irrelevant, unresolved, or assurance-significant when deterministic tooling cannot decide it.

### Persistent executor may

- modify implementation within the approved scope;
- add or extend tests that preserve the approved oracle;
- make mechanical fixture/configuration changes required to exercise that oracle;
- run targeted local tests repeatedly;
- run long-lived mutation, fuzz, property, service, database, container, migration, restart, or replay loops;
- inspect deterministic logs and artifacts;
- propose a gate change when the existing obligation is shown to be defective or infeasible.

### Persistent executor may not silently

- weaken an invariant, oracle, or acceptance threshold;
- lower a mutation/fuzz/coverage threshold merely to obtain green status;
- remove hard cases or narrow test scope merely to obtain green status;
- convert a failing or unresolved case into an exclusion without approved rationale;
- suppress, delete, or omit material failing evidence from the handoff;
- redefine what counts as equivalent or non-significant when judgment is required;
- self-approve a material checkpoint.

A requested gate change is a new design/checkpoint decision. It must be visible as such and reviewed by the authority that owns the gate.

## Local-first convergence

Persistent local execution is preferred when state continuity and repetition dominate the cost of the work. Typical examples include:

- repeated edit-test-debug cycles;
- targeted unit/contract/integration pytest loops;
- mutation testing;
- fuzz/property/state-machine execution;
- local database or service iteration;
- Docker/container integration;
- migration rehearsal;
- restart/resume/recovery testing;
- long-running deterministic tool execution;
- log inspection and mechanical spec-conforming repair.

Local-first does **not** mean local-only. Where CI or another independent boundary is required by the applicable assurance module, final candidate evidence still includes that independent attestation.

Local-first is normally unnecessary when:

- the task is a one-shot judgment or architecture decision;
- the result depends primarily on external review rather than repeated execution;
- the work is too small for persistent state to matter;
- the only meaningful environment is already the independent integration environment.

## CI role

CI remains mandatory whenever the applicable project/module contract requires it.

For iterative assurance work, CI should primarily establish properties such as:

- clean checkout and declared dependency reconstruction;
- environment independence;
- packaging/build reproducibility;
- compatibility across declared environments;
- absence of dirty local assumptions or undeclared state;
- execution of the configured repository gate at an exact candidate revision;
- durable, independently addressable evidence.

CI may also execute expensive assurance techniques when appropriate. This policy only rejects using remote CI as the default interactive debug loop when a persistent local executor can converge more efficiently without weakening independence.

A green CI run proves only the checks it actually executed. It does not expand the semantic scope of the claim.

## Task-routing policy

| Work type | Default authority/executor |
| --- | --- |
| product definition, PDD, SDD, architecture | assurance architect / high-reasoning review |
| invariants and failure semantics | assurance architect / high-reasoning review |
| threat modeling | assurance architect / high-reasoning review |
| acceptance criteria and test-oracle design | assurance architect / high-reasoning review |
| mutation/fuzz/property policy and survivor semantics | assurance architect / high-reasoning review |
| repeated implementation convergence | persistent executor |
| targeted local test loops | persistent executor |
| mutation/fuzz/property execution | persistent executor, using deterministic tools |
| local service/database/container iteration | persistent executor |
| migration/restart/recovery rehearsal | persistent executor |
| clean reproducibility and environment independence | CI or equivalent independent attestation |
| evidence interpretation and residual-risk judgment | checkpoint reviewer / high-reasoning review |
| checkpoint acceptance | checkpoint authority; never the executor acting unilaterally |

The policy optimizes reasoning quality rather than model prestige. Use stronger reasoning where ambiguity and judgment dominate; use inexpensive persistent execution where repetition and state continuity dominate; use deterministic tools whenever deterministic tools can decide the question.

## Candidate handoff contract

Before checkpoint review, the executor should hand off a candidate with enough exact state to reproduce and audit the claim. At minimum, material assurance work should identify:

- the project/repository and exact candidate revision or equivalent immutable identity;
- the assurance module, requirement, issue, or checkpoint being targeted;
- the frozen gate/oracle/threshold identity or durable reference;
- local commands or tool invocations used for convergence;
- test/mutation/fuzz/property/service receipts that materially support the claim;
- the independent attestation result and exact revision it evaluated, when required;
- unresolved failures, survivors, risks, exclusions, or environment differences;
- any requested gate change, explicitly separated from ordinary implementation changes;
- the reviewer/authority that must decide the checkpoint.

A candidate is not ready for acceptance when its exact revision is unknown or when material failing evidence has been omitted.

## Compatibility with existing PAM checkpoint semantics

This policy does not add a universal `verified` state and does not change the Project Assurance Manifest requirement-state vocabulary.

- `pending`, `satisfied`, `not_applicable`, `deferred`, and `blocked` retain their existing meanings.
- Existing module closure rules remain authoritative for what evidence is required.
- CI remains one evidence kind among the evidence types admitted by each module; it is not automatically sufficient for semantic correctness.
- `human_review` remains explicit evidence where judgment is inherent.
- Structured handoff remains the place for resumable project execution state. Execution-topology declarations must not make stale handoff prose override live repository/CI truth.
- Historical manifests and module identities are not rewritten because this policy exists.

The policy constrains **how evidence is produced and approved**. It does not replace module-specific closure rules.

## Proposed machine contract

Do not add executor identities or model names directly to every reusable `module.yaml`. Those values are adopter-specific execution state and would blur PAM's methodology/runtime boundary.

If repeated adoption demonstrates that machine validation is valuable, add a separate adopter-owned contract, tentatively `pam-execution-topology/0.1.0`, referenced as evidence by the project or by a future governance module.

A future contract should represent, at minimum:

- `schema_version`;
- project/checkpoint/module or requirement scope;
- role declarations for architect, executor, independent attestation, and checkpoint reviewer;
- actor class/capability description without requiring a vendor-specific model name;
- local-first enabled/disabled state with rationale;
- executor authority flags;
- forbidden executor authorities;
- exact stop condition;
- independent attestation mechanism and required evidence identity;
- candidate handoff requirements, including exact revision;
- gate-change request and approval state;
- unresolved-risk disclosure requirements.

The validator should fail closed for unknown contract versions and for topologies that grant the optimizing executor authority to weaken the gate or self-approve a material checkpoint.

## Proposed deterministic tests for that contract

A future machine contract should include positive and negative coverage for at least:

1. valid local-first topology with separate reviewer and CI attestation;
2. executor granted `redefine_gate` authority -> reject;
3. executor granted `weaken_gate` authority -> reject;
4. executor granted `self_approve_checkpoint` authority -> reject for material gates;
5. local-first enabled with no independent attestation where CI is required -> reject;
6. candidate handoff missing exact revision -> reject;
7. candidate handoff omitting unresolved-risk disclosure -> reject;
8. gate-change request treated as ordinary implementation evidence -> reject;
9. unknown schema version -> reject;
10. historical `pam-manifest/0.1.0` and existing module identities remain valid without migration.

## Migration and versioning

This documentation policy is additive and does not require migration of existing PAM artifacts.

If the proposed machine contract is later implemented:

- add it as a new specialized schema identity rather than mutating historical artifacts;
- preserve `pam-manifest/0.1.0` and existing module/profile identities;
- introduce a new governance module or profile version only if routing/closure semantics materially change;
- require adopter migration only when that adopter explicitly opts into the new module/profile or checkpoint contract;
- keep historical execution evidence immutable and pinned to the methodology revision that governed it.

Do not version a module merely to add prose clarification that does not change its requirements, applicability, or closure evidence. Do version a module/profile when execution-topology obligations become required closure semantics rather than advisory policy.
