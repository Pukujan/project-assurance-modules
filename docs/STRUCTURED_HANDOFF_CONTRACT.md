# Generic structured-handoff contract

PAM ships versioned reusable, fail-closed state contracts for material cross-session, cross-agent, or cross-repository work.

## Contract identities

The original generic schema identity is `pam-handoff/0.1.0`, implemented by `schemas/structured-handoff.schema.json`.

`pam-handoff/0.2.0`, implemented by `schemas/structured-handoff-v0.2.schema.json`, is an additive versioned contract created after explicit Research Assurance parity review. It preserves the v0.1 semantics and additionally makes these routing identities first-class:

- project `observed_identity`;
- project `active_issue`;
- component `issue` and `pr` references.

The v0.1 schema remains unchanged and fail-closed. The validator dispatches by exact `schema_version`; fields introduced in v0.2 are not silently accepted by v0.1.

A handoff records the exact PAM repository revision used by the project plus the selected module identities. The schema contract version and the methodology repository revision are separate identities and must not be conflated.

## Authority and resume semantics

A handoff is durable execution context, not an authority override. Live repository, issue, pull-request, CI, and component state supersede stale observations in a handoff.

A resumed worker must:

1. validate the handoff deterministically;
2. read the exact next action, blockers, phase, and scope exclusions;
3. execute the listed reconciliation checks against live mutable state;
4. stop and reconcile or refresh and revalidate if the handoff is stale;
5. mutate project state only after reconciliation.

The schema therefore requires `reconciliation.live_state_wins` to be `true` and requires at least one explicit live-state check.

## Current state versus historical checkpoints

`state_kind` distinguishes:

- `current`: replaceable resumable state intended to describe the present execution checkpoint;
- `historical_checkpoint`: an immutable or append-only record retained for material lineage or transition evidence.

Projects may keep only current state when historical checkpoints have no value, but they must not present an old checkpoint as current execution truth.

## Exact identities and routing references

The methodology identity requires a 40-character Git commit SHA for the PAM revision. Component and project identities use typed values so Git commits, versions, digests, immutable URIs, or another explicitly named identity scheme can be represented without assuming every component is a Git repository.

For `git_commit` identities the validator enforces a full 40-character lowercase hexadecimal SHA.

In `pam-handoff/0.2.0`, `project.active_issue` and each component's `issue`/`pr` keys are required fields whose values may be null. This keeps issue/PR routing explicit without pretending every project or component has a GitHub work item.

## Hidden evaluation boundary

Agent-visible handoffs must not contain hidden or confirmatory labels, answers, seeds, or reports. `hidden_evaluation.agent_visible_hidden_material` is therefore fixed to `false`. A project with no hidden evaluation may simply say so in the policy text.

## Research Assurance migration boundary

`Pukujan/research-assurance` remains the reference implementation that motivated this extraction. Its local `ra-handoff/1.0.0` schema, state, validator, and tests are not automatically replaced by PAM.

The first parity review found that `pam-handoff/0.1.0` could express RA's core resume semantics but could not losslessly preserve three machine-readable routing facts: the observed program identity, the program-level active issue, and per-component issue/PR references. `pam-handoff/0.2.0` exists specifically to close those generic representation gaps without weakening or rewriting v0.1.

Migration from a project-local handoff contract to a PAM handoff still requires:

1. explicit parity review against the exact target schema version;
2. deterministic validation of an adopter-owned candidate state;
3. project-owner approval;
4. a versioned migration that preserves live-state authority and hidden-evaluation boundaries.

A green PAM parity fixture is evidence that the generic contract can represent the adopter state; it is not migration approval and does not make PAM a runtime dependency.

## Validation

Run:

```text
python -m scripts.pam_handoff <handoff.json>
```

The normal PAM check lane validates both `examples/HANDOFF_STATE.example.json` (`0.1.0`) and `examples/HANDOFF_STATE.v0.2.example.json` (`0.2.0`) and runs positive and negative schema tests.
