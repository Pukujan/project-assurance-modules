# Replayable Promotion Program — project plan

Working name: **Replayable Promotion Program (RPP)**
Status: pre-implementation projectization, frozen for this baseline run
Input: `experiments/ra-retrospective-blind/TASK_PACKET.md` only
Not an attempt to reconstruct any unseen finished repository

## 1. Why this project exists

Research and software work routinely *promote* working material into something others will treat as true enough to act on: a conclusion, a benchmark number, an architecture decision, or shared knowledge.

The program exists to answer one narrow question:

> When a workflow promotes evidence into a consequential conclusion, benchmark result, architecture decision, or shared knowledge, what evidence and validation are required to justify that promotion and make it replayable?

The product is not a general agent governor. Exploration must remain possible when a promotion gate fails. A failed gate must not forge, silently skip, or back-date an accepted promotion.

## 2. Product definition

RPP is a small **promotion kernel** plus **pinned compositions** of already-owned systems, plus one **first-domain application loop**.

A *promotion* is a typed, identity-bound, reviewable transition:

| From | To | Typical consequence |
|---|---|---|
| working notes / retrieved passages | a claim or conclusion | others may cite it |
| rankings / eval runs | a published benchmark result | others may compare against it |
| design discussion | an architecture decision | later work is constrained by it |
| local draft knowledge | shared knowledge | later sessions treat it as given |

The kernel records, for each promotion:

1. exact artifact identities of inputs and outputs;
2. the promotion type;
3. independent dimension statuses (never a single `verified=true`);
4. which checkers ran, with versions and results;
5. whether human review was required and, if so, the exact claim/evidence binding reviewed;
6. a replay recipe sufficient to rebuild projections and re-run deterministic checks;
7. residual risk and any waived dimensions, named as waivers rather than hidden as success.

Exploration, drafts, failed attempts, and local notes are first-class and ungated. They may be stored, but they are not promotions.

## 3. Non-scope (explicit)

Do not implement in the first program unless a later, reviewed admission changes this list:

- governing every model response or ordinary coding action;
- a universal agent “stamp” / compliance overlay (prior approach failed: gaming, blockage, unclear actions, simultaneously too strict and too loose);
- GraphRAG / graph retrieval as a required substrate;
- ontology or meta-system platforms;
- cross-domain assurance packs (legal, medical, etc.) before the finance loop is real;
- importing entire external standards (PRISMA, Cochrane, SACM, PROV, SLSA, in-toto, RO-Crate) as runtime dependencies;
- collapsing retrieval quality, source quality, citation integrity, and claim correctness into one score;
- treating vector/graph indexes as evidence authority;
- requiring human review of trivial actions;
- making the agent/harness plugin a core dependency;
- exposing hidden confirmatory benchmark answers to implementation agents.

Attractive techniques and red-team findings are *candidates*. They do not become current work by existing.

## 4. Build versus reuse

Owner preference: reuse maintained systems and compose thinly when they already satisfy a scoped need. New code is justified only where existing systems do not provide the promotion contract.

### 4.1 Reuse as substrate (do not rebuild)

| Existing system | Role in RPP | First obligation |
|---|---|---|
| **FOSSIL Core** | durable immutable artifacts, exact citations, append-only history, lineage, reviewed promotion boundaries, redaction/rebuild/replay | pin exact revision; write an adapter; *empirically test* the integrity hypotheses in the packet rather than asserting them |
| **Retrieval Benchmarker** | independent retrieval evaluation on immutable corpora/queries/qrels; sparse/dense/hybrid/rerank; persisted rankings/reports; finance datasets | pin exact revision and dataset manifests; keep its scores in the retrieval layer only |
| **Financial analysis application** | first domain loop: SEC/financial evidence, temporal/version semantics, real user-facing research | pin revision; define which user actions are promotions vs exploration |

### 4.2 Reuse as bounded research dependency (not assumed runtime gate)

| Existing system | Role | Bound |
|---|---|---|
| **Source Ranker** | source suitability / quality / claim-source fit | broader than current proven implementation. Admit into a promotion path only after a scoped empirical comparison against a simpler baseline (e.g., authority-list + recency + document-type rules for SEC). If no measured benefit, keep as research, not as a gate. |

### 4.3 Build (thin, new)

