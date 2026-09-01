# Failure-mode register (v0)

This is a living register *after* a real repo exists. Here it is the v0 seed from the research packet. Items are risks to design against, not confirmed production bugs.

| ID | Failure | Why it matters | Detection | Mitigation in v0 | Residual if unfixed |
|---|---|---|---|---|---|
| F1 | Universal verified flag | Mixed dimensions look like success | Schema/API contract tests; adversarial review | No `verified` field; dimension enum only | Users still verbally say “verified” — docs discipline |
| F2 | Agent stamp gaming | Prior stamp protocol was gamed | Adversarial tests: accept without evidence | No stamps; evidence-closed transitions only | Social pressure to rubber-stamp reviews |
| F3 | Gate blocks exploration | Useful work stops; people bypass | Tests that draft writes work after reject | I-1, separate explore vs accept APIs | Product UX may still nag |
| F4 | Silent bypass of accept | Failed gate still writes accepted | State machine; FOSSIL append checks | Accept only after required dimensions | Operator with raw FOSSIL write — operational control |
| F5 | Substrate down, fake accept | Outage forges success | I-11 tests | Accept unavailable; explore remains | Users confuse “couldn’t record” with “true” |
| F6 | Index treated as evidence | Rebuild/redaction desync | Citation checker requires immutable IDs | D5; recipe rebuilds projections | Apps may still deep-link index rows in UI |
| F7 | Wrong filing version accepted | Temporal error presented as fact | Temporal gold fixtures | E3-2, E4-3 | Incomplete lineage in source data |
| F8 | Restatement ignored | Superseded numbers survive | Same | Same | Policy may waive with named residual |
| F9 | Citation to wrong span/cell | Correct doc, wrong support | Quote/offset and numeric cell tests | E3-1, E3-3 | Unstructured prose without spans |
| F10 | Review bound to different text | Rubber-stamp | Review hash of claim+spans | E1-4, E4-5 | Off-platform verbal approval |
| F11 | Actor spoof / unbound roles | Can’t tell who promoted | Actor attribution campaign | E1-7, E3-4 | Shared service accounts |
| F12 | Partial ingest looks complete | Crash window | Fault injection | E1-5, E1-6 | Depends on FOSSIL disposition |
| F13 | Layer-score collapse | Retrieval sold as claim truth | P-BENCH schema layer field | D7, E5-3 | Slide decks still collapse — process |
| F14 | Hidden eval leaked to agents | Adaptive contamination | Repo grep; access control | D10; no hidden labels in tree | Accidental paste into chat |
| F15 | Domain transfer assumption | Finance accept used as legal/medical | Pack field required on promotion | I-8; finance pack only | People copy records across domains |
| F16 | Source Ranker as silent gate | Unproven mechanism blocks or passes wrongly | E6 must close before gate use | Default out of accept path | Ranker scores shown as decoration only |
| F17 | Plugin becomes stamp layer | Repeat of negative prior | Experiment kill rule | D9; cannot import into kernel | Later adapters add gates — review D9 |
| F18 | Scope explosion from red team | Every finding becomes a subsystem | Admission rule D12 | Candidates list, not issues | Tracker hygiene |
| F19 | Stochastic check where deterministic exists | Flaky identity/numeric/temporal | Code review + tests | I-5 | Ambiguous prose claims |
| F20 | Replay impossible | Later session cannot rebuild | Recipe tests | E2-4, E7-2 | Non-pinned upstream data disappearance |
| F21 | Self-attestation closure | Agent says “done” without evidence | Issue/closure rules | I-2, I-10 | Human still has to refuse |

Adversarial review (distinct from unit tests) should at least attempt F2, F4, F6, F10, F13, F14.
