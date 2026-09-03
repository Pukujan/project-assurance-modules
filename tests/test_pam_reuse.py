from __future__ import annotations

import copy
import json

import pytest
from jsonschema import ValidationError

from scripts.pam_core import ROOT, load_json
from scripts.pam_reuse import validate_manifest_reuse_assessments, validate_reuse_assessment


def valid_assessment() -> dict[str, object]:
    return load_json(ROOT / "examples" / "REUSE_ASSESSMENT.example.json")


def test_valid_reuse_assessment_passes_with_dataset_fact() -> None:
    validate_reuse_assessment(
        valid_assessment(), project_facts={"benchmark_or_dataset_use": True}
    )


def test_interview_os_shortcut_regression_fails() -> None:
    shortcut = load_json(ROOT / "fixtures" / "reuse" / "interview-os-shortcut.json")
    with pytest.raises(ValueError):
        validate_reuse_assessment(
            shortcut, project_facts={"benchmark_or_dataset_use": True}
        )


def test_adopting_project_cannot_be_its_own_candidate() -> None:
    assessment = copy.deepcopy(valid_assessment())
    candidates = assessment["candidates"]
    project = assessment["project"]
    assert isinstance(candidates, list)
    assert isinstance(project, dict)
    first = candidates[0]
    assert isinstance(first, dict)
    identity = first["identity"]
    assert isinstance(identity, dict)
    identity["locator"] = project["repository"]
    with pytest.raises(ValueError, match="adopting project itself"):
        validate_reuse_assessment(assessment)


def test_pam_cannot_count_as_product_or_runtime_candidate() -> None:
    assessment = copy.deepcopy(valid_assessment())
    candidates = assessment["candidates"]
    assert isinstance(candidates, list)
    first = candidates[0]
    assert isinstance(first, dict)
    identity = first["identity"]
    assert isinstance(identity, dict)
    identity["locator"] = "Pukujan/project-assurance-modules"
    with pytest.raises(ValueError, match="PAM methodology"):
        validate_reuse_assessment(assessment)


def test_abstract_serious_candidate_fails_even_with_concrete_locator() -> None:
    assessment = copy.deepcopy(valid_assessment())
    candidates = assessment["candidates"]
    assert isinstance(candidates, list)
    first = candidates[0]
    assert isinstance(first, dict)
    first["name"] = "generic quiz framework"
    with pytest.raises(ValueError, match="abstract category"):
        validate_reuse_assessment(assessment)


def test_internal_only_discovery_cannot_satisfy_required_external_search() -> None:
    assessment = copy.deepcopy(valid_assessment())
    searches = assessment["searches"]
    assert isinstance(searches, list)
    assessment["searches"] = [
        search for search in searches if isinstance(search, dict) and search.get("scope") == "internal"
    ]
    with pytest.raises((ValidationError, ValueError)):
        validate_reuse_assessment(assessment)


def test_required_asset_class_must_have_traceable_search() -> None:
    assessment = copy.deepcopy(valid_assessment())
    search_plan = assessment["search_plan"]
    assert isinstance(search_plan, dict)
    search_plan["required_asset_classes"] = ["model"]
    with pytest.raises(ValueError, match="asset classes were not searched"):
        validate_reuse_assessment(assessment)


def test_dataset_fact_requires_asset_discovery_plan() -> None:
    assessment = copy.deepcopy(valid_assessment())
    search_plan = assessment["search_plan"]
    assert isinstance(search_plan, dict)
    search_plan["required_asset_classes"] = []
    with pytest.raises(ValueError, match="benchmark_or_dataset_use=true"):
        validate_reuse_assessment(
            assessment, project_facts={"benchmark_or_dataset_use": True}
        )


def test_self_authored_relative_search_receipt_is_not_concrete_search_evidence() -> None:
    assessment = copy.deepcopy(valid_assessment())
    searches = assessment["searches"]
    assert isinstance(searches, list)
    first = searches[0]
    assert isinstance(first, dict)
    receipts = first["receipts"]
    assert isinstance(receipts, list)
    receipt = receipts[0]
    assert isinstance(receipt, dict)
    receipt["locator"] = "docs/BUILD_VS_REUSE.md"
    with pytest.raises(ValueError, match="non-concrete locator"):
        validate_reuse_assessment(assessment)


