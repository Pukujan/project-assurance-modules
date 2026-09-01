from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts.pam_core import load_json, route_as_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Route v0 PAM modules from explicit project facts")
    parser.add_argument("facts", help="Path to JSON object containing declared project facts")
    args = parser.parse_args()

    facts = load_json(Path(args.facts))
    print(json.dumps(route_as_json(facts), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
