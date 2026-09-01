# Executable work decomposition

Run: `condition-d-grok-4.6-opencode-20260901-174255`
These are proposed issues for a future RPP program repository. They are not GitHub issues yet. Do not bulk-open them before a human accepts Phase 0.

Priority: P0 must exist before any accepted promotion is claimed. P1 is the finance loop. P2 is independent retrieval reporting. P3 is go/no-go research. Deferred items are *not* issues.

---

## Epic E0 — Projectization freeze

### E0-1 Accept or revise this plan
- Priority: P0
- Goal: Human owner accepts `PLAN.md` invariants, non-scope, build-vs-reuse, and phases, or records a dated revision.
- Evidence: signed/recorded decision in `docs/DECISIONS.md` (future repo) naming this run or a successor plan SHA.
- Not done: silent drift in chat.

### E0-2 Create program repository skeleton
- Priority: P0
- Goal: Empty RPP repo with the layout in `PLAN.md` §8.1, license, README pointing at PDD/SDD placeholders.
- Evidence: repository exists; CI placeholder is no-network and green on empty tests.
- Non-scope: copying FOSSIL or apps into the repo.

### E0-3 Lockfile schemas
- Priority: P0
- Goal: `COMPONENTS.lock.json` and `DATASETS.lock.json` schemas with fields for name, uri, git_sha or content_hash, role, admitted_use.
- Evidence: schema tests reject missing SHA/hash.
- Pins may be `pending` until E1.

---

## Epic E1 — Pin existing systems and test FOSSIL boundaries

### E1-1 Inventory and pin owned revisions
- Priority: P0
- Goal: Record exact revisions of FOSSIL Core, Retrieval Benchmarker, Source Ranker, financial analysis application as they exist at pin time.
- Evidence: lockfile entries with SHAs; short note of what each is admitted to do.
- Not done: “latest” or unpinned submodule.

### E1-2 FOSSIL adapter (read/write identity only)
- Priority: P0
- Goal: Thinnest adapter: put bytes, get immutable identity, append a promotion-record artifact, read it back.
- Evidence: contract tests against the pinned FOSSIL revision.
- Non-scope: reimplementing lineage, redaction, or history.

### E1-3 FOSSIL integrity campaign — whole-artifact verification
- Priority: P0
- Goal: Empirically check that stored artifacts can be verified as whole artifacts (not partial/truncated/wrong hash accepted).
- Evidence: tests that tamper/truncate and expect reject; written disposition.
- Status of finding: hypothesis, not a confirmed bug.

### E1-4 FOSSIL integrity campaign — review-reference authority
- Priority: P0
- Goal: A review record cannot bind to a different artifact/span than the one presented to the reviewer.
- Evidence: negative tests; disposition.

### E1-5 FOSSIL integrity campaign — failed ingest orphans
- Priority: P0
- Goal: Failed ingest does not leave reachable “accepted” artifacts; orphan/storage behavior is documented and tested.
- Evidence: ingest-failure tests; disposition.

### E1-6 FOSSIL integrity campaign — crash / partial batch
- Priority: P0
- Goal: Crash or partial batch cannot yield a promotion that looks accepted without durable complete records.
- Evidence: fault-injection/replay tests; disposition.

### E1-7 FOSSIL integrity campaign — actor attribution
- Priority: P0
- Goal: Caller vs service actor cannot be confused; role/quality metadata is provenance-bound or explicitly documented as not bound.
- Evidence: tests attempting actor spoof / unbound metadata; disposition.

### E1-8 Upstream vs adapter vs blocker
- Priority: P0
- Goal: Each campaign result is `reuse`, `mitigate-in-adapter`, `upstream-issue`, or `promotion-blocked`.
- Evidence: table in `docs/DECISIONS.md`.
- Rule: do not expand RPP into a FOSSIL rewrite.

---

## Epic E2 — Promotion kernel

