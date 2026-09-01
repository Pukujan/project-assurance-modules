# Project plan

This is a proposed plan. Owner review of the manifest, scope boundary, and reuse decisions is the entry gate for any implementation issue; no issue is authorized merely by this document.

## M0 — adopt composition and prove seams

**Objective.** Turn the research packet into an executable, version-pinned first-slice contract without building a duplicate substrate.

**Scoped capability.** Select one finance promotion type, source authority, review authority, and exact references for existing systems; define typed promotion states and invariant/failure register.

**Dependencies / entry.** Owner approves preflight and supplies or authorizes immutable component references and licenses.

**Evidence.** A composition lock/receipt; ownership map; policy draft; FOSSIL contract probe covering whole-artifact integrity, review reference authority, failed ingest/orphan behavior, actor attribution, crash/replay, and rebuild; deterministic handoff schema plus positive and negative fixtures.

**Exit gate.** Either a version-pinned reuse/wrap decision with documented seam behavior, or a narrow evidence-backed change request to the owning system. No broad new implementation is admitted until this gate passes.

**Non-scope.** Dataset/model tuning, graph/vector infrastructure, universal scoring, and harness adapters.

## M1 — first fail-closed promotion slice

**Objective.** Implement one thin `promotion-assurance` adapter around the approved evidence substrate and finance workflow.

**Scoped capability.** Create a proposed promotion containing immutable evidence references and individual integrity/citation/temporal/numeric/identity/authorization/review results; accept only when the policy's required results and exact review binding are present.

**Dependencies / entry.** M0 lock, selected promotion type, explicit source authority, and passing adapter contracts.

**Evidence.** PDD/SDD/invariants/failure register; deterministic unit and contract tests; no-network CI; fixtures for wrong evidence root, altered artifact, missing/stale review, wrong actor, wrong time/version, missing citation, and unavailable dependency; one end-to-end replayable finance fixture.

**Exit gate.** The accepted path is replayable from pinned evidence and policy; every required failed check leaves the work exploratory/proposed and cannot synthesize acceptance.

**Non-scope.** Proof of general semantic correctness, generic model verification, or cross-domain support.

## M2 — resilience and evidence-boundary validation

**Objective.** Validate stateful and persistent boundaries before widening workflow coverage.

**Scoped capability.** Make failed/partial/retry/rebuild/redaction paths preserve authoritative identity and make state transitions fail closed.

**Dependencies / entry.** M1 vertical slice and deterministic baseline green.

**Evidence.** Property/state-machine, metamorphic, mutation, and fault-injection campaigns; adverse review; documented residual risks and remediation/defer decisions.

**Exit gate.** Critical deterministic controls demonstrate fault detection and recovery/replay behavior; residual risks have owner-approved disposition.

**Non-scope.** Adding retrieval/model quality as an acceptance requirement.

## M3 — bounded empirical claims

**Objective.** Evaluate retrieval, source-suitability, and any semantic-support mechanism as separate fallible claims.

**Scoped capability.** Versioned development evaluation and, only if tuning is adaptive, a protected confirmatory evaluation. Finance retrieval and claim tasks have independent metrics and reports.

**Dependencies / entry.** M1/M2 evidence boundary passing; dataset admission cards; owner-approved task/metric/authority; hidden split governance if applicable.

**Evidence.** Immutable dataset/corpus/query/qrels or label manifests; baseline and ablation reports; composition tests; cost/friction report; holdout access controls; explicit no-benefit/kill decision where effect is absent.

**Exit gate.** Each empirical claim names its population, metric, versioned inputs, uncertainty, and non-transfer boundary. No result becomes a generic acceptance signal.

**Non-scope.** Training a model because a benchmark exists; merging retrieval and synthesis scores.

## M4 — optional continuity/harness experiment

**Objective.** Test, rather than assume, whether a local research-state/HITL layer improves cross-session research continuity.

**Scoped capability.** Plugin-first, transport-neutral local protocol with forced interruption/restart, exact review binding, and cross-model handoff on frozen microworlds.

**Dependencies / entry.** M0 handoff and idempotency controls green; a fixed protocol, cost budget, and success/no-benefit thresholds approved.

**Evidence.** Deterministic state/restart/idempotency tests before model spend; fixed-seed microworld records; comparison report; protocol-failure and friction data; no hidden confirmatory content in handoffs.

**Exit gate.** Adopt an adapter only for measured benefit that exceeds its cost/friction; otherwise record `NO_MEASURABLE_BENEFIT` and keep it out of the core.

**Non-scope.** A generic agent governance plane.
