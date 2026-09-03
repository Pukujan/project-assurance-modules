from __future__ import annotations

import copy

import pytest
from jsonschema import ValidationError

from scripts.pam_core import ROOT, load_json
from scripts.pam_profiles import (
    compose_as_json,
    load_profiles,
    select_profiles,
    validate_manifest_profile_refs,
    validate_profile,
)


def example_manifest() -> dict[str, object]:
    return load_json(ROOT / "examples" / "PROJECT_ASSURANCE.example.json")


def test_shipped_profiles_validate_and_resolve_modules() -> None:
    profiles = load_profiles()
    assert set(profiles) == {
        ("benchmark.empirical-work", "0.1.0"),
        ("continuity.material-work", "0.1.0"),
        ("projectization.software", "0.1.0"),
        ("projectization.software", "0.2.0"),
        ("provenance.material-decisions", "0.1.0"),
    }


def test_automatic_profile_selection_prefers_latest_version() -> None:
    facts: dict[str, object] = {"software": True, "projectization": True}
    software = [
        selection
        for selection in select_profiles(facts)
        if selection.profile_id == "projectization.software"
    ]
    assert len(software) == 1
    assert software[0].version == "0.2.0"
    assert software[0].disposition == "selected"


def test_unknown_profile_field_fails_closed() -> None:
    profile = copy.deepcopy(load_profiles()[("continuity.material-work", "0.1.0")])
    profile["verified"] = True
    with pytest.raises(ValidationError):
        validate_profile(profile)


def test_profiles_select_from_declared_project_facts() -> None:
    facts: dict[str, object] = {
        "software": True,
        "projectization": True,
        "nontrivial": True,
        "reusable_systems_possible": False,
        "horizontal_scope_risk": False,
        "multi_session": True,
        "agent_assisted": False,
        "empirical_quality_claims": False,
        "benchmark_or_dataset_use": False,
        "hidden_confirmatory_evaluation": False,
        "consequential_decisions": False,
        "durable_provenance_and_decision_lineage": False,
    }
    selected = {item.profile_id: item.disposition for item in select_profiles(facts)}
    assert selected == {
        "benchmark.empirical-work": "not_selected",
        "continuity.material-work": "selected",
        "projectization.software": "selected",
        "provenance.material-decisions": "not_selected",
    }


def test_missing_selector_facts_remain_conditional() -> None:
    facts: dict[str, object] = {
        "software": True,
        "projectization": True,
        "nontrivial": True,
    }
    selected = {item.profile_id: item.disposition for item in select_profiles(facts)}
    assert selected["benchmark.empirical-work"] == "conditional"
    assert selected["continuity.material-work"] == "conditional"
    assert selected["projectization.software"] == "selected"
    assert selected["provenance.material-decisions"] == "conditional"


def test_declared_single_session_work_does_not_select_continuity_profile() -> None:
    facts: dict[str, object] = {
        "software": True,
        "projectization": True,
        "nontrivial": True,
        "multi_session": False,
        "agent_assisted": False,
        "empirical_quality_claims": False,
        "benchmark_or_dataset_use": False,
        "hidden_confirmatory_evaluation": False,
        "consequential_decisions": False,
        "durable_provenance_and_decision_lineage": False,
    }
    composed = compose_as_json(facts)
    profiles = composed["profiles"]
    modules = composed["modules"]
    assert isinstance(profiles, list)
    assert isinstance(modules, list)
    profile_states = {
        item["profile_id"]: item["disposition"] for item in profiles if isinstance(item, dict)
    }
    module_ids = {item["module_id"] for item in modules if isinstance(item, dict)}
    assert profile_states["continuity.material-work"] == "not_selected"
    assert "continuity.structured-handoff" not in module_ids
    assert "benchmark.integrity" not in module_ids
    assert "provenance.decision-lineage" not in module_ids


def test_profile_selection_does_not_make_every_module_required() -> None:
    facts: dict[str, object] = {
        "software": True,
        "projectization": True,
        "nontrivial": True,
        "reusable_systems_possible": False,
        "horizontal_scope_risk": False,
        "multi_session": True,
        "agent_assisted": False,
        "empirical_quality_claims": False,
        "benchmark_or_dataset_use": False,
        "hidden_confirmatory_evaluation": False,
        "consequential_decisions": False,
        "durable_provenance_and_decision_lineage": False,
    }
    composed = compose_as_json(facts)
    modules = composed["modules"]
    assert isinstance(modules, list)
    dispositions = {
        item["module_id"]: item["disposition"] for item in modules if isinstance(item, dict)
    }
    assert dispositions == {
        "continuity.structured-handoff": "required",
        "engineering.swe-ci-foundation": "required",
        "planning.foundation": "required",
        "projectization.build-vs-reuse": "recommended",
        "projectization.scope-boundary": "recommended",
    }


def test_empirical_and_provenance_profiles_route_only_when_declared() -> None:
    facts: dict[str, object] = {
        "software": False,
        "projectization": False,
        "nontrivial": True,
        "multi_session": False,
        "agent_assisted": False,
        "empirical_quality_claims": True,
        "benchmark_or_dataset_use": True,
        "hidden_confirmatory_evaluation": False,
        "consequential_decisions": True,
        "durable_provenance_and_decision_lineage": True,
    }
    composed = compose_as_json(facts)
    modules = composed["modules"]
    assert isinstance(modules, list)
    dispositions = {
        item["module_id"]: item["disposition"] for item in modules if isinstance(item, dict)
    }
    assert dispositions == {
        "benchmark.integrity": "required",
        "provenance.decision-lineage": "required",
    }


def test_unknown_manifest_profile_fails() -> None:
    manifest = copy.deepcopy(example_manifest())
    manifest["profiles"] = [{"profile_id": "imaginary.profile", "version": "0.1.0"}]
    with pytest.raises(ValueError, match="unknown profile"):
        validate_manifest_profile_refs(manifest)


def test_historical_software_profile_v01_still_resolves() -> None:
    manifest: dict[str, object] = {
        "project_facts": {"software": True, "projectization": True},
        "profiles": [{"profile_id": "projectization.software", "version": "0.1.0"}],
        "modules": [
            {
                "module_id": "projectization.build-vs-reuse",
                "version": "0.1.0",
            }
        ],
    }
    validate_manifest_profile_refs(manifest)


def test_manifest_profile_contradicted_by_facts_fails() -> None:
    manifest = copy.deepcopy(example_manifest())
    facts = manifest["project_facts"]
    assert isinstance(facts, dict)
    facts["multi_session"] = False
    facts["agent_assisted"] = False
    manifest["profiles"] = [{"profile_id": "continuity.material-work", "version": "0.1.0"}]
    with pytest.raises(ValueError, match="contradicted"):
        validate_manifest_profile_refs(manifest)


def test_manifest_module_must_be_covered_by_selected_profiles() -> None:
    manifest = copy.deepcopy(example_manifest())
    manifest["profiles"] = [{"profile_id": "continuity.material-work", "version": "0.1.0"}]
    modules = manifest["modules"]
    assert isinstance(modules, list)
    module = modules[0]
    assert isinstance(module, dict)
    module["module_id"] = "projectization.scope-boundary"
    with pytest.raises(ValueError, match="not covered"):
        validate_manifest_profile_refs(manifest)