- promotion record schema and state machine;
- dimensioned status model (no universal verified flag);
- deterministic checkers that FOSSIL/the apps do not already own: citation identity, temporal/version match, numeric extraction consistency where mechanical, authorization/actor attribution at the promotion boundary;
- replay/rebuild orchestration that treats indexes as disposable projections;
- dataset/composition identity manifests;
- public-dev vs hidden-confirmatory evaluation *process* (hidden material stays out of implementer context);
- finance promotion pack: source-authority policy, temporal/version gold cases, restatement/wrong-version fixtures;
- failure-mode register and residual-risk records;
- optional later: a killable agent-continuity experiment, plugin-first, after deterministic tests are green.

### 4.4 Defer until earned

Claim-verification productization, GraphRAG, ontology, MCP/ChatGPT adapters, TREC/BEIR-wide retrieval campaigns, FEVER/SciFact/AVeriTeC/RAGTruth/ALCE as runtime gates. Each may be admitted only with: scoped question, public-dev protocol, cost bound, and an allowed `NO_MEASURABLE_BENEFIT` / kill outcome.

## 5. Assurance dimensions (do not collapse)

These are separate. A promotion may be accepted on some dimensions, failed or waived on others, and still must not present a single Boolean success.

| Dimension | Question | Typical evidence |
|---|---|---|
| Source integrity | Is the artifact the bytes/identity we think it is? | FOSSIL snapshot identity, hash, ingest receipt |
| Citation integrity | Do citations point at the exact artifact/span claimed? | exact citation records, quote/offset checks |
| Temporal validity | Is the cited version valid at the as-of time? | filing dates, restatements, version lineage |
| Numeric validity | Are extracted numbers consistent with the cited artifact? | deterministic parsers, table/cell identity |
| Semantic support | Does the cited material actually support the claim? | human review and/or later scoped claim-eval; not a retrieval score |
| Retrieval quality | Did the retriever surface the right evidence *as a retriever*? | Retrieval Benchmarker reports on frozen qrels |
| Source suitability | Is this source an appropriate authority for this claim type? | policy/authority list; Source Ranker only if empirically earned |
| Authorization / actor | Who/what performed ingest, check, review, promotion? | attested actor identity, role bound into provenance |
| Human review | Was a consequential judgment actually reviewed against exact claim+evidence? | review binding record, not a stamp |
| Replayability | Can a later session rebuild projections and re-run deterministic checks? | recipe + pinned versions + dataset manifests |

Semantic correctness is not provenance. Retrieval correctness is not claim correctness. Source quality is not claim-source fit. Domain validity does not transfer from finance to other domains.

## 6. Core invariants

I-1. Exploration is never blocked by a failed promotion gate. Failed promotions remain failed; work may continue in ungated space.

I-2. An accepted promotion cannot be created by self-attestation, agent stamp, or “checklist complete” without the required evidence kinds for that promotion type.

I-3. No API, document, or UI may expose a universal `verified=true` that hides mixed dimension outcomes.

I-4. Indexes (vector, graph, search) are rebuildable projections. Promotion evidence cites FOSSIL (or equally immutable) artifact identities, not index rows.

I-5. Deterministic checks that can replace a stochastic judgment must be used for identity, citation targeting, numeric extraction against a cited cell, temporal/version match, and authorization.

I-6. Hidden confirmatory material is not present in the implementation repository, fixtures used by coding agents, or prompts.

I-7. Exact versions of every composed system and dataset used in a reported result are recorded. Historical promotions are not rewritten when dependencies evolve; new promotions cite new pins.

I-8. Domain packs are explicit. A finance-accepted promotion is not evidence for legal/medical/other domains.

I-9. Costly mechanisms (rerankers, LLMs, graphs, source rankers, agent plugins) require a scoped empirical question and may conclude `NO_MEASURABLE_BENEFIT`.

I-10. Assurance/checklist items attach to a specific promotion type or state transition and close with evidence, not with the agent saying it complied.

I-11. Research/work logs remain writable if the assurance substrate is down. Promotion *accept* is unavailable until the substrate can record the promotion honestly.

## 7. Promotion types and required evidence

Minimum set for v0. Additional types require a written admission.

### P-CLAIM — promote evidence to a consequential claim/conclusion

Required:

- immutable identities of cited artifacts and spans;
- citation-integrity check pass or named waiver;
- temporal-validity check if the claim is as-of dated (finance default: yes);
- numeric-validity check if the claim contains numbers taken from evidence;
- semantic-support: human review bound to the exact claim text and cited spans, **or** an admitted later automatic checker that has passed a public-dev protocol (none is assumed for v0);
- actor + timestamp;
- residual-risk note if any dimension is waived.

