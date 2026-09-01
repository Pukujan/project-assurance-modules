from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
MODULE_SCHEMA_PATH = ROOT / "schemas" / "module.schema.json"
MANIFEST_SCHEMA_PATH = ROOT / "schemas" / "project-assurance-manifest.schema.json"

JSONDict = dict[str, Any]


@dataclass(frozen=True)
class RouteResult:
    module_id: str
    version: str
    disposition: str
    rationale: str


def load_json(path: Path) -> JSONDict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"expected JSON object in {path}")
    return cast(JSONDict, value)


def load_yaml(path: Path) -> JSONDict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"expected YAML mapping in {path}")
    return cast(JSONDict, value)


def _validator(schema_path: Path) -> Draft202012Validator:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def module_paths() -> list[Path]:
    return sorted(ROOT.glob("modules/**/module.yaml"))


def validate_module(module: JSONDict) -> None:
    _validator(MODULE_SCHEMA_PATH).validate(module)


def load_modules() -> dict[tuple[str, str], JSONDict]:
    modules: dict[tuple[str, str], JSONDict] = {}
    for path in module_paths():
        module = load_yaml(path)
        validate_module(module)
        module_id = module.get("module_id")
        version = module.get("version")
        if not isinstance(module_id, str) or not isinstance(version, str):
            raise TypeError(f"module identity is not string-valued in {path}")
        key = (module_id, version)
        if key in modules:
            raise ValueError(f"duplicate module identity {module_id}@{version}")
        modules[key] = module
    return modules


def validate_manifest(manifest: JSONDict) -> None:
    _validator(MANIFEST_SCHEMA_PATH).validate(manifest)
    modules = load_modules()

    selections = manifest.get("modules")
    if not isinstance(selections, list):
        raise TypeError("manifest modules must be a list")

    seen_modules: set[tuple[str, str]] = set()
    for raw_selection in selections:
        if not isinstance(raw_selection, dict):
            raise TypeError("manifest module selection must be an object")
        selection = cast(JSONDict, raw_selection)
        module_id = selection.get("module_id")
        version = selection.get("version")
        if not isinstance(module_id, str) or not isinstance(version, str):
            raise TypeError("manifest module identity must be string-valued")
        key = (module_id, version)
        if key in seen_modules:
            raise ValueError(f"duplicate manifest module selection {module_id}@{version}")
        seen_modules.add(key)
        if key not in modules:
            raise ValueError(f"unknown module {module_id}@{version}")

        module = modules[key]
        module_requirements = module.get("requirements")
        selection_requirements = selection.get("requirements")
        if not isinstance(module_requirements, list) or not isinstance(selection_requirements, list):
            raise TypeError(f"invalid requirements for {module_id}@{version}")

        expected_ids = {
            item["id"]
            for item in module_requirements
            if isinstance(item, dict) and isinstance(item.get("id"), str)
        }
        actual_ids = {
            item["requirement_id"]
            for item in selection_requirements
            if isinstance(item, dict) and isinstance(item.get("requirement_id"), str)
        }
        if expected_ids != actual_ids:
            missing = sorted(expected_ids - actual_ids)
            unknown = sorted(actual_ids - expected_ids)
            raise ValueError(
                f"requirement mismatch for {module_id}@{version}: missing={missing}, unknown={unknown}"
            )

        requirements_by_id = {
            cast(str, item["id"]): cast(JSONDict, item)
            for item in module_requirements
            if isinstance(item, dict) and isinstance(item.get("id"), str)
        }
        for raw_state in selection_requirements:
            if not isinstance(raw_state, dict):
                raise TypeError("manifest requirement state must be an object")
            state = cast(JSONDict, raw_state)
            requirement_id = state.get("requirement_id")
            if not isinstance(requirement_id, str):
                raise TypeError("requirement_id must be a string")
            if state.get("state") != "satisfied":
                continue
            allowed = requirements_by_id[requirement_id].get("evidence_kinds")
            evidence = state.get("evidence")
            if not isinstance(allowed, list) or not isinstance(evidence, list):
                raise TypeError(f"invalid evidence definition for {requirement_id}")
            allowed_kinds = {kind for kind in allowed if isinstance(kind, str)}
            for raw_evidence in evidence:
                if not isinstance(raw_evidence, dict):
                    raise TypeError(f"invalid evidence entry for {requirement_id}")
                kind = raw_evidence.get("kind")
                if not isinstance(kind, str) or kind not in allowed_kinds:
                    raise ValueError(
                        f"evidence kind {kind!r} is not allowed for requirement {requirement_id}"
                    )


def route_project(project_facts: JSONDict) -> list[RouteResult]:
    """Route only the v0 extracted modules from explicit declared project facts."""

    software = project_facts.get("software")
    nontrivial = project_facts.get("nontrivial")
    projectization = project_facts.get("projectization")
    reusable_systems_possible = project_facts.get("reusable_systems_possible")
    multi_session = project_facts.get("multi_session")
    agent_assisted = project_facts.get("agent_assisted")
    horizontal_scope_risk = project_facts.get("horizontal_scope_risk")

    results: list[RouteResult] = []

    if multi_session is True or agent_assisted is True:
        results.append(
            RouteResult(
                "continuity.structured-handoff",
                "0.1.0",
                "required",
                "Material work is expected to span sessions/agents or agent-assisted execution.",
            )
        )
    elif multi_session is False and agent_assisted is False:
        results.append(
            RouteResult(
                "continuity.structured-handoff",
                "0.1.0",
                "not_applicable",
                "Declared single-session, non-agent-assisted work has no material continuity boundary.",
            )
        )
    else:
        results.append(
            RouteResult(
                "continuity.structured-handoff",
                "0.1.0",
                "conditional",
                "Session/agent continuity facts are not fully declared; do not silently route to N/A.",
            )
        )

    if software is True and nontrivial is True and projectization is True:
        if reusable_systems_possible is True:
            disposition = "required"
            rationale = "Nontrivial software projectization declares plausible reusable systems."
        elif reusable_systems_possible is False:
            disposition = "recommended"
            rationale = (
                "Nontrivial software projectization declares no known reusable systems; preserve a "
                "lightweight search/disposition rather than assuming build_new."
            )
        else:
            disposition = "conditional"
            rationale = "Reuse possibility is unresolved; do not authorize build_new by default."
        results.append(
            RouteResult("projectization.build-vs-reuse", "0.1.0", disposition, rationale)
        )
    elif software is False:
        results.append(
            RouteResult(
                "projectization.build-vs-reuse",
                "0.1.0",
                "not_applicable",
                "The declared project does not contain a software implementation decision.",
            )
        )
    else:
        results.append(
            RouteResult(
                "projectization.build-vs-reuse",
                "0.1.0",
                "conditional",
                "Software/nontrivial/projectization facts are incomplete.",
            )
        )

    if projectization is True and nontrivial is True:
        if horizontal_scope_risk is False:
            disposition = "recommended"
            rationale = "Projectization is nontrivial but declares low horizontal-scope risk."
        elif horizontal_scope_risk is True:
            disposition = "required"
            rationale = "Nontrivial projectization declares material horizontal-scope risk."
        else:
            disposition = "required"
            rationale = (
                "Nontrivial projectization requires an explicit scope boundary; uncertainty cannot "
                "silently remove the boundary."
            )
        results.append(RouteResult("projectization.scope-boundary", "0.1.0", disposition, rationale))
    elif nontrivial is False:
        results.append(
            RouteResult(
                "projectization.scope-boundary",
                "0.1.0",
                "not_applicable",
                "The declared work is trivial and has no material project scope choice.",
            )
        )
    else:
        results.append(
            RouteResult(
                "projectization.scope-boundary",
                "0.1.0",
                "conditional",
                "Projectization complexity is not fully declared.",
            )
        )

    return results


def route_as_json(project_facts: JSONDict) -> list[JSONDict]:
    return [
        {
            "module_id": result.module_id,
            "version": result.version,
            "disposition": result.disposition,
            "rationale": result.rationale,
        }
        for result in route_project(project_facts)
    ]
