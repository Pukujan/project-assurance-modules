# Validation applicability

The packet lists many techniques. v0 uses a technique only when the failure it targets is in scope. This table is the applicability map.

| Technique | Applicable in v0? | Where | Not applicable when |
|---|---|---|---|
| PDD / SDD / invariants | yes | `PLAN.md`, future `docs/` | — |
| Failure-mode register | yes | `FAILURE_MODES.md` | Treating the list as a compliance stamp |
| Deterministic unit/contract tests | yes | schemas, checkers, adapters | — |
| Property / state-machine tests | yes | promotion states, append-only accept | Purely functional formatters with no state |
| Metamorphic relations | limited | retrieval: rank-order stability under benign query paraphrase *if* Benchmarker already supports it; numeric: unit conversion identities | Semantic claim text (human-reviewed) |
| Mutation testing | yes, targeted | deterministic checkers (E3-5) | LLM prompts, UI copy |
| Fault injection / crash / replay / rebuild | yes | FOSSIL boundary campaigns E1-3..E1-7 | Stateless checkers |
| Adversarial review | yes, distinct | F2/F4/F6/F10/F13/F14 | Replacing unit tests |
| Benchmark-first eval | yes, layered | retrieval via Benchmarker; not for identity checks | Identity/citation/temporal (those are tests, not IR benchmarks) |
| Public-dev vs hidden confirmatory | yes | datasets, finance gold | Kernel unit tests (no hidden needed) |
| Dataset manifests / version identity | yes | lockfiles, P-BENCH | — |
| Composition tests / layer ablations | yes | E7-2; E6 ablation for Source Ranker | Ablating mechanisms not in the composition |
| Residual risk / kill outcomes | yes | every P3+ candidate | Using kill language as decoration while keeping the gate |

## Layered evaluation (do not merge scores)

```text
substrate integrity  --> tests + FOSSIL campaigns
citation / temporal / numeric --> deterministic checkers + mutation
retrieval quality --> Retrieval Benchmarker metrics (P-BENCH layer=retrieval)
source suitability --> policy; Source Ranker only if E6 admits
semantic support --> human review in v0; later C1/C2 if admitted
```

No dashboard number may average these.

## Benchmark/data placement

| Source | Layer | v0 use |
|---|---|---|
| Mechanical SEC temporal/version/restatement/wrong-version | temporal + citation | public-dev fixtures in finance pack |
| FOSSIL corruption/auth/retry/recovery/redaction/rebuild | substrate | Phase 1 campaigns |
| FinanceBench, FinQA, TAT-QA | retrieval (and maybe later reasoning, not v0 claim gate) | via Retrieval Benchmarker after E5 |
| TREC / BEIR | retrieval generalization | candidate C6 |
| FEVER, SciFact, AVeriTeC | claim/evidence support | candidate C1 |
| RAGTruth, ALCE | unsupported/grounding | candidate C2 |

## Hidden material rule

Implementer-facing trees contain only public-dev. Confirmatory answers are not in this planning bundle and must not be added to a later RPP repo that coding agents can read.
