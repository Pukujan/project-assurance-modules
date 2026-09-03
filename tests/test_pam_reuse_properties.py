from __future__ import annotations

import copy

import pytest

from scripts.pam_core import ROOT, load_json
from scripts.pam_reuse import validate_reuse_assessment


def valid_assessment() -> dict[str, object]:
    return load_json(ROOT / "examples" / "REUSE_ASSESSMENT.example.json")


def test_search_order_does_not_change_validity() -> None:
    assessment = copy.deepcopy(valid_assessment())
    searches = assessment["searches"]
    assert isinstance(searches, list)
    searches.reverse()
    validate_reuse_assessment(assessment, project_facts={"benchmark_or_dataset_use": True})


def test_candidate_order_does_not_change_validity() -> None:
    assessment = copy.deepcopy(valid_assessment())
    candidates = assessment["candidates"]
    assert isinstance(candidates, list)
    candidates.reverse()
    validate_reuse_assessment(assessment, project_facts={"benchmark_or_dataset_use": True})


def test_duplicate_search_id_fails_closed() -> None:
    assessment = copy.deepcopy(valid_assessment())
    searches = assessment["searches"]
    assert isinstance(searches, list)
    first = searches[0]
    second = searches[1]
    assert isinstance(first, dict)
    assert isinstance(second, dict)
    second["search_id"] = first["search_id"]
    with pytest.raises(ValueError, match="duplicate search_id"):
        validate_reuse_assessment(assessment)


def test_duplicate_candidate_id_fails_closed() -> None:
    assessment = copy.deepcopy(valid_assessment())
    candidates = assessment["candidates"]
    assert isinstance(candidates, list)
    first = candidates[0]
    second = candidates[1]
    assert isinstance(first, dict)
    assert isinstance(second, dict)
    second["candidate_id"] = first["candidate_id"]
    with pytest.raises(ValueError, match="duplicate candidate_id"):
        validate_reuse_assessment(assessment)
