# Blind evaluator candidate bundle v1

This branch contains opaque candidate evidence bundles for a **model/vendor/harness-blind** evaluation of the frozen Research Assurance retrospective benchmark.

The purpose of this pass is to test whether evaluator knowledge of the planner's vendor/model/harness changes planning-quality judgments. Experimental treatment may be inferable from substantive methodology artifacts; treatment blinding is not the target of this pass.

Evaluator rules:

- Read only the candidate directories under this path plus the already-permitted `Pukujan/research-assurance` reference project.
- Do not enumerate repository branches, commits, pull requests, issues, prior evaluator outputs, or candidate run directories elsewhere in this repository.
- Do not inspect Git history for this branch or infer candidate author identity from repository metadata.
- Candidate model/vendor/harness identities and the candidate-to-run mapping are intentionally withheld until all scores are frozen.
- In each candidate directory, read `EVIDENCE.md` and every `DOC-*.txt` file. These are copied from frozen substantive planning artifacts under neutral filenames.
- Run manifests, access attestations, explicit methodology-gap notes, branch names, and explicit model/provider/harness metadata are excluded.
- Score all candidates using the pre-frozen 12-dimension / 100-point rubric. Semantic equivalence matters; filenames and historical Research Assurance choices do not.
- Freeze `BLIND_EVALUATION.json` and `BLIND_EVALUATION.md` before requesting or receiving any reveal mapping.

Opaque candidates in this bundle:

- `candidate-alpha`
- `candidate-beta`
- `candidate-gamma`
- `candidate-delta`
- `candidate-epsilon`

No reveal mapping is stored on this branch.