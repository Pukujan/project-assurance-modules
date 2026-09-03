from __future__ import annotations

import argparse
from pathlib import Path

from scripts.pam_core import load_json, load_modules, validate_manifest
from scripts.pam_profiles import validate_manifest_profile_refs
from scripts.pam_reuse import validate_manifest_reuse_assessments


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate PAM methodology modules and a project manifest"
    )
    parser.add_argument("manifest", nargs="?", help="Optional Project Assurance manifest JSON path")
    args = parser.parse_args()

    modules = load_modules()
    print(f"validated modules: {len(modules)}")

    if args.manifest:
        path = Path(args.manifest)
        manifest = load_json(path)
        validate_manifest(manifest)
        validate_manifest_profile_refs(manifest)
        validate_manifest_reuse_assessments(manifest, path.parent)
        print(f"validated manifest: {path}")


if __name__ == "__main__":
    main()
