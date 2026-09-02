from __future__ import annotations

import copy

import pytest
from jsonschema import ValidationError

from scripts.pam_core import ROOT, load_json
from scripts.pam_handoff import validate_handoff


def example_handoff_v0_1() -> dict[str, object]:
    return load_json(ROOT / "examples" / "HANDOFF_STATE.example.json")


def example_handoff_v0_2() -> dict[str, object]:
    return load_json(ROOT / "examples" / "HANDOFF_STATE.v0.2.example.json")


def test_v0_1_example_handoff_validates() -> None:
    validate_handoff(example_handoff_v0_1())


def test_v0_2_example_handoff_validates() -> None:
    validate_handoff(example_handoff_v0_2())


def test_unknown_handoff_schema_version_fails() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    state["schema_version"] = "pam-handoff/999.0.0"
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_missing_next_action_fails() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    del state["next_action"]
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_unknown_assurance_field_fails_closed() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    state["verified"] = True
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_bad_methodology_revision_fails() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    methodology = state["methodology"]
    assert isinstance(methodology, dict)
    methodology["revision"] = "not-a-git-sha"
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_bad_component_git_identity_fails() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    components = state["components"]
    assert isinstance(components, list)
    component = components[0]
    assert isinstance(component, dict)
    observed = component["observed_identity"]
    assert isinstance(observed, dict)
    observed["value"] = "short"
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_live_state_precedence_cannot_be_disabled() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    reconciliation = state["reconciliation"]
    assert isinstance(reconciliation, dict)
    reconciliation["live_state_wins"] = False
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_reconciliation_requires_at_least_one_live_check() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    reconciliation = state["reconciliation"]
    assert isinstance(reconciliation, dict)
    reconciliation["checks"] = []
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_hidden_evaluation_cannot_be_exposed() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    hidden = state["hidden_evaluation"]
    assert isinstance(hidden, dict)
    hidden["agent_visible_hidden_material"] = True
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_component_can_use_non_git_exact_identity() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    components = state["components"]
    assert isinstance(components, list)
    components.append(
        {
            "name": "External schema package",
            "role": "versioned contract dependency",
            "locator": "registry.example/schema",
            "observed_identity": {"kind": "version", "value": "2.4.1"},
            "tested_identity": {"kind": "digest", "value": "sha256:abcd"},
        }
    )
    validate_handoff(state)


def test_v0_2_requires_project_observed_identity() -> None:
    state = copy.deepcopy(example_handoff_v0_2())
    project = state["project"]
    assert isinstance(project, dict)
    del project["observed_identity"]
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_v0_2_requires_project_active_issue_field() -> None:
    state = copy.deepcopy(example_handoff_v0_2())
    project = state["project"]
    assert isinstance(project, dict)
    del project["active_issue"]
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_v0_2_requires_component_issue_and_pr_fields() -> None:
    state = copy.deepcopy(example_handoff_v0_2())
    components = state["components"]
    assert isinstance(components, list)
    component = components[0]
    assert isinstance(component, dict)
    del component["issue"]
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_v0_1_rejects_v0_2_project_routing_fields() -> None:
    state = copy.deepcopy(example_handoff_v0_1())
    project = state["project"]
    assert isinstance(project, dict)
    project["active_issue"] = 1
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_v0_2_preserves_ra_project_and_component_routing_identity() -> None:
    state = example_handoff_v0_2()
    project = state["project"]
    components = state["components"]
    assert isinstance(project, dict)
    assert project["active_issue"] == 1
    observed = project["observed_identity"]
    assert isinstance(observed, dict)
    assert observed["value"] == "8b5fa8f16dbc434126fa838e4e2eaff5a1b3e8f6"
    assert isinstance(components, list)
    pam_component = components[1]
    assert isinstance(pam_component, dict)
    assert pam_component["issue"] == 1
    assert "pr" in pam_component
    validate_handoff(state)
