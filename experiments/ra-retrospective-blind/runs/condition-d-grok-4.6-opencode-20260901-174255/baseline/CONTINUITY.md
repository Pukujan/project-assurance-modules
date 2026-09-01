# Continuity

A later human or agent must be able to resume without this chat.

## Read order for a new session (post-accept implementation)

1. `HANDOFF.md` in this bundle (or the RPP repo README once it exists)
2. `PLAN.md` §§2–6 (product, non-scope, dimensions, invariants)
3. `DECISIONS.md`
4. `ISSUES.md` current epic
5. `FAILURE_MODES.md` for the component being touched
6. lockfiles (`COMPONENTS.lock.json`, `DATASETS.lock.json`) once they exist
7. open issue text, not remembered chat

## What is durable

- Promotion records and evidence identities (FOSSIL)
- Pins and dataset manifests
- Decision records
- Public-dev fixtures
- Test reports stored as artifacts

## What is not durable

- Chat
- Unrecorded “we decided to…”
- Index contents
- Agent self-attestation

## Session start checklist

- Confirm you are not in the forbidden reference repo.
- Confirm lockfile SHAs still match the issue you are closing.
- If you need a new mechanism, stop and write an admission; do not silently expand scope.
- If you are about to close a promotion-related issue with “I verified it,” attach the evidence kind required by that issue instead.

## Benchmark freeze

Run `condition-d-grok-4.6-opencode-20260901-174255` is complete and frozen. Do not patch this directory after feedback.
