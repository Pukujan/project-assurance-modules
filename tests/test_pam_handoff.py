from __future__ import annotations

import copy

import pytest
from jsonschema import ValidationError

from scripts.pam_core import ROOT, load_json
from scripts.pam_handoff import validate_handoff


def example_handoff() -> dict[str, object]:
    return load_json(ROOT / "examples" / "HANDOFF_STATE.example.json")


def test_example_handoff_validates() -> None:
    validate_handoff(example_handoff())


def test_unknown_handoff_schema_version_fails() -> None:
    state = copy.deepcopy(example_handoff())
    state["schema_version"] = "pam-handoff/999.0.0"
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_missing_next_action_fails() -> None:
    state = copy.deepcopy(example_handoff())
    del state["next_action"]
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_unknown_assurance_field_fails_closed() -> None:
    state = copy.deepcopy(example_handoff())
    state["verified"] = True
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_bad_methodology_revision_fails() -> None:
    state = copy.deepcopy(example_handoff())
    methodology = state["methodology"]
    assert isinstance(methodology, dict)
    methodology["revision"] = "not-a-git-sha"
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_bad_component_git_identity_fails() -> None:
    state = copy.deepcopy(example_handoff())
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
    state = copy.deepcopy(example_handoff())
    reconciliation = state["reconciliation"]
    assert isinstance(reconciliation, dict)
    reconciliation["live_state_wins"] = False
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_reconciliation_requires_at_least_one_live_check() -> None:
    state = copy.deepcopy(example_handoff())
    reconciliation = state["reconciliation"]
    assert isinstance(reconciliation, dict)
    reconciliation["checks"] = []
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_hidden_evaluation_cannot_be_exposed() -> None:
    state = copy.deepcopy(example_handoff())
    hidden = state["hidden_evaluation"]
    assert isinstance(hidden, dict)
    hidden["agent_visible_hidden_material"] = True
    with pytest.raises(ValidationError):
        validate_handoff(state)


def test_component_can_use_non_git_exact_identity() -> None:
    state = copy.deepcopy(example_handoff())
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
