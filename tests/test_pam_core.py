from __future__ import annotations

import copy

import pytest
from jsonschema import ValidationError

from scripts.pam_core import ROOT, load_json, load_modules, route_as_json, validate_manifest


def example_manifest() -> dict[str, object]:
    return load_json(ROOT / "examples" / "PROJECT_ASSURANCE.example.json")


def test_all_shipped_modules_validate_and_resolve() -> None:
    modules = load_modules()
    assert set(modules) == {
        ("continuity.structured-handoff", "0.1.0"),
        ("projectization.build-vs-reuse", "0.1.0"),
        ("projectization.scope-boundary", "0.1.0"),
    }


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
    }
    routed = {item["module_id"]: item["disposition"] for item in route_as_json(facts)}
    assert routed == {
        "continuity.structured-handoff": "required",
        "projectization.build-vs-reuse": "required",
        "projectization.scope-boundary": "required",
    }


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
