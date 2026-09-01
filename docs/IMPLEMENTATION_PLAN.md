# PAM v0 executable implementation plan

## Objective

Turn the current methodology specification into a small deterministic substrate that can validate modules/manifests, route a bounded first set of project facts, render evidence-backed gaps, and support the blinded retrospective planning benchmark without becoming a runtime service.

## Gate 0 — contracts

Before planner experiments count:

- module schema validates every shipped module;
- Project Assurance Manifest schema validates positive fixtures and rejects invalid states;
- unknown schema/module versions fail safely;
- satisfied requirements require evidence;
- N/A/deferred/blocked requirement states require rationale;
- module IDs/versions referenced by a manifest must resolve at the pinned methodology revision;
- no generic `verified=true` field is accepted.

## Gate 1 — deterministic routing vertical slice

Implement a small router over explicit project facts. Initial rules need only cover the currently extracted portable modules:

- `continuity.structured-handoff` when work spans material sessions/agents/harnesses;
- `projectization.build-vs-reuse` for nontrivial software projectization where reusable systems may exist;
- `projectization.scope-boundary` for nontrivial projectization with horizontal scope risk.

Routing output is a candidate disposition with rationale. Human review remains required for material waivers/uncertainty. The router must never silently convert an unknown fact into `not_applicable`.

## Gate 2 — evidence/gap validator

Given a project manifest:

- resolve selected modules;
- verify every module requirement is represented;
- reject unknown requirement IDs;
- reject `satisfied` without allowed evidence kinds;
- require N/A/defer rationale;
- emit a deterministic gap report for pending/blocked/conditional work.

Markdown checklists may be rendered from this state but must not become authoritative.

## Gate 3 — methodology tests

Required test classes for v0:

- schema positive/negative fixtures;
- module resolution/version-pin tests;
- routing table tests;
- metamorphic tests: reordering project facts/modules must not change semantic routing;
- mutation-sensitive tests for evidence/rationale closure rules;
- negative tests for unknown schemas/modules/requirements and forbidden universal verification fields;
- deterministic repeated-run equality.

## Gate 4 — first two adopters

1. `Pukujan/research-assurance` structured handoff is the first reference adoption.
2. `Pukujan/RA-plugin` should adopt the generic structured-handoff/projectization contracts only after v0 validators are green.

Do not claim stable v1 until at least two materially distinct projects can adopt without bespoke methodology edits.

## Gate 5 — blinded retrospective benchmark

Freeze the PAM revision and run `experiments/ra-retrospective-blind` with a fresh candidate planner that cannot access the finished Research Assurance project. Candidate output is frozen before evaluation.

This is development/conformance evidence only. A later unseen project is required for generalization evidence.

## Non-scope for this implementation slice

- runtime service/MCP server;
- automatic GitHub repository/issue creation;
- live web OSS search automation;
- full catalogue of planned modules;
- FOSSIL runtime dependency;
- autonomous methodology waivers;
- LLM-based scoring as the sole benchmark oracle.