### E2-1 Promotion record schema
- Priority: P0
- Goal: JSON schema for promotion records: type, input identities, output identity, dimension statuses, checker runs, review binding, waivers, replay recipe pointer, actor, time.
- Evidence: positive/negative fixtures; no `verified` field.
- Non-scope: domain-specific claim NLP fields beyond opaque claim text + citation list.

### E2-2 Dimension status model
- Priority: P0
- Goal: Enum per dimension: `pass | fail | waived | not_applicable | pending`. Waiver requires reason + author. `not_applicable` requires a rule, not silence.
- Evidence: tests that mixed dimensions cannot serialize as overall verified.

### E2-3 State machine
- Priority: P0
- Goal: Legal states `draft | proposed | checking | accepted | rejected`. Property tests for illegal transitions. Accepted is append-only; correction is a new promotion that supersedes by identity, not an edit in place.
- Evidence: state-machine/property tests.

### E2-4 Replay recipe
- Priority: P0
- Goal: Recipe names component pins, dataset pins, checker versions, and projection rebuild steps. Indexes are listed as derived.
- Evidence: test rebuilds a projection from recipe on public-dev fixtures.

### E2-5 Exploration continues on failure
- Priority: P0
- Goal: API/library allows write of drafts and rejected proposals when accept is denied; accept endpoint is the only gated path.
- Evidence: tests that reject does not raise a hard work-stop for draft writes; I-11: if substrate is down, accept is unavailable and does not fake success.

---

## Epic E3 — Deterministic checkers

### E3-1 Citation targeting checker
- Priority: P0
- Goal: Citation must resolve to the named artifact identity and, where spans exist, to offsets/quotes that match bytes.
- Evidence: unit tests; mutation tests of the matcher.

### E3-2 Temporal / version checker (finance-usable, kernel-generic)
- Priority: P0
- Goal: Given as-of time and version lineage, reject superseded/wrong-version citations when policy says the claim is as-of dated.
- Evidence: public-dev restatement/wrong-version fixtures.

### E3-3 Numeric checker (mechanical only)
- Priority: P0
- Goal: Where a claim number is bound to a table/cell/span, compare normalized numeric values. No LLM.
- Evidence: fixtures for correct cell, wrong cell, rounding policy documented.
- Non-scope: general financial reasoning.

### E3-4 Authorization checker
- Priority: P0
- Goal: Ingest actor, checker actor, reviewer, and promoter are recorded; policy can require distinct reviewer for P-CLAIM accept.
- Evidence: tests for missing reviewer, self-review if policy forbids, actor mismatch.

### E3-5 Mutation campaign on checkers
- Priority: P1
- Goal: Mutation testing on E3-1..E3-4; survivors are either killed by new tests or accepted as residual risk.
- Evidence: mutation report artifact (public summary, no need for hidden eval).

---

## Epic E4 — Finance first loop

### E4-1 Map application actions to explore vs promote
- Priority: P1
- Depends: E2, finance app pin
- Goal: Written mapping of current financial-app workflows to ungated exploration vs P-CLAIM / P-KNOW.
- Evidence: `packs/finance/action_map.md` reviewed by owner.
- Non-scope: rewriting the whole app.

### E4-2 Finance source-authority policy
- Priority: P1
- Goal: Which source types may support which claim types (e.g., 10-K vs press vs secondary). Explicit “not authority” list.
- Evidence: policy doc + tests that policy violations become `source_suitability=fail` or block accept per policy.

### E4-3 Public-dev temporal/version gold
- Priority: P1
- Goal: Mechanically generated or curated public-dev cases: restatement, wrong version, wrong period, wrong evidence root.
- Evidence: fixtures in `packs/finance/temporal_gold/` with manifest hashes.
- Forbidden: putting hidden confirmatory answers in this tree.

### E4-4 Wire P-CLAIM into one application path
- Priority: P1
- Goal: One path: propose claim → checkers → human review binding → accept/reject record in FOSSIL.
- Evidence: integration test on public-dev fixtures; screenshot or API transcript optional.

