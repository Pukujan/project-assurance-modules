from __future__ import annotations

from dataclasses import dataclass
from typing import cast

from jsonschema import Draft202012Validator, FormatChecker

from scripts.pam_core import ROOT, JSONDict, load_json, load_modules, load_yaml, route_as_json

PROFILE_SCHEMA_PATH = ROOT / "schemas" / "profile.schema.json"


@dataclass(frozen=True)
class ProfileSelection:
    profile_id: str
    version: str
    disposition: str
    rationale: str


def _validator() -> Draft202012Validator:
    schema = load_json(PROFILE_SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_profile(profile: JSONDict) -> None:
    _validator().validate(profile)


def load_profiles() -> dict[tuple[str, str], JSONDict]:
    profiles: dict[tuple[str, str], JSONDict] = {}
    modules = load_modules()

    for path in sorted(ROOT.glob("profiles/**/profile.yaml")):
        profile = load_yaml(path)
        validate_profile(profile)
        profile_id = profile.get("profile_id")
        version = profile.get("version")
        if not isinstance(profile_id, str) or not isinstance(version, str):
            raise TypeError(f"profile identity is not string-valued in {path}")
        key = (profile_id, version)
        if key in profiles:
            raise ValueError(f"duplicate profile identity {profile_id}@{version}")

        refs = profile.get("modules")
        if not isinstance(refs, list):
            raise TypeError(f"profile modules must be a list in {path}")
        for raw_ref in refs:
            if not isinstance(raw_ref, dict):
                raise TypeError(f"profile module reference must be an object in {path}")
            module_id = raw_ref.get("module_id")
            module_version = raw_ref.get("version")
            if not isinstance(module_id, str) or not isinstance(module_version, str):
                raise TypeError(f"profile module identity must be string-valued in {path}")
            if (module_id, module_version) not in modules:
                raise ValueError(
                    f"profile {profile_id}@{version} references unknown module "
                    f"{module_id}@{module_version}"
                )

        profiles[key] = profile

    return profiles


def _condition_result(condition: JSONDict, project_facts: JSONDict) -> bool | None:
    fact = condition.get("fact")
    if not isinstance(fact, str):
        raise TypeError("profile fact condition must name a string fact")
    if fact not in project_facts:
        return None
    return project_facts[fact] == condition.get("equals")


def _selection_for_profile(profile: JSONDict, project_facts: JSONDict) -> ProfileSelection:
    profile_id = cast(str, profile["profile_id"])
    version = cast(str, profile["version"])
    selector = profile.get("selector")
    if not isinstance(selector, dict):
        raise TypeError(f"profile selector must be an object for {profile_id}@{version}")

    raw_all = selector.get("all_of")
    raw_any = selector.get("any_of")
    if not isinstance(raw_all, list) or not isinstance(raw_any, list):
        raise TypeError(f"profile selector lists are invalid for {profile_id}@{version}")

    all_results = [
        _condition_result(cast(JSONDict, item), project_facts)
        for item in raw_all
        if isinstance(item, dict)
    ]
    any_results = [
        _condition_result(cast(JSONDict, item), project_facts)
        for item in raw_any
        if isinstance(item, dict)
    ]

    all_state: bool | None
    if any(result is False for result in all_results):
        all_state = False
    elif any(result is None for result in all_results):
        all_state = None
    else:
        all_state = True

    any_state: bool | None
    if not any_results or any(result is True for result in any_results):
        any_state = True
    elif any(result is None for result in any_results):
        any_state = None
    else:
        any_state = False

    if all_state is False or any_state is False:
        return ProfileSelection(
            profile_id,
            version,
            "not_selected",
            "Declared project facts do not satisfy this profile selector.",
        )
    if all_state is None or any_state is None:
        return ProfileSelection(
            profile_id,
            version,
            "conditional",
            "One or more selector facts are undeclared; keep the profile visible until resolved.",
        )
    return ProfileSelection(
        profile_id,
        version,
        "selected",
        "Declared project facts satisfy this profile selector.",
    )


def select_profiles(project_facts: JSONDict) -> list[ProfileSelection]:
    profiles = load_profiles()
    return [
        _selection_for_profile(profile, project_facts) for _, profile in sorted(profiles.items())
    ]


def _module_keys(profile: JSONDict) -> set[tuple[str, str]]:
    refs = profile.get("modules")
    if not isinstance(refs, list):
        raise TypeError("profile modules must be a list")
    keys: set[tuple[str, str]] = set()
    for raw_ref in refs:
        if not isinstance(raw_ref, dict):
            raise TypeError("profile module reference must be an object")
        module_id = raw_ref.get("module_id")
        version = raw_ref.get("version")
        if not isinstance(module_id, str) or not isinstance(version, str):
            raise TypeError("profile module identity must be string-valued")
        keys.add((module_id, version))
    return keys


def compose_as_json(project_facts: JSONDict) -> JSONDict:
    profiles = load_profiles()
    selections = select_profiles(project_facts)
    candidate_modules: set[tuple[str, str]] = set()

    for selection in selections:
        if selection.disposition == "not_selected":
            continue
        profile = profiles[(selection.profile_id, selection.version)]
        candidate_modules.update(_module_keys(profile))

    modules = [
        item
        for item in route_as_json(project_facts)
        if (cast(str, item["module_id"]), cast(str, item["version"])) in candidate_modules
    ]
    return {
        "profiles": [
            {
                "profile_id": selection.profile_id,
                "version": selection.version,
                "disposition": selection.disposition,
                "rationale": selection.rationale,
            }
            for selection in selections
        ],
        "modules": modules,
    }


def validate_manifest_profile_refs(manifest: JSONDict) -> None:
    profiles = load_profiles()
    project_facts = manifest.get("project_facts")
    raw_refs = manifest.get("profiles")
    raw_modules = manifest.get("modules")
    if not isinstance(project_facts, dict):
        raise TypeError("manifest project_facts must be an object")
    if not isinstance(raw_refs, list):
        raise TypeError("manifest profiles must be a list")
    if not isinstance(raw_modules, list):
        raise TypeError("manifest modules must be a list")

    selections = {
        (selection.profile_id, selection.version): selection
        for selection in select_profiles(cast(JSONDict, project_facts))
    }
    seen: set[tuple[str, str]] = set()
    allowed_modules: set[tuple[str, str]] = set()

    for raw_ref in raw_refs:
        if not isinstance(raw_ref, dict):
            raise TypeError("manifest profile reference must be an object")
        profile_id = raw_ref.get("profile_id")
        version = raw_ref.get("version")
        if not isinstance(profile_id, str) or not isinstance(version, str):
            raise TypeError("manifest profile identity must be string-valued")
        key = (profile_id, version)
        if key in seen:
            raise ValueError(f"duplicate manifest profile reference {profile_id}@{version}")
        seen.add(key)
        if key not in profiles:
            raise ValueError(f"unknown profile {profile_id}@{version}")
        if selections[key].disposition == "not_selected":
            raise ValueError(
                f"profile {profile_id}@{version} is contradicted by declared project facts"
            )
        allowed_modules.update(_module_keys(profiles[key]))

    if not raw_refs:
        return

    for raw_module in raw_modules:
        if not isinstance(raw_module, dict):
            raise TypeError("manifest module selection must be an object")
        module_id = raw_module.get("module_id")
        version = raw_module.get("version")
        if not isinstance(module_id, str) or not isinstance(version, str):
            raise TypeError("manifest module identity must be string-valued")
        if (module_id, version) not in allowed_modules:
            raise ValueError(
                f"module {module_id}@{version} is not covered by the manifest's selected profiles"
            )
