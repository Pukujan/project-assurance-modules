# Blind evaluator handoff

Start here in a fresh evaluator session.

1. Read `README.md` in this directory.
2. Read `SCORING_RUBRIC.md`.
3. For each opaque candidate, read its `EVIDENCE.md` and every `DOC-*.txt` file in that candidate directory.
4. You may inspect the finished `Pukujan/research-assurance` reference project because candidate outputs were frozen before this blind bundle was prepared.
5. Do not inspect any other branch/path in `Pukujan/project-assurance-modules`, prior evaluator results, candidate manifests/attestations, or Git metadata that could reveal model/vendor/harness identity or candidate-to-run mapping.
6. Score semantic planning obligations, not textual similarity to the reference. A materially defensible alternative may receive full credit; flag potential improvements to the reference.
7. Use exactly the frozen rubric in `SCORING_RUBRIC.md`.
8. Write and freeze `BLIND_EVALUATION.json` and `BLIND_EVALUATION.md` with `evaluation_status: frozen_before_identity_reveal`.
9. Stop after freezing. Do not request identities. A later turn will provide the reveal mapping for vendor-bias analysis.

The target of this blind pass is model/vendor/harness awareness. Experimental treatment may be inferable from substantive methodology artifacts; do not attempt to infer the author from that fact.

A valid blind evaluation must not alter scores after the identity reveal.