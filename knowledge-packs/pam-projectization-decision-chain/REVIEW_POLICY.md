# Review policy — PAM projectization decision chain

This pack preserves reviewed working decisions and proposed claims from the Project Assurance Modules bootstrap discussion.

## Authority boundary

- Source records preserve the reviewed discussion context.
- Entries in `claims.json` are **proposed claims only**.
- Ingestion into FOSSIL or successful schema validation does not promote these claims to accepted project truth.
- Acceptance/promotion remains a separate human/project decision and should bind the exact source/claim revision being reviewed.
- Later changes supersede through new records/events; historical source and proposal identities are not rewritten.

## Suitable promotion targets

The highest-value durable lineage is:

- why PAM exists and what problem it is intended to solve;
- the projectization/build-vs-reuse/scope-control boundaries;
- the separation between PAM operational state and FOSSIL provenance;
- the benchmark anti-contamination protocol and limitations;
- later reviewed module/profile/schema changes and benchmark conclusions.

Ordinary scratch reasoning, trivial checklist transitions, and every intermediate agent thought should not automatically become accepted knowledge.

## Benchmark integrity

The finished `Pukujan/research-assurance` project is forbidden input to the blinded candidate run. This knowledge pack itself may mention the existence and benchmark role of that reference project, but it must not contain its finished issue hierarchy, milestone numbering, repository tree, exact project plan, or evaluator answers.

If a future edit adds such answer material, it must not be included in the candidate allowlist for an existing benchmark version.
