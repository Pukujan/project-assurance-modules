from __future__ import annotations

import copy

import pytest
from jsonschema import ValidationError

from scripts.pam_bootstrap import validate_bootstrap
from scripts.pam_core import ROOT, load_json


def example_bootstrap() -> dict[str, object]:
    return load_json(ROOT / "examples" / "BOOTSTRAP_ACQUISITION.example.json")


def test_example_bootstrap_validates() -> None:
    validate_bootstrap(example_bootstrap())


def test_unknown_bootstrap_field_fails_closed() -> None:
    contract = copy.deepcopy(example_bootstrap())
    contract["verified"] = True
    with pytest.raises(ValidationError):
        validate_bootstrap(contract)


def test_bad_requested_git_commit_fails() -> None:
    contract = copy.deepcopy(example_bootstrap())
    source = contract["source"]
    assert isinstance(source, dict)
    requested = source["requested_revision"]
    assert isinstance(requested, dict)
    requested["value"] = "short"
    with pytest.raises(ValidationError):
        validate_bootstrap(contract)


def test_requested_git_commit_must_match_resolved_commit() -> None:
    contract = copy.deepcopy(example_bootstrap())
    source = contract["source"]
    assert isinstance(source, dict)
    requested = source["requested_revision"]
    assert isinstance(requested, dict)
    requested["value"] = "8f4737fc212e6b09f8066d90e178aa8760e619fb"
    with pytest.raises(ValueError, match="requested git commit"):
        validate_bootstrap(contract)


def test_resolved_commit_must_match_verification_target() -> None:
    contract = copy.deepcopy(example_bootstrap())
    verification = contract["verification"]
    assert isinstance(verification, dict)
    verification["expected_commit"] = "8f4737fc212e6b09f8066d90e178aa8760e619fb"
    with pytest.raises(ValueError, match="resolved_commit"):
        validate_bootstrap(contract)


def test_checkout_must_be_detached() -> None:
    contract = copy.deepcopy(example_bootstrap())
    acquisition = contract["acquisition"]
    assert isinstance(acquisition, dict)
    acquisition["checkout_mode"] = "branch"
    with pytest.raises(ValidationError):
        validate_bootstrap(contract)


def test_revision_mismatch_cannot_continue_to_routing() -> None:
    contract = copy.deepcopy(example_bootstrap())
    behavior = contract["failure_behavior"]
    assert isinstance(behavior, dict)
    behavior["revision_mismatch"] = "continue"
    with pytest.raises(ValidationError):
        validate_bootstrap(contract)


def test_start_locator_must_exist_before_routing() -> None:
    contract = copy.deepcopy(example_bootstrap())
    start = contract["start"]
    assert isinstance(start, dict)
    start["must_exist_before_routing"] = False
    with pytest.raises(ValidationError):
        validate_bootstrap(contract)


def test_working_tree_bytes_cannot_be_primary_identity() -> None:
    contract = copy.deepcopy(example_bootstrap())
    identity = contract["content_identity"]
    assert isinstance(identity, dict)
    identity["working_tree_bytes_authoritative"] = True
    with pytest.raises(ValidationError):
        validate_bootstrap(contract)


def test_tag_revision_is_bound_to_immutable_commit() -> None:
    contract = copy.deepcopy(example_bootstrap())
    source = contract["source"]
    assert isinstance(source, dict)
    source["requested_revision"] = {"kind": "git_tag", "value": "v0.2.0-rc1"}
    validate_bootstrap(contract)