Not required: retrieval score threshold, source-ranker score, graph neighborhood.

### P-BENCH — promote an evaluation run to a shared benchmark result

Required:

- dataset manifest identity (corpus, queries, qrels, split: public-dev vs held-out);
- system composition pin (retriever/ranker/checker versions, configs);
- persisted rankings/reports as immutable artifacts;
- statement of which layer the number belongs to (retrieval vs citation vs claim vs substrate integrity);
- no mixing of layers into one headline number unless a separately defined composite is admitted (v0: not admitted);
- replay recipe.

### P-ARCH — promote discussion to an architecture decision

Required:

- decision text;
- alternatives considered;
- evidence/artifacts that motivated the choice;
- consequences / non-goals;
- reviewer identity for consequential decisions;
- FOSSIL (or equivalent) identity of the decision record.

### P-KNOW — promote local draft to shared knowledge

Required:

- exact source artifacts;
- claim-like statement or scoped fact;
- dimension statuses;
- review if the knowledge will constrain later agents/humans;
- expiry or as-of if temporal.

### Non-promotions (always allowed)

Drafts, search, failed experiments, notes, chat, speculative design. These may be snapshotted for lineage but must be labeled non-promoted.

## 8. Proposed system shape

Not a platform. Four layers, with existing repos remaining the systems of record where they already are.

```text
[ungated exploration]
        |
        v
[promotion request] --> deterministic checkers --> dimension record
        |                                              |
        v                                              v
[FOSSIL identities / receipts] <-------- replay/rebuild projections
        |
        +--> finance application actions that are promotions
        +--> retrieval-benchmarker runs that may be P-BENCH
        +--> optional source-ranker scores as *inputs*, never as sole accept
```

### 8.1 Suggested repository layout (new program repo)

Existing FOSSIL, Retrieval Benchmarker, Source Ranker, and the financial application stay in their own repositories. RPP is a composition/program repo that pins them.

```text
rpp/
  README.md
  docs/
    PDD.md                 # problem, invariants, non-scope
    SDD.md                 # components, adapters, state machine
    DECISIONS.md           # architecture/projectization decisions
    FAILURE_MODES.md
    BUILD_VS_REUSE.md
    VALIDATION.md
    CONTINUITY.md
  pins/
    COMPONENTS.lock.json   # exact git SHAs / release ids
    DATASETS.lock.json
  schemas/
    promotion-record.schema.json
    dimension-status.schema.json
    dataset-manifest.schema.json
    replay-recipe.schema.json
    review-binding.schema.json
  src/
    kernel/                # state machine, records, waiver rules
    checkers/              # deterministic checks
    adapters/
      fossil/
      retrieval_benchmarker/
      source_ranker/
      finance_app/
    replay/
  packs/
    finance/
      source_authority_policy.md
      temporal_gold/       # public-dev only in this repo
      numeric_fixtures/
  tests/
    unit/
    contract/
    property/              # promotion state machine
    fault/                 # crash, partial batch, replay, redaction
    mutation/              # critical deterministic checkers
  experiments/
    agent_continuity/      # killable; not imported by kernel
  benchmarks/
    public_dev/            # manifests + allowed labels only
    HIDDEN.md              # process for confirmatory eval; no answers
  ci/
    no_network.yml
```

Hidden confirmatory sets live outside this tree (separate store, separate access control). The repo documents the *process* and identities after a run, not the answers before a run.

### 8.2 Suggested runtime/module boundaries

- `kernel` has no LLM dependency.
- `checkers` have no network in CI.
- adapters may call existing local systems; they do not reimplement them.
- `packs/finance` is the only domain pack in v0.
- `experiments/agent_continuity` cannot be imported by `kernel`.

## 9. First-domain loop (finance)

The financial analysis application is the first *user-visible* promotion loop because it already has SEC/financial evidence, temporal/version semantics, and real research workflows.

v0 finance loop (smallest complete path):

1. Analyst (human or agent) explores filings/notes ungated.
2. A claim is proposed with citations to specific filing versions/spans.
3. Checkers run: artifact identity, citation targeting, as-of vs filing/restatement version, numeric cell match where mechanical.
4. Semantic support is human-reviewed against the exact claim+spans.
5. On accept: P-CLAIM is recorded with dimension statuses and FOSSIL identities.
6. On fail: the claim remains local; exploration continues; no accepted record is written.

Mechanical gold that belongs in *this* loop (public-dev in-repo; confirmatory held out):

