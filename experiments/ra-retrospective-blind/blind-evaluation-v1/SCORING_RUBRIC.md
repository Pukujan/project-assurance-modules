# Frozen scoring rubric

Use exactly these dimensions and weights. Do not change them after inspecting candidates.

| Dimension | Weight |
| --- | ---: |
| Problem/product scope and explicit non-goals | 8 |
| Build-vs-reuse / existing-system decision discipline | 8 |
| System/component ownership boundaries | 12 |
| Milestone/phase sequencing and dependency logic | 10 |
| Executable issue decomposition and closure evidence | 10 |
| SWE/CI foundation | 8 |
| Invariants, failure modes, and fail-closed negative validation | 12 |
| Benchmark/dataset/holdout methodology | 10 |
| Scope control and mechanism entry/kill discipline | 7 |
| Provenance/FOSSIL decision-lineage boundary | 5 |
| Multi-repo orchestration and exact revision/evidence identity | 5 |
| Structured handoff/continuity | 5 |
| **Total** | **100** |

For every candidate also record non-scoring diagnostics:

- material omissions;
- unnecessary complexity;
- contradictory requirements;
- scope creep;
- unjustified bespoke build versus reuse;
- continuity/handoff weaknesses;
- defensible divergences from the reference;
- reference challenges where the candidate may improve on the reference.

Classify each material difference from the reference as one of:

- `MATERIAL_OMISSION`
- `MATERIAL_ERROR`
- `EQUIVALENT_ALTERNATIVE`
- `POTENTIAL_IMPROVEMENT`
- `INCIDENTAL_DIFFERENCE`

The reference is evidence, not an infallible gold architecture.