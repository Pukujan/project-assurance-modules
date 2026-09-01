# PAM gaps

1. **The frozen v0 has only three executable modules for a much broader routing vocabulary.** The PDD/architecture/routing documents identify system design, SWE/CI, validation, benchmark/holdout, provenance, multi-repository orchestration, and release-evidence concerns, but this revision provides no stable module definitions/requirement IDs for them. The candidate therefore had to plan those obligations project-specifically rather than route/track them in `PROJECT_ASSURANCE.json`.

2. **`continuity.structured-handoff` requires a pinned machine-readable handoff schema, but the frozen PAM inputs do not supply a generic handoff-state schema.** This makes the required handoff shape clear semantically but leaves deterministic schema selection/validation to the adopting project.

3. **Profiles are described conceptually, but no profile definitions are available in the frozen input.** The manifest therefore uses an empty `profiles` list and routes the three available modules directly from project facts.

These gaps were not patched during the run.
