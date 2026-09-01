# Blind evaluator candidate bundle v1

This branch contains opaque candidate evidence bundles for a vendor/condition-blind evaluation of the frozen Research Assurance retrospective benchmark.

Evaluator rules:

- Read only the candidate directories under this path plus the already-permitted `Pukujan/research-assurance` reference project.
- Do not enumerate repository branches, commits, pull requests, issues, prior evaluator outputs, or candidate run directories elsewhere in this repository.
- Do not inspect Git history for this branch or infer candidate identity from repository metadata.
- Candidate identities, model vendors, harnesses, and experimental conditions are intentionally withheld until all scores are frozen.
- Each candidate is represented by one normalized `EVIDENCE.md` file containing substantive planning output only. Run manifests, access attestations, explicit methodology-gap notes, and identity-bearing metadata are excluded.
- Score all candidates using the pre-frozen 12-dimension / 100-point rubric. Semantic equivalence matters; filenames and historical Research Assurance choices do not.
- Freeze `BLIND_EVALUATION.json` and `BLIND_EVALUATION.md` before requesting or receiving any reveal mapping.

Opaque candidates in this bundle:

- `candidate-alpha`
- `candidate-beta`
- `candidate-gamma`
- `candidate-delta`
- `candidate-epsilon`

No reveal mapping is stored on this branch.