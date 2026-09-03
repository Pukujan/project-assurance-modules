# Product Definition Document — Project Assurance Modules

## Problem

Research-backed projects repeatedly depend on a human or capable agent remembering the same engineering disciplines before implementation begins: product definition, system design, invariants, failure analysis, SWE foundations, CI, testing strategy, benchmark integrity, scope control, provenance, GitHub planning, continuity, release evidence, and other project-specific obligations.

That memory-based process is inconsistent across sessions, models, harnesses, and projects. It also encourages premature issue/repository creation before the project has frozen what it is trying to prove and how completion will be evidenced.

A second failure mode is **evidence circularity**: an agent can sometimes author a convincing decision document and then cite that same document as proof that the underlying research or comparison was actually performed. PAM must distinguish durable conclusions from traceable source/search evidence where the methodology claim depends on work external to the conclusion itself.

## Product hypothesis

A versioned registry of independent assurance-methodology modules, combined through routed profiles and frozen into a project-specific manifest, can make the transition from completed research to engineered project repeatable without turning the process into a universal agent-control protocol.

## Primary users

- a human project/research owner deciding that exploration is mature enough to become a project;
- an AI orchestrator preparing a new project from durable research;
- implementation agents that need explicit, versioned requirements and closure evidence;
- reviewers auditing which engineering methodology a project actually followed.

## Trigger

The methodology begins only after a human or authorized project owner decides that enough exploratory research has been done to run **project preflight**.

It does not decide when research is intellectually complete.

## Core workflow

```text
research / exploration
        |
human: "run project preflight"
        |
collect project facts + intended claims
        |
route applicable modules/profiles
        |
gap analysis
        |
human review of required / conditional / N/A dispositions
        |
freeze PROJECT_ASSURANCE manifest against exact methodology revision
        |
produce project specs / repo plan / issue hierarchy / validation plan
        |
implementation closes requirements with evidence
        |
release/milestone claims refer to exact evidence
```

## Goals

1. Make "what did we forget before building?" mechanically inspectable.
2. Separate reusable methodology from project-specific architecture and state.
3. Route requirements based on project/task characteristics rather than forcing every project through every technique.
4. Version modules and profiles so a project can state exactly which methodology revision it adopted.
5. Require evidence-backed closure instead of agent self-attestation or ceremonial checkboxes.
6. Allow explicit `not_applicable`, `deferred`, and `blocked` states with rationale.
7. Support humans, ChatGPT, Codex, OpenCode, BYOK harnesses, and other agents without model-specific semantics.
8. Make project bootstrap (specs, GitHub issues/projects, CI plan, benchmark plan, handoff policy) an output of reviewed preflight rather than an ad-hoc first action.
9. Use specialized machine-valid evidence contracts where structural manifest validation alone cannot prevent circular or self-referential closure.

## Non-goals

- universal agent governance or per-response stamping;
- determining whether research conclusions are true;
- replacing Research Assurance or FOSSIL;
- a runtime authorization service;
- making every available methodology mandatory;
- auto-creating repositories/issues before preflight is reviewed;
- replacing domain-specific architecture, security, legal, medical, or scientific review;
- turning "best practice" preferences into requirements without an applicability argument.

## Core objects

- **Module** — one independently versioned engineering/assurance methodology with applicability, requirements, evidence expectations, and non-scope.
- **Profile** — a composable starting set of modules for a project/task class.
- **Project facts** — declared properties used by routing, such as statefulness, distributed execution, empirical quality claims, human consequences, multiple repositories, or agent-assisted development.
- **Routing result** — required/recommended/conditional/not-applicable module dispositions with rationale.
- **Project Assurance Manifest** — the reviewed, project-specific frozen methodology selection and requirement state.
- **Evidence reference** — concrete artifact showing why a requirement may be considered satisfied.
- **Specialized evidence contract** — a domain-specific machine-valid artifact used when a requirement must establish traceable underlying work, not merely the existence of an authored conclusion.

## Requirement state vocabulary

Use narrow states:

- `pending` — applicable but not yet satisfied;
- `satisfied` — closure evidence exists;
- `not_applicable` — excluded with explicit rationale;
- `deferred` — intentionally moved beyond the current project/milestone with rationale;
- `blocked` — applicable but currently impossible to complete.

Do not use a universal `verified=true` state.

## Trust boundary

Models/agents may propose:

- project facts;
- module applicability;
- N/A/defer rationales;
- project artifacts and evidence references;
- candidate searches, comparisons, and implementation dispositions.

Deterministic tooling owns:

- schema validation;
- version identity;
- manifest structural consistency;
- required evidence presence rules;
- profile/module resolution;
- generated checklist consistency;
- specialized fail-closed invariants that can be established mechanically, such as forbidding self-referential reuse candidates, requiring traceable search receipts, and resolving referenced evidence contracts.

Deterministic validation does not prove that every human judgment is true. It should, however, reject evidence structures that are known to permit circular closure or that contradict a versioned contract.

Humans/project owners own:

- the decision that research is mature enough for projectization;
- disputed scope/applicability decisions;
- consequential methodology waivers;
- final acceptance when judgment cannot be reduced to a deterministic oracle.

## Success criteria for a stable v1

- at least two materially different real projects adopt the methodology;
- a fresh agent with no prior conversation can run preflight from project facts and pinned methodology state;
- module routing does not require project-specific hidden prompt knowledge;
- satisfied requirements point to concrete evidence;
- invalid/unknown module or manifest versions fail safely;
- the process materially reduces repeated human prompting without creating high protocol-induced failure or checklist bureaucracy;
- projects can reject/defer irrelevant modules without editing the methodology source.

## Kill/redesign criteria

Redesign or reject the approach if:

- most projects require extensive bespoke exceptions that defeat routing;
- agents optimize for checklist completion rather than project outcomes;
- self-authored conclusions can repeatedly pass as proof of the research or comparison they claim to summarize;
- the methodology creates substantial work with no decision/quality/continuity benefit;
- module boundaries become a second architecture monolith;
- the system requires a runtime service merely to maintain planning state;
- version/profile complexity becomes harder to understand than project-specific documentation.

## Reference precedent

`Pukujan/research-assurance` is the first reference source because its planning was developed manually before this methodology existed: PDD/SDD/invariants, failure register, validation strategy, SWE/CI foundation, benchmark integrity, scope control, adversarial review, FOSSIL decision lineage, GitHub issue hierarchy, multi-repository orchestration, and structured handoff. Those patterns are candidates for extraction, not automatically universal requirements.

`Pukujan/interview-os-game` exposed the first concrete build-vs-reuse evidence-circularity defect: a plausible free-form candidate register could satisfy the older requirement without demonstrating sufficiently concrete alternative and reusable-asset discovery. That defect is tracked as PAM issue #10 and motivates the versioned build-vs-reuse hardening rather than a silent rewrite of historical methodology.
