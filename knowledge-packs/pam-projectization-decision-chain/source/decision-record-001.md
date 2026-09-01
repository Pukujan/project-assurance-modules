# PAM projectization and blind-planning benchmark decision record

Date: 2026-09-01
Status: reviewed working decision record for Project Assurance Modules bootstrap

## Why PAM exists

Project Assurance Modules (PAM) is intended to make the transition from completed research into an engineered project repeatable across humans, ChatGPT, Codex, OpenCode and other harnesses. The reusable repository should contain versioned methodology modules, routing rules, schemas, validators and evidence-backed closure requirements. An adopting project owns its own live Project Assurance Manifest and implementation evidence.

The motivating failure mode is repeated human prompting: project owners should not need to remember to ask every new agent about PDD/SDD, invariants, failure analysis, CI, lint/types, property/metamorphic/mutation/fault tests, benchmarks, hidden holdouts, GitHub issue/project structure, scope control, provenance and handoff continuity.

## Projectization gate

PAM should include a pre-build projectization boundary before large repository/issue/code generation. The gate asks:
1. should this capability be built at all, or can an existing maintained system be reused/configured/wrapped/extended/composed/forked?
2. if something must be built, what is the smallest justified scope?

The durable projectization outputs should include a compact research handoff, build-vs-reuse assessment, scope boundary and frozen Project Assurance Manifest before detailed project bootstrap.

A bespoke `build_new` decision must earn itself with concrete unmet requirements or unacceptable trade-offs. Where cheap evidence is available, a spike, compatibility probe, contract test or benchmark is preferred over prose-only rejection.

Scope control should preserve current goals/claims, explicit non-goals, deferred/rejected mechanisms and reconsideration triggers. A red-team finding or attractive technology is evidence, not an automatic roadmap requirement.

## PAM versus FOSSIL

PAM/project Git state and FOSSIL have separate roles.

PAM answers which methodology applies now, what is pending and what evidence closes each project requirement. FOSSIL preserves durable evidence and lineage for consequential research/project decisions.

Exploration should remain cheap in transcripts/notes. At projectization, a compact reviewed handoff and material decisions can be promoted into Git operational artifacts and, where useful, ingested into FOSSIL. FOSSIL should not become the live checklist/task tracker and every exploratory thought should not require ingestion.

## Structured handoff precedent

Research Assurance is the first reference adopter of a machine-validated structured handoff. The normal continuation path is intended to be AGENTS + validated handoff state + human-readable handoff + cheap reconciliation against live GitHub state. A full cold-start reconstruction remains a periodic conformance test rather than normal session startup.

## Retrospective Research Assurance benchmark

PAM should be tested against the project-planning process that originally motivated it. A fresh candidate planner receives a frozen pre-project research packet and frozen PAM revision, but must not access the finished `Pukujan/research-assurance` repository or any of its issues/PRs/docs/project state.

The candidate writes its planning bundle into an isolated experiment run directory in PAM. Only after the candidate output is frozen does an evaluator compare it with the finished reference project.

This is a retrospective development/conformance benchmark, not a clean generalization benchmark, because PAM itself was extracted from Research Assurance planning.

The benchmark should score semantic planning equivalence rather than byte-for-byte reproduction. Equivalent filenames, issue numbers or decompositions are allowed. Material boundaries, validation obligations, ownership, scope and evidence discipline matter.

A run is contaminated if the candidate accesses the finished Research Assurance project. The candidate must produce an access attestation and must not modify PAM methodology during the run. Methodology gaps are recorded separately.

## Model/harness separation

A fresh cloud Sol session is preferred as the first candidate planner so planning quality is not confounded by weaker local models. The candidate must be a fresh session with no finished Research Assurance context and explicit forbidden-source instructions.

Terra/Luna remain useful later for implementation/conformance work, but the retrospective benchmark should distinguish methodology quality from planner capability. Future experiments can deliberately compare planners/harnesses as a separate factor.

## Generalization requirement

A high retrospective score does not establish that PAM generalizes. After the retrospective development benchmark, PAM should be frozen and evaluated on at least one materially different project that did not contribute to the tested module definitions.