def test_serious_candidate_requires_traceable_receipts() -> None:
    assessment = copy.deepcopy(valid_assessment())
    candidates = assessment["candidates"]
    assert isinstance(candidates, list)
    first = candidates[0]
    assert isinstance(first, dict)
    first["evidence_receipts"] = []
    with pytest.raises(ValueError, match="no search/source receipts"):
        validate_reuse_assessment(assessment)


def test_build_new_cannot_finalize_with_unresolved_full_candidate_probe() -> None:
    assessment = copy.deepcopy(valid_assessment())
    candidates = assessment["candidates"]
    assert isinstance(candidates, list)
    first = candidates[0]
    assert isinstance(first, dict)
    first["disposition"] = "spike_required"
    with pytest.raises(ValueError, match="still require probes"):
        validate_reuse_assessment(assessment)


def test_build_new_can_pass_when_broad_search_finds_no_full_candidate() -> None:
    assessment = copy.deepcopy(valid_assessment())
    candidates = assessment["candidates"]
    probes = assessment["probes"]
    assert isinstance(candidates, list)
    assert isinstance(probes, list)
    assessment["candidates"] = [
        candidate
        for candidate in candidates
        if isinstance(candidate, dict) and candidate.get("coverage") == "partial"
    ]
    assessment["probes"] = [
        probe
        for probe in probes
        if isinstance(probe, dict) and probe.get("candidate_id") == "study-os"
    ]
    validate_reuse_assessment(assessment)


def test_unknown_reuse_assessment_version_fails_closed() -> None:
    assessment = copy.deepcopy(valid_assessment())
    assessment["schema_version"] = "pam-reuse-assessment/9.9.9"
    with pytest.raises(ValidationError):
        validate_reuse_assessment(assessment)


def test_manifest_satisfied_reuse_requirements_validate_shared_artifact(tmp_path) -> None:
    assessment_path = tmp_path / "REUSE_ASSESSMENT.json"
    assessment_path.write_text(json.dumps(valid_assessment()), encoding="utf-8")
    manifest: dict[str, object] = {
        "project_facts": {"benchmark_or_dataset_use": True},
        "modules": [
            {
                "module_id": "projectization.build-vs-reuse",
                "version": "0.2.0",
                "requirements": [
                    {
                        "requirement_id": "REUSE_002",
                        "state": "satisfied",
                        "evidence": [
                            {
                                "kind": "artifact",
                                "locator": "REUSE_ASSESSMENT.json",
                                "note": "validated reuse discovery",
                            }
                        ],
                    },
                    {
                        "requirement_id": "REUSE_008",
                        "state": "satisfied",
                        "evidence": [
                            {
                                "kind": "artifact",
                                "locator": "REUSE_ASSESSMENT.json",
                                "note": "reviewed final disposition",
                            }
                        ],
                    },
                ],
            }
        ],
    }
    validate_manifest_reuse_assessments(manifest, tmp_path)


def test_manifest_final_disposition_rejects_draft_assessment(tmp_path) -> None:
    assessment = valid_assessment()
    assessment["assessment_status"] = "draft"
    decision = assessment["decision"]
    assert isinstance(decision, dict)
    review = decision["human_review"]
    assert isinstance(review, dict)
    review["status"] = "pending"
    review["evidence"] = None
    (tmp_path / "REUSE_ASSESSMENT.json").write_text(
        json.dumps(assessment), encoding="utf-8"
    )
    manifest: dict[str, object] = {
        "project_facts": {"benchmark_or_dataset_use": True},
        "modules": [
            {
                "module_id": "projectization.build-vs-reuse",
                "version": "0.2.0",
                "requirements": [
                    {
                        "requirement_id": "REUSE_008",
                        "state": "satisfied",
                        "evidence": [
                            {
                                "kind": "artifact",
                                "locator": "REUSE_ASSESSMENT.json",
                                "note": "draft should not close final disposition",
                            }
                        ],
                    }
                ],
            }
        ],
    }
    with pytest.raises(ValueError, match="draft reuse assessment"):
        validate_manifest_reuse_assessments(manifest, tmp_path)
