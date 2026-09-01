# Project preflight and routing

## Entry condition

Do not run this process simply because an idea exists.

The normal entry signal is an explicit human/project-owner decision such as:

> Research is mature enough to consider projectization. Run Project Assurance preflight before creating the implementation plan.

The preflight may identify that more research is needed. It does not manufacture a pass.

## Preflight outputs

Before large-scale repository/issue/project bootstrap, produce:

1. declared project facts and intended claims;
2. selected profile candidates;
3. routed module dispositions;
4. gap analysis;
5. explicit `not_applicable` / conditional / defer rationales;
6. reviewed `PROJECT_ASSURANCE` manifest pinned to an exact methodology revision;
7. only then, a project bootstrap plan (specs, repository layout, issue hierarchy, CI/validation plan, benchmark plan, continuity plan, release gates).

## Initial project facts

The v0 router should be able to reason from facts such as:

- project is software / research-only / mixed;
- implementation languages/ecosystem;
- expected lifetime and number of material sessions;
- agent-assisted development expected;
- single repository vs multi-repository composition;
- persistent/stateful behavior;
- concurrency/distributed execution;
- security/authorization boundary;
- external/network dependencies;
- empirical quality/performance claims;
- stochastic/model behavior;
- benchmark or dataset use;
- hidden/confirmatory evaluation required;
- domain-specific temporal/version semantics;
- human-in-the-loop decisions;
- consequential external actions;
- reproducibility/provenance requirements;
- prior research/discussion worth preserving as lineage;
- public/open-source release expectations;
- migration/replay/rollback requirements.

Facts are declarations, not proof. The preflight may request evidence or human clarification where misclassification would materially alter requirements.

## Dispositions

Each candidate module receives one routing disposition:

- `required` — omission would leave a current project claim, boundary, or continuity need materially unsupported;
- `recommended` — strong default with meaningful likely value, but not a hard precondition;
- `conditional` — applicability depends on a fact/decision not yet resolved;
- `not_applicable` — explicitly excluded with rationale.

Execution state is tracked separately in the project manifest (`pending`, `satisfied`, `not_applicable`, `deferred`, `blocked`).

## Routing principles

1. Prefer cheap/deterministic techniques before expensive/stochastic ones.
2. A technique is not required merely because the repository contains a module for it.
3. Riskier claims and irreversible boundaries justify stronger validation.
4. Empirical/model quality claims require benchmark methodology; deterministic identity/integrity claims should prefer deterministic tests.
5. Hidden holdouts apply only when adaptive tuning/contamination is a meaningful threat.
6. Formal methods apply only when the state/concurrency problem and expected value justify them.
7. FOSSIL/provenance modules apply when durable research/decision lineage is valuable; they do not prove semantic correctness.
8. GitHub Projects/complex issue hierarchies should scale with project complexity, not be ceremonial requirements for tiny projects.
9. Agent continuity applies when work will span sessions/agents/harnesses; it should not require checkpoint churn after trivial actions.
10. Uncertainty must not silently route to `not_applicable`.

## Human review boundary

The router may propose the preflight. A human/project owner should review material exclusions, disputed project facts, consequential waivers, and the final transition into implementation planning.

The human should not need to manually remember every module; the point of this repository is to surface them.

## Repeatability target

A fresh capable agent should eventually be able to receive only:

> Read `Pukujan/project-assurance-modules`. Research is mature enough. Run preflight for this project before creating anything.

plus the project's durable research/context, and produce the same material module selection as another capable agent within declared ambiguity. Differences should be visible as routing rationale rather than hidden prompt behavior.
