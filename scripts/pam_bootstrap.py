from __future__ import annotations

import argparse
from pathlib import Path
from typing import cast

from jsonschema import Draft202012Validator, FormatChecker

from scripts.pam_core import ROOT, JSONDict, load_json

BOOTSTRAP_SCHEMA_PATH = ROOT / "schemas" / "bootstrap-acquisition.schema.json"


def _as_object(value: object, name: str) -> JSONDict:
    if not isinstance(value, dict):
        raise TypeError(f"{name} must be an object")
    return cast(JSONDict, value)


def validate_bootstrap(contract: JSONDict) -> None:
    schema = load_json(BOOTSTRAP_SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    validator.validate(contract)

    source = _as_object(contract["source"], "source")
    verification = _as_object(contract["verification"], "verification")
    requested = _as_object(source["requested_revision"], "source.requested_revision")

    resolved_commit = source["resolved_commit"]
    expected_commit = verification["expected_commit"]
    if resolved_commit != expected_commit:
        raise ValueError("resolved_commit must equal verification.expected_commit")

    if requested["kind"] == "git_commit" and requested["value"] != resolved_commit:
        raise ValueError("requested git commit must equal resolved_commit")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a PAM bootstrap/acquisition contract")
    parser.add_argument("contract", type=Path, help="Bootstrap/acquisition JSON path")
    args = parser.parse_args()

    validate_bootstrap(load_json(args.contract))
    print(f"validated bootstrap contract: {args.contract}")


if __name__ == "__main__":
    main()