- wrong filing version / superseded statement;
- restatement vs original;
- evidence rooted in the wrong document or period;
- citation to a real document but wrong table/row;
- authorization/actor mismatch on ingest vs promote.

Do not start with FinQA/TAT-QA/FinanceBench as the *promotion* metric. Those are retrieval/reasoning datasets. Use Retrieval Benchmarker on them for the retrieval layer only, after the finance promotion path can cite immutable identities.

## 10. Validation strategy (applicable techniques only)

Do not ritualize the full research menu. Apply a technique when the failure it targets is in scope.

### 10.1 Always on for the kernel

- PDD/SDD and the invariants in §6;
- failure-mode register (see `FAILURE_MODES.md`);
- deterministic unit + contract tests for schemas and checkers;
- property / state-machine tests for promotion states: `draft → proposed → checking → accepted | rejected | waived-dimension`; illegal transitions must be unrepresentable or rejected;
- no-network PR CI;
- composition identity tests: a recorded promotion names pins that resolve.

### 10.2 For persistent / FOSSIL boundaries

Packet hypotheses, to be tested not asserted:

- whole-artifact integrity verification;
- review-reference authority (a review cannot bind a different artifact than the one shown);
- orphan storage on failed ingest;
- crash / partial batch;
- caller vs service actor attribution;
- whether role/quality metadata is actually provenance-bound.

Techniques: fault injection, crash/replay/rebuild, redaction/rebuild, mutation testing of the integrity checkers.

These are empirical campaigns. Outcomes may be “hold,” “fix in FOSSIL,” or “adapter-level mitigation.” They are not automatically RPP scope expansion.

### 10.3 For retrieval quality

Owned by Retrieval Benchmarker. Frozen corpora/queries/qrels. Persist rankings and reports as artifacts. Report retrieval metrics *as retrieval metrics*.

Public-dev vs hidden confirmatory splits. Implementers see public-dev only.

Candidate public-dev sources: FinanceBench / FinQA / TAT-QA *for retrieval*, not as a merged “assurance score.” TREC/BEIR only if a later admission asks a retrieval-generalization question.

### 10.4 For citation / grounding / claim support

Not v0 gates. Candidate later experiments, each separate:

- RAGTruth / ALCE — unsupported/grounding/citation behavior;
- FEVER / SciFact / AVeriTeC — support/refute.

Admit only with a question like “does checker X reduce unsupported citations on public-dev without blocking exploration?” Kill if no benefit.

### 10.5 Adversarial review

Distinct from ordinary tests. Goal: can an agent or caller obtain an *accepted* promotion without the required evidence (stamp gaming, wrong-version citation, review bound to different text, index-as-authority, mixed-layer score presented as verified)?

A finding is a candidate issue. It does not automatically add a new subsystem.

### 10.6 Residual risk and kill outcomes

Every admitted expensive mechanism has a pre-declared kill/no-benefit rule. Residual risks after v0 are listed, not papered over.

## 11. External precedents (interop ideas, not imports)

Use as design vocabulary where helpful; do not take on the standard as a dependency.

| Precedent | What to steal as an idea |
|---|---|
| PRISMA | transparent discovery/selection trail for research promotions |
| Cochrane RoB 2 / GRADE | dimension-specific judgments, not one trust score |
| OMG SACM | claim / argument / evidence as distinct objects |
| W3C PROV / RO-Crate | provenance and research packaging concepts |
| in-toto / SLSA | receipts over exact process and artifact identity |
| TREC qrels | retrieval eval methodology |
| SciFact / FEVER / AVeriTeC / RAGTruth / ALCE | later empirical suites, not v0 product |

Mapping: promotion records should be *exportable* toward PROV-like and receipt-like forms later. v0 stores our schema in FOSSIL, not a standards stack.

## 12. Agent / harness continuity experiment (optional, killable)

Interest exists in a small local research-state / HITL layer for cross-session and cross-model continuity.

Rules:

- not a kernel dependency;
- plugin-first, transport-neutral;
- local semantic operations first;
- thin adapters for OpenCode, a second harness, and maybe MCP/ChatGPT only after local tests pass;
- model spend only after deterministic state, restart, idempotency, and review-binding tests are green;
- allowed conclusion: `NO_MEASURABLE_BENEFIT`.

Early experiment (if admitted after kernel v0):

- frozen local research microworlds;
- forced interruption/restart;
- cross-model handoff;
- review bound to exact claim/evidence;
- protocol-induced failure rate vs a no-plugin baseline.

Do not recreate a universal stamp protocol. If the plugin starts gating ordinary actions, it has failed the negative prior.

