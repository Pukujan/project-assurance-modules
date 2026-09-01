from __future__ import annotations

import copy

import pytest
from jsonschema import ValidationError

from scripts.pam_core import ROOT, load_json, load_modules, route_as_json, validate_manifest

NEW_BOUNDED_MODULES = {
    ("benchmark.integrity", "0.1.0"),
    ("engineering.swe-ci-foundation", "0.1.0"),
    ("planning.foundation", "0.1.0"),
    ("provenance.decision-lineage", "0.1.0"),
}


def example_manifest() -> dict[str, object]:
    return load_json(ROOT / "examples" / "PROJECT_ASSURANCE.example.json")


def test_all_shipped_modules_validate_and_resolve() -> None:
    modules = load_modules()
    assert set(modules) == {
        ("benchmark.integrity", "0.1.0"),
        ("continuity.structured-handoff", "0.1.0"),
        ("engineering.swe-ci-foundation", "0.1.0"),
        ("planning.foundation", "0.1.0"),
        ("projectization.build-vs-reuse", "0.1.0"),
        ("projectization.scope-boundary", "0.1.0"),
        ("provenance.decision-lineage", "0.1.0"),
    }


def test_new_bounded_modules_record_extraction_metadata() -> None:
    modules = load_modules()
    for key in NEW_BOUNDED_MODULES:
        module = modules[key]
        assert module["schema_version"] == "pam-module/0.2.0"
        assert module["motivation"]
        assert isinstance(module["conflicts"], list)
        assert module["compatibility"]["impact"] == "additive"


def test_example_manifest_validates() -> None:
    validate_manifest(example_manifest())


def test_unknown_manifest_field_fails_closed() -> None:
    manifest = copy.deepcopy(example_manifest())
    manifest["verified"] = True
    with pytest.raises(ValidationError):
        validate_manifest(manifest)


def test_unknown_module_fails() -> None:
    manifest = copy.deepcopy(example_manifest())
    modules = manifest["modules"]
    assert isinstance(modules, list)
    selection = modules[0]
    assert isinstance(selection, dict)
    selection["module_id"] = "planning.imaginary"
    with pytest.raises(ValueError, match="unknown module"):
        validate_manifest(manifest)


def test_missing_module_requirement_fails() -> None:
    manifest = copy.deepcopy(example_manifest())
    modules = manifest["modules"]
    assert isinstance(modules, list)
    selection = modules[0]
    assert isinstance(selection, dict)
    requirements = selection["requirements"]
    assert isinstance(requirements, list)
    requirements.pop()
    with pytest.raises(ValueError, match="requirement mismatch"):
        validate_manifest(manifest)


def test_satisfied_requirement_rejects_disallowed_evidence_kind() -> None:
    manifest = copy.deepcopy(example_manifest())
    modules = manifest["modules"]
    assert isinstance(modules, list)
    selection = modules[0]
    assert isinstance(selection, dict)
    requirements = selection["requirements"]
    assert isinstance(requirements, list)
    first = requirements[0]
    assert isinstance(first, dict)
    first["state"] = "satisfied"
    first["evidence"] = [
        {"kind": "benchmark", "locator": "bench.json", "note": "wrong kind for HANDOFF-001"}
    ]
    with pytest.raises(ValueError, match="not allowed"):
        validate_manifest(manifest)


def test_router_requires_extracted_modules_for_nontrivial_agent_projectization() -> None:
    facts: dict[str, object] = {
        "software": True,
        "nontrivial": True,
        "projectization": True,
        "reusable_systems_possible": True,
        "multi_session": True,
        "agent_assisted": True,
        "horizontal_scope_risk": True,
        "empirical_quality_claims": False,
        "benchmark_or_dataset_use": False,
        "hidden_confirmatory_evaluation": False,
        "consequential_decisions": False,
        "durable_provenance_and_decision_lineage": False,
    }
    routed = {item["module_id"]: item["disposition"] for item in route_as_json(facts)}
    assert routed == {
        "benchmark.integrity": "not_applicable",
        "continuity.structured-handoff": "required",
        "engineering.swe-ci-foundation": "required",
        "planning.foundation": "required",
        "projectization.build-vs-reuse": "required",
        "projectization.scope-boundary": "required",
        "provenance.decision-lineage": "not_applicable",
    }


def test_bounded_module_positive_and_negative_fixtures() -> None:
    fixture = load_json(ROOT / "fixtures" / "modules" / "bounded-repeated-extractions.json")
    assert set(fixture) == {module_id for module_id, _ in NEW_BOUNDED_MODULES}

    for module_id, cases in fixture.items():
        assert isinstance(cases, dict)
        for case_name in ("positive", "negative"):
            case = cases[case_name]
            assert isinstance(case, dict)
            facts = case["facts"]
            expected = case["expected_disposition"]
            assert isinstance(facts, dict)
            assert isinstance(expected, str)
            routed = {item["module_id"]: item["disposition"] for item in route_as_json(facts)}
            assert routed[module_id] == expected, f"{module_id} {case_name} fixture"


def test_router_does_not_silently_convert_unknown_reuse_fact_to_na() -> None:
    facts: dict[str, object] = {
        "software": True,
        "nontrivial": True,
        "projectization": True,
        "multi_session": False,
        "agent_assisted": False,
        "horizontal_scope_risk": False,
    }
    routed = {item["module_id"]: item["disposition"] for item in route_as_json(facts)}
    assert routed["projectization.build-vs-reuse"] == "conditional"


def test_routing_is_invariant_to_project_fact_order() -> None:
    facts_a: dict[str, object] = {
        "software": True,
        "nontrivial": True,
        "projectization": True,
        "reusable_systems_possible": True,
        "multi_session": True,
        "agent_assisted": True,
        "horizontal_scope_risk": True,
        "empirical_quality_claims": True,
        "benchmark_or_dataset_use": True,
        "hidden_confirmatory_evaluation": True,
        "consequential_decisions": True,
        "durable_provenance_and_decision_lineage": True,
    }
    facts_b = dict(reversed(list(facts_a.items())))
    assert route_as_json(facts_a) == route_as_json(facts_b)


def test_routing_is_deterministic_on_repeat() -> None:
    facts: dict[str, object] = {
        "software": True,
        "nontrivial": True,
        "projectization": True,
        "reusable_systems_possible": False,
        "multi_session": True,
        "agent_assisted": False,
        "horizontal_scope_risk": None,
    }
    assert route_as_json(facts) == route_as_json(facts)
