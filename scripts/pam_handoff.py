from __future__ import annotations

import argparse
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, ValidationError

from scripts.pam_core import ROOT, JSONDict, load_json

HANDOFF_SCHEMA_PATHS = {
    "pam-handoff/0.1.0": ROOT / "schemas" / "structured-handoff.schema.json",
    "pam-handoff/0.2.0": ROOT / "schemas" / "structured-handoff-v0.2.schema.json",
}


def validate_handoff(state: JSONDict) -> None:
    schema_version = state.get("schema_version")
    if not isinstance(schema_version, str) or schema_version not in HANDOFF_SCHEMA_PATHS:
        raise ValidationError(f"unsupported handoff schema_version: {schema_version!r}")

    schema = load_json(HANDOFF_SCHEMA_PATHS[schema_version])
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    validator.validate(state)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a PAM generic structured handoff")
    parser.add_argument("state", type=Path, help="Structured handoff JSON path")
    args = parser.parse_args()

    validate_handoff(load_json(args.state))
    print(f"validated handoff: {args.state}")


if __name__ == "__main__":
    main()