## 13. Engineering foundations

- Language/runtime: choose in implementation preflight to match adapter cost to FOSSIL and the finance app. Kernel should stay boring and typed. This plan does not freeze a language.
- CI: deterministic, no-network on PRs. Any test that needs corpora uses vendored public-dev fixtures.
- Identity: `COMPONENTS.lock.json` and `DATASETS.lock.json` are the composition source of truth.
- Secrets: none required for kernel tests. Domain API keys stay in the finance app, never in RPP CI.
- Docs: PDD/SDD/decisions are durable; chat is not.
- Resume: a new session reads `HANDOFF.md`, `DECISIONS.md`, lockfiles, and open issues. No hidden conversational memory.

## 14. Phases

Phases are admission gates, not a promise to build everything.

### Phase 0 — Freeze projectization (this bundle)

- agree scope, non-scope, reuse, dimensions, promotion types;
- create program repo skeleton and lockfile schema;
- record pins as “to be filled” until SHAs are collected from the owned repos.

Exit: human accepts this plan (or a marked revision). No feature code required.

### Phase 1 — Pins, adapters, and FOSSIL integrity campaign

- record exact revisions of FOSSIL, Retrieval Benchmarker, Source Ranker, finance app;
- thinnest adapters that can snapshot an artifact and read identity;
- run the FOSSIL integrity hypotheses as tests/campaigns;
- disposition: reuse-as-is / adapter mitigate / upstream issue / do not promote until fixed.

Exit: we can store a promotion record against real FOSSIL identities, or we have a written blocker.

### Phase 2 — Kernel and deterministic checkers

- schemas + state machine + waivers;
- citation, temporal/version, numeric (mechanical), authorization checkers;
- property tests; mutation on checkers; illegal transition tests;
- I-1 through I-11 enforced in tests where mechanically expressible.

Exit: a P-CLAIM can be accepted or rejected with dimension statuses and replay recipe, with no LLM.

### Phase 3 — Finance first loop

- map finance-app user actions to explore vs promote;
- public-dev temporal/wrong-version/restatement fixtures;
- human review-binding UX or API (minimal);
- residual-risk and waiver UX so mixed dimensions cannot look like `verified`.

Exit: one real (or realistic fixture) filing-backed claim can be promoted, replayed, and shown with dimension statuses.

### Phase 4 — Independent retrieval reporting

- pin Retrieval Benchmarker;
- run public-dev finance retrieval configs;
- persist rankings/reports as artifacts;
- P-BENCH for retrieval layer only;
- document that these numbers are not claim correctness.

Exit: a retrieval result can be promoted without being mistaken for a claim result.

### Phase 5 — Source Ranker bound (go/no-go)

- define a simple finance authority baseline;
- compare Source Ranker on a scoped claim-source-fit public-dev set;
- admit as optional input, or record `NO_MEASURABLE_BENEFIT` and leave it out of the gate.

### Phase 6 — Agent continuity experiment (optional)

Only if Phases 2–3 are green and a human admits the experiment. Killable.

### Later candidates (not scheduled)

Claim-verification suite, grounding suite, TREC/BEIR generalization, other domains, standards exporters, graph projections as *projections only*.

## 15. Work decomposition

See `ISSUES.md`. Issues are executable; they do not pre-create a huge backlog of deferred ideas. Deferred ideas live in `CANDIDATES.md` as non-issues until admitted.

## 16. Continuity and provenance of *this* plan

This baseline run is itself a planning artifact. It should be snapshotted with the frozen packet revision `8f4737fc212e6b09f8066d90e178aa8760e619fb` and run id `condition-d-grok-4.6-opencode-20260901-174255`.

A later session must not silently mutate this run after `RUN_MANIFEST.json` status `complete`. Revisions are new run ids or, after benchmark freeze, ordinary project commits in a real RPP repo.

## 17. Success for v0 (small but proper)

v0 is successful if all of the following are true:

1. A claim about a versioned financial artifact can be accepted only with identity, citation, temporal, and (when numeric) numeric checks, plus bound human review for semantic support.
2. Failure of those checks cannot produce an accepted promotion.
3. Exploration still works after failure.
4. The accepted record is replayable from pinned identities.
5. Retrieval numbers, if published, are labeled as retrieval.
6. No universal verified flag exists.
7. FOSSIL integrity hypotheses have been tested and dispositioned.
8. Source Ranker and the agent plugin are either empirically admitted or explicitly out.

v0 can be small. It cannot be vague.