### E4-5 Review binding UI/API
- Priority: P1
- Goal: Reviewer sees exact claim text and cited spans; recorded review hashes those bytes.
- Evidence: negative test that altered claim text invalidates the review.

### E4-6 Mixed-dimension presentation
- Priority: P1
- Goal: UI/API shows per-dimension status. Cannot display a green “verified” badge.
- Evidence: contract test on serialized view model.

---

## Epic E5 — Retrieval layer reporting (independent)

### E5-1 Pin Retrieval Benchmarker and finance public-dev sets
- Priority: P2
- Goal: Lockfile entries for Benchmarker SHA and dataset manifests (FinanceBench / FinQA / TAT-QA as *retrieval* sets if/as available in the pinned tool).
- Evidence: lockfile; split labeled `public-dev`.

### E5-2 Persist rankings/reports as artifacts
- Priority: P2
- Goal: A benchmarker run writes immutable ranking + report identities via FOSSIL adapter.
- Evidence: rerun with same pins reproduces report identity or a documented non-bit-identical-but-metric-identical policy.

### E5-3 P-BENCH for retrieval only
- Priority: P2
- Goal: Promotion type P-BENCH with `layer=retrieval`. Schema rejects a payload that also claims claim-correctness.
- Evidence: negative fixture.

### E5-4 Hidden confirmatory process
- Priority: P2
- Goal: Document how a later confirmatory retrieval run is executed without exposing qrels/answers to implementers. `benchmarks/HIDDEN.md` is process-only.
- Evidence: process doc; no hidden labels in repo.

---

## Epic E6 — Source Ranker go/no-go

### E6-1 Simple authority baseline
- Priority: P3
- Goal: Deterministic finance authority+recency+doc-type baseline.
- Evidence: tests; documented rules.

### E6-2 Scoped comparison
- Priority: P3
- Goal: Compare Source Ranker vs baseline on a public-dev claim-source-fit set. Pre-declare metric and `NO_MEASURABLE_BENEFIT` threshold.
- Evidence: report artifact; decision record: admit as optional input **or** exclude from gates.
- Rule: no gate inclusion without this issue closed.

---

## Epic E7 — Engineering / CI

### E7-1 No-network PR CI
- Priority: P0
- Goal: Format, typecheck (if applicable), schema validate, unit/contract tests, no egress.
- Evidence: CI log.

### E7-2 Composition tests
- Priority: P1
- Goal: A sample accepted promotion resolves all lockfile pins and recipe steps on public-dev data.
- Evidence: CI job `composition`.

### E7-3 Resume artifacts
- Priority: P0
- Goal: README + CONTINUITY.md tell a fresh session exactly what to read. No dependence on chat memory.
- Evidence: the files exist and are referenced from README.

---

## Epic E8 — Optional agent continuity experiment

Do not open as active implementation until a human admits it after E2–E4.

### E8-1 Deterministic microworld harness
- Priority: deferred-until-admitted
- Goal: Frozen local research state, interrupt/restart, idempotent writes, review binding — no model spend.
- Kill: if this is not green, do not buy tokens.

### E8-2 Cross-model handoff protocol
- Priority: deferred-until-admitted
- Goal: Measure protocol-induced failure vs no-plugin baseline. Allowed outcome `NO_MEASURABLE_BENEFIT`.
- Non-scope: MCP/ChatGPT adapters until E8-1 green; no universal stamps.

---

## Explicitly not issues yet

These stay in `CANDIDATES.md` until admitted:

- Graph retrieval / GraphRAG;
- ontology / meta-systems;
- legal/medical packs;
- FEVER / SciFact / AVeriTeC as gates;
- RAGTruth / ALCE as gates;
- TREC/BEIR generalization campaign;
- full PROV / RO-Crate / SLSA / in-toto exporters;
- MCP or ChatGPT adapters;
- any new mechanism invented by a red-team finding without disposition.

If a future session files them as issues without an admission record, that is scope error.
