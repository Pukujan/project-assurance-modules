from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import cast

from jsonschema import Draft202012Validator, FormatChecker

from scripts.pam_core import ROOT, JSONDict, load_json

REUSE_SCHEMA_PATH = ROOT / "schemas" / "reuse-assessment.schema.json"
PAM_REPOSITORY = "Pukujan/project-assurance-modules"
ABSTRACT_CANDIDATE_TERMS = (
    "generic quiz framework",
    "generic framework",
    "existing library",
    "some oss",
    "some open source",
    "generic solution",
)
CONCRETE_REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
CONCRETE_PREFIXES = ("npm:", "pypi:", "cargo:", "standard:")
ASSET_CLASSES = {"dataset", "model", "corpus", "benchmark", "question_bank", "content_asset"}
REUSE_ASSESSMENT_REQUIREMENTS = {
    "REUSE_002",
    "REUSE_003",
    "REUSE_004",
    "REUSE_005",
    "REUSE_006",
    "REUSE_007",
    "REUSE_008",
}


def _validator() -> Draft202012Validator:
    schema = load_json(REUSE_SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _as_dict(value: object, name: str) -> JSONDict:
    if not isinstance(value, dict):
        raise TypeError(f"{name} must be an object")
    return cast(JSONDict, value)


def _as_list(value: object, name: str) -> list[object]:
    if not isinstance(value, list):
        raise TypeError(f"{name} must be a list")
    return cast(list[object], value)


def _as_string(value: object, name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string")
    return value


def _is_concrete_locator(locator: str) -> bool:
    return (
        "://" in locator
        or bool(CONCRETE_REPOSITORY.fullmatch(locator))
        or locator.startswith(CONCRETE_PREFIXES)
    )


def _is_concrete_receipt_locator(kind: str, locator: str) -> bool:
    if kind == "repository":
        return bool(CONCRETE_REPOSITORY.fullmatch(locator))
    if kind in {"url", "search_result", "catalog"}:
        return "://" in locator
    if kind == "package_registry":
        return locator.startswith(("npm:", "pypi:", "cargo:")) or "://" in locator
    if kind == "standard":
        return locator.startswith("standard:") or "://" in locator
    return False


def validate_reuse_assessment(
    assessment: JSONDict,
    *,
    project_facts: JSONDict | None = None,
) -> None:
    _validator().validate(assessment)

    project = _as_dict(assessment["project"], "project")
    project_repository = _as_string(project["repository"], "project.repository")
    search_plan = _as_dict(assessment["search_plan"], "search_plan")
    searches = _as_list(assessment["searches"], "searches")
    candidates = _as_list(assessment["candidates"], "candidates")
    probes = _as_list(assessment["probes"], "probes")
    decision = _as_dict(assessment["decision"], "decision")

    search_ids: set[str] = set()
    receipt_ids: set[str] = set()
    receipt_scopes: dict[str, str] = {}
    scopes: set[str] = set()
    searched_asset_classes: set[str] = set()

    for raw_search in searches:
        search = _as_dict(raw_search, "search")
        search_id = _as_string(search["search_id"], "search.search_id")
        if search_id in search_ids:
            raise ValueError(f"duplicate search_id {search_id}")
        search_ids.add(search_id)
        scope = _as_string(search["scope"], "search.scope")
        scopes.add(scope)
        target_classes = {
            _as_string(value, "search.target_classes item")
            for value in _as_list(search["target_classes"], "search.target_classes")
        }
        searched_asset_classes.update(target_classes & ASSET_CLASSES)
        for raw_receipt in _as_list(search["receipts"], "search.receipts"):
            receipt = _as_dict(raw_receipt, "search receipt")
            receipt_id = _as_string(receipt["receipt_id"], "receipt.receipt_id")
            if receipt_id in receipt_ids:
                raise ValueError(f"duplicate receipt_id {receipt_id}")
            receipt_ids.add(receipt_id)
            receipt_scopes[receipt_id] = scope
            kind = _as_string(receipt["kind"], "receipt.kind")
            locator = _as_string(receipt["locator"], "receipt.locator")
            if not _is_concrete_receipt_locator(kind, locator):
                raise ValueError(
                    f"search receipt {receipt_id} has non-concrete locator {locator!r} for kind {kind!r}"
                )

    required_scopes = {
        _as_string(value, "search_plan.required_scopes item")
        for value in _as_list(search_plan["required_scopes"], "search_plan.required_scopes")
    }
    missing_scopes = sorted(required_scopes - scopes)
    if missing_scopes:
        raise ValueError(f"required search scopes were not executed: {missing_scopes}")

    required_asset_classes = {
        _as_string(value, "search_plan.required_asset_classes item")
        for value in _as_list(
            search_plan["required_asset_classes"], "search_plan.required_asset_classes"
        )
    }
    missing_assets = sorted(required_asset_classes - searched_asset_classes)
    if missing_assets:
        raise ValueError(f"required reusable asset classes were not searched: {missing_assets}")

    if (
        project_facts is not None
        and project_facts.get("benchmark_or_dataset_use") is True
        and not required_asset_classes
    ):
        raise ValueError(
            "benchmark_or_dataset_use=true requires at least one reusable asset class search"
        )

    candidate_ids: set[str] = set()
    candidate_by_id: dict[str, JSONDict] = {}
    serious_full_candidates: list[JSONDict] = []
    for raw_candidate in candidates:
        candidate = _as_dict(raw_candidate, "candidate")
        candidate_id = _as_string(candidate["candidate_id"], "candidate.candidate_id")
        if candidate_id in candidate_ids:
            raise ValueError(f"duplicate candidate_id {candidate_id}")
        candidate_ids.add(candidate_id)
        candidate_by_id[candidate_id] = candidate

        name = _as_string(candidate["name"], "candidate.name").strip().lower()
        origin = _as_string(candidate["origin"], "candidate.origin")
        identity = _as_dict(candidate["identity"], "candidate.identity")
        locator = _as_string(identity["locator"], "candidate.identity.locator")
        serious = bool(candidate["serious"])

        if locator == project_repository:
            raise ValueError(f"candidate {candidate_id} is the adopting project itself")
        if locator == PAM_REPOSITORY:
            raise ValueError(
                f"candidate {candidate_id} is PAM methodology and cannot count as a product/runtime alternative"
            )
        if not _is_concrete_locator(locator):
            raise ValueError(f"candidate {candidate_id} has non-concrete locator {locator!r}")
        if serious and any(term in name for term in ABSTRACT_CANDIDATE_TERMS):
            raise ValueError(
                f"serious candidate {candidate_id} is an abstract category, not an identified alternative"
            )

        evidence_receipts = {
            _as_string(value, "candidate.evidence_receipts item")
            for value in _as_list(candidate["evidence_receipts"], "candidate.evidence_receipts")
        }
        if serious and not evidence_receipts:
            raise ValueError(f"serious candidate {candidate_id} has no search/source receipts")
        unknown_receipts = sorted(evidence_receipts - receipt_ids)
        if unknown_receipts:
            raise ValueError(
                f"candidate {candidate_id} references unknown receipts: {unknown_receipts}"
            )
        if serious and not any(
            receipt_scopes[receipt_id] == origin for receipt_id in evidence_receipts
        ):
            raise ValueError(
                f"serious candidate {candidate_id} has no evidence receipt from its declared {origin} search scope"
            )
        if serious and candidate.get("coverage") == "full":
            serious_full_candidates.append(candidate)

    probe_candidates: set[str] = set()
    for raw_probe in probes:
        probe = _as_dict(raw_probe, "probe")
        candidate_id = _as_string(probe["candidate_id"], "probe.candidate_id")
        if candidate_id not in candidate_ids:
            raise ValueError(f"probe references unknown candidate {candidate_id}")
        if candidate_id in probe_candidates:
            raise ValueError(f"duplicate probe for candidate {candidate_id}")
        probe_candidates.add(candidate_id)
        status = _as_string(probe["status"], "probe.status")
        evidence = _as_list(probe["evidence"], "probe.evidence")
        rationale = probe.get("rationale")
        if status == "run" and not evidence:
            raise ValueError(f"run probe for {candidate_id} must include evidence")
        if status == "not_run" and not isinstance(rationale, str):
            raise ValueError(f"not-run probe for {candidate_id} requires rationale")

    for candidate in serious_full_candidates:
        candidate_id = _as_string(candidate["candidate_id"], "candidate.candidate_id")
        if (
            candidate.get("disposition") in {"reject", "spike_required"}
            and candidate_id not in probe_candidates
        ):
            raise ValueError(
                f"serious full-coverage candidate {candidate_id} requires probe evidence or a not-run rationale"
            )

    selected_candidate_ids = {
        _as_string(value, "decision.selected_candidate_ids item")
        for value in _as_list(decision["selected_candidate_ids"], "decision.selected_candidate_ids")
    }
    unknown_selected = sorted(selected_candidate_ids - candidate_ids)
    if unknown_selected:
        raise ValueError(f"decision selects unknown candidates: {unknown_selected}")
    invalid_selected = sorted(
        candidate_id
        for candidate_id in selected_candidate_ids
        if candidate_by_id[candidate_id].get("disposition") in {"reject", "spike_required"}
    )
    if invalid_selected:
        raise ValueError(f"decision selects rejected or unresolved candidates: {invalid_selected}")

    disposition = _as_string(decision["disposition"], "decision.disposition")
    if disposition == "build_new":
        unmet = _as_list(
            decision["build_new_unmet_requirements"], "decision.build_new_unmet_requirements"
        )
        if not unmet:
            raise ValueError("build_new requires concrete unmet requirements")
        unresolved_full = [
            _as_string(candidate["candidate_id"], "candidate.candidate_id")
            for candidate in serious_full_candidates
            if candidate.get("disposition") == "spike_required"
        ]
        if unresolved_full:
            raise ValueError(
                "build_new cannot be finalized while serious full-coverage candidates still require probes: "
                f"{unresolved_full}"
            )
    elif disposition not in {"more_research"} and not selected_candidate_ids:
        raise ValueError(f"{disposition} requires at least one selected candidate")

    if assessment.get("assessment_status") == "reviewed":
        review = _as_dict(decision["human_review"], "decision.human_review")
        if review.get("status") != "approved" or not isinstance(review.get("evidence"), str):
            raise ValueError("reviewed assessments require approved human review evidence")


def validate_manifest_reuse_assessments(manifest: JSONDict, project_root: Path) -> None:
    raw_modules = manifest.get("modules")
    if not isinstance(raw_modules, list):
        raise TypeError("manifest modules must be a list")

    for raw_module in raw_modules:
        if not isinstance(raw_module, dict):
            continue
        module = cast(JSONDict, raw_module)
        if (
            module.get("module_id") != "projectization.build-vs-reuse"
            or module.get("version") != "0.2.0"
        ):
            continue
        raw_requirements = module.get("requirements")
        if not isinstance(raw_requirements, list):
            raise TypeError("build-vs-reuse requirements must be a list")

        assessment_locators: set[str] = set()
        satisfied_assessment_requirement = False
        final_disposition_satisfied = False
        for raw_requirement in raw_requirements:
            if not isinstance(raw_requirement, dict):
                continue
            requirement = cast(JSONDict, raw_requirement)
            requirement_id = requirement.get("requirement_id")
            if requirement_id not in REUSE_ASSESSMENT_REQUIREMENTS:
                continue
            if requirement.get("state") != "satisfied":
                continue
            satisfied_assessment_requirement = True
            if requirement_id == "REUSE_008":
                final_disposition_satisfied = True
            evidence = requirement.get("evidence")
            if not isinstance(evidence, list):
                raise TypeError(f"invalid evidence for {requirement_id}")
            for raw_evidence in evidence:
                if not isinstance(raw_evidence, dict):
                    continue
                if raw_evidence.get("kind") == "artifact" and isinstance(
                    raw_evidence.get("locator"), str
                ):
                    assessment_locators.add(cast(str, raw_evidence["locator"]))

        if not satisfied_assessment_requirement:
            continue
        if not assessment_locators:
            raise ValueError(
                "build-vs-reuse@0.2.0 satisfied requirements require a reuse assessment artifact"
            )
        if len(assessment_locators) != 1:
            raise ValueError(
                "build-vs-reuse@0.2.0 satisfied requirements must reference one shared reuse assessment artifact"
            )

        locator = next(iter(assessment_locators))
        path = (project_root / locator).resolve()
        root = project_root.resolve()
        if root not in path.parents and path != root:
            raise ValueError("reuse assessment artifact must stay within the adopting project")
        if not path.is_file():
            raise ValueError(f"reuse assessment artifact does not exist: {locator}")
        assessment = load_json(path)
        project_facts = manifest.get("project_facts")
        if not isinstance(project_facts, dict):
            raise TypeError("manifest project_facts must be an object")
        validate_reuse_assessment(assessment, project_facts=cast(JSONDict, project_facts))
        if final_disposition_satisfied and assessment.get("assessment_status") != "reviewed":
            raise ValueError("REUSE_008 cannot be satisfied by a draft reuse assessment")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate a machine-readable PAM build-vs-reuse assessment"
    )
    parser.add_argument("assessment", help="Reuse assessment JSON path")
    args = parser.parse_args()
    path = Path(args.assessment)
    assessment = load_json(path)
    validate_reuse_assessment(assessment)
    print(f"validated reuse assessment: {path}")


if __name__ == "__main__":
    main()
