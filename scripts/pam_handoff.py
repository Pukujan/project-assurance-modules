from __future__ import annotations

import argparse
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from scripts.pam_core import ROOT, JSONDict, load_json

HANDOFF_SCHEMA_PATH = ROOT / "schemas" / "structured-handoff.schema.json"


def validate_handoff(state: JSONDict) -> None:
    schema = load_json(HANDOFF_SCHEMA_PATH)
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
