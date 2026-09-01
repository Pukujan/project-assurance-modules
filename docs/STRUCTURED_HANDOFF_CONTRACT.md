# Generic structured-handoff contract

PAM ships `schemas/structured-handoff.schema.json` as a reusable, fail-closed state contract for material cross-session, cross-agent, or cross-repository work.

## Contract identity

The first generic schema identity is `pam-handoff/0.1.0`.

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

## Exact identities

The methodology identity requires a 40-character Git commit SHA for the PAM revision. Component identities use typed values so Git commits, versions, digests, immutable URIs, or another explicitly named identity scheme can be represented without assuming every component is a Git repository.

For `git_commit` identities the validator enforces a full 40-character lowercase hexadecimal SHA.

## Hidden evaluation boundary

Agent-visible handoffs must not contain hidden or confirmatory labels, answers, seeds, or reports. `hidden_evaluation.agent_visible_hidden_material` is therefore fixed to `false`. A project with no hidden evaluation may simply say so in the policy text.

## Research Assurance migration boundary

`Pukujan/research-assurance` remains the reference implementation that motivated this extraction. Its local `ra-handoff/1.0.0` schema, state, validator, and tests are not replaced by this contract.

Migration from a project-local handoff contract to `pam-handoff/0.1.0` requires explicit parity review, project-owner approval, and a versioned migration. PAM must not silently rewrite an adopter's current-state contract.

## Validation

Run:

```text
python -m scripts.pam_handoff <handoff.json>
```

The normal PAM check lane also validates `examples/HANDOFF_STATE.example.json` and runs positive and negative schema tests.
