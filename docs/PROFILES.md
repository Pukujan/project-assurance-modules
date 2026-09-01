# Routing profiles

Profiles are versioned, explainable candidate-module sets selected from declared project facts. They reduce arbitrary manual module enumeration without converting every module into a requirement.

## Identity

Profiles validate against `schemas/profile.schema.json` with schema identity `pam-profile/0.1.0`.

Stable profile identity is the PAM repository revision plus `profile_id` and profile `version`, matching the repository's broader methodology identity model.

## Shipped profiles

The bounded profiles are:

- `projectization.software@0.1.0` — surfaces build-vs-reuse, scope-boundary, planning-foundation, and SWE/CI modules when software work is explicitly entering projectization;
- `continuity.material-work@0.1.0` — surfaces structured handoff when material work spans sessions or uses agent-assisted execution;
- `benchmark.empirical-work@0.1.0` — surfaces benchmark integrity for empirical claims, dataset/benchmark use, or hidden/confirmatory evaluation;
- `provenance.material-decisions@0.1.0` — surfaces decision-lineage methodology for consequential or explicitly replay-worthy decisions.

These profiles contain only the frozen v0 modules and the small repeated v0.2 extraction cluster justified by the retrospective handoff. They do not mass-extract the roadmap.

## Selection states

Profile selection has three outcomes:

- `selected` — declared facts satisfy the selector;
- `conditional` — one or more selector facts are undeclared and no declared fact disproves applicability;
- `not_selected` — declared facts contradict the selector.

Missing facts therefore do not silently remove a profile.

A selector contains deterministic `all_of` and `any_of` equality conditions over declared project facts. At least one condition must exist.

## Composition

`python -m scripts.pam_compose <facts.json>` returns both profile decisions and the routed candidate modules covered by selected or conditional profiles.

Profiles choose the candidate module set. The module router still decides whether each candidate module is `required`, `recommended`, `conditional`, or `not_applicable` from the project facts. Selecting a profile therefore does not make all of its modules required.

## Manifest validation

For backward compatibility, a v0-style manifest may still contain an empty `profiles` list.

Once a manifest cites profiles:

1. each profile identity must resolve at the pinned PAM revision;
2. declared project facts must not contradict the selected profile;
3. each selected module must be covered by at least one cited profile.

This is a bounded migration path: adopters can move from manual module enumeration to profile-backed composition without invalidating frozen v0 manifests.
