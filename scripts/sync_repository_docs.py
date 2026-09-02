from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import yaml

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = Path("docs/repository-state.json")
README_START = "<!-- BEGIN PAM GENERATED REPOSITORY STATUS -->"
README_END = "<!-- END PAM GENERATED REPOSITORY STATUS -->"
ARCH_START = "<!-- BEGIN PAM GENERATED INVENTORY -->"
ARCH_END = "<!-- END PAM GENERATED INVENTORY -->"


@dataclass(frozen=True)
class RepositoryState:
    label: str
    landing_merge_commit: str
    frozen_tested_revision: str
    status: str
    stability_level: str
    consumer_rule: str
    source_adopter: str
    reference_boundary: str


@dataclass(frozen=True, order=True)
class InventoryItem:
    identity: str
    version: str
    title: str
    path: str


@dataclass(frozen=True)
class Inventory:
    modules: tuple[InventoryItem, ...]
    profiles: tuple[InventoryItem, ...]
    schemas: tuple[str, ...]


def _mapping(value: object, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    return cast(dict[str, Any], value)


def _string(mapping: dict[str, Any], key: str, name: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name}.{key} must be a non-empty string")
    return value


def load_state(root: Path = ROOT) -> RepositoryState:
    raw = json.loads((root / STATE_PATH).read_text(encoding="utf-8"))
    top = _mapping(raw, "repository state")
    if top.get("schema_version") != "pam-repository-state/1.0.0":
        raise ValueError("repository state schema_version must be 'pam-repository-state/1.0.0'")

    landed = _mapping(top.get("landed_methodology"), "landed_methodology")
    stability = _mapping(top.get("stability"), "stability")
    reference = _mapping(top.get("reference"), "reference")
    return RepositoryState(
        label=_string(landed, "label", "landed_methodology"),
        landing_merge_commit=_string(landed, "landing_merge_commit", "landed_methodology"),
        frozen_tested_revision=_string(landed, "frozen_tested_revision", "landed_methodology"),
        status=_string(landed, "status", "landed_methodology"),
        stability_level=_string(stability, "level", "stability"),
        consumer_rule=_string(stability, "consumer_rule", "stability"),
        source_adopter=_string(reference, "source_adopter", "reference"),
        reference_boundary=_string(reference, "boundary", "reference"),
    )


def _yaml_mapping(path: Path) -> dict[str, Any]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{path} must contain a YAML object")
    return cast(dict[str, Any], raw)


def _inventory_item(path: Path, *, id_key: str, root: Path) -> InventoryItem:
    data = _yaml_mapping(path)
    identity = _string(data, id_key, path.as_posix())
    version = _string(data, "version", path.as_posix())
    title = _string(data, "title", path.as_posix())
    return InventoryItem(identity, version, title, path.relative_to(root).as_posix())


def _ensure_unique(items: tuple[InventoryItem, ...], kind: str) -> None:
    seen: set[tuple[str, str]] = set()
    for item in items:
        key = (item.identity, item.version)
        if key in seen:
            raise ValueError(f"duplicate {kind} identity {item.identity}@{item.version}")
        seen.add(key)


def discover_inventory(root: Path = ROOT) -> Inventory:
    modules = tuple(
        sorted(
            (
                _inventory_item(path, id_key="module_id", root=root)
                for path in root.glob("modules/**/module.yaml")
            ),
            key=lambda item: (item.identity, item.version),
        )
    )
    profiles = tuple(
        sorted(
            (
                _inventory_item(path, id_key="profile_id", root=root)
                for path in root.glob("profiles/**/profile.yaml")
            ),
            key=lambda item: (item.identity, item.version),
        )
    )
    schemas = tuple(
        sorted(path.relative_to(root).as_posix() for path in (root / "schemas").glob("*.json"))
    )
    if not modules:
        raise ValueError("no shipped PAM modules were discovered")
    if not profiles:
        raise ValueError("no shipped PAM profiles were discovered")
    if not schemas:
        raise ValueError("no PAM schemas were discovered")
    _ensure_unique(modules, "module")
    _ensure_unique(profiles, "profile")
    return Inventory(modules=modules, profiles=profiles, schemas=schemas)


def _item_lines(items: tuple[InventoryItem, ...]) -> list[str]:
    return [
        f"- `{item.identity}@{item.version}` — {item.title} (`{item.path}`)" for item in items
    ]


def render_readme_block(state: RepositoryState, inventory: Inventory) -> str:
    lines = [
        README_START,
        "## Current shipped methodology",
        "",
        "> This section is generated from `docs/repository-state.json` and the live "
        "module/profile/schema files. Run `make docs-sync` after changing those inputs; CI runs "
        "`make docs-check` and fails on drift.",
        "",
        f"- Landed methodology: **{state.label}** ({state.status}).",
        f"- v0.2 landing merge: `{state.landing_merge_commit}`.",
        f"- Frozen tested methodology revision: `{state.frozen_tested_revision}`.",
        f"- Stability: **{state.stability_level}**. {state.consumer_rule}",
        f"- Reference source/adopter: `{state.source_adopter}`. {state.reference_boundary}",
        "",
        f"### Shipped modules ({len(inventory.modules)})",
        "",
        *_item_lines(inventory.modules),
        "",
        f"### Routing profiles ({len(inventory.profiles)})",
        "",
        *_item_lines(inventory.profiles),
        "",
        f"### Contract schemas ({len(inventory.schemas)})",
        "",
        *[f"- `{path}`" for path in inventory.schemas],
        "",
        "### Reproducible quick start",
        "",
        "Pin the exact tested methodology revision rather than relying on a mutable branch:",
        "",
        "```bash",
        "git fetch origin a10ad56b7088c1e101e80914a9e00357dbef9120",
        "git checkout --detach a10ad56b7088c1e101e80914a9e00357dbef9120",
        "python -m pip install -e '.[dev]'",
        "python -m scripts.pam_validate examples/PROJECT_ASSURANCE.example.json",
        "python -m scripts.pam_handoff examples/HANDOFF_STATE.example.json",
        "python -m scripts.pam_bootstrap examples/BOOTSTRAP_ACQUISITION.example.json",
        "```",
        "",
        "An adopting project owns its project facts, selected profiles, requirement/evidence state, "
        "bootstrap record, and current handoff. PAM supplies the versioned methodology contracts and "
        "deterministic validators; it is not an adopter runtime dependency.",
        README_END,
    ]
    return "\n".join(lines)


def render_architecture_block(state: RepositoryState, inventory: Inventory) -> str:
    lines = [
        ARCH_START,
        "## Current repository inventory",
        "",
        "> Generated from the shipped module/profile/schema files. This inventory describes landed "
        "repository state, not roadmap candidates or unmerged pull requests.",
        "",
        f"Methodology status: **{state.label}** ({state.status}); frozen tested revision "
        f"`{state.frozen_tested_revision}`.",
        "",
        "### Modules",
        "",
        *_item_lines(inventory.modules),
        "",
        "### Profiles",
        "",
        *_item_lines(inventory.profiles),
        "",
        "### Schemas",
        "",
        *[f"- `{path}`" for path in inventory.schemas],
        ARCH_END,
    ]
    return "\n".join(lines)


def synchronized_text(text: str, *, start: str, end: str, anchor: str, block: str) -> str:
    start_count = text.count(start)
    end_count = text.count(end)
    if start_count != end_count or start_count > 1:
        raise ValueError(f"markers {start!r}/{end!r} must be absent or appear exactly once")
    if start_count == 1:
        start_index = text.index(start)
        end_index = text.index(end, start_index) + len(end)
        replacement = block
        if end_index < len(text) and text[end_index] == "\n":
            replacement += "\n"
            end_index += 1
        return text[:start_index] + replacement + text[end_index:]
    if anchor not in text:
        raise ValueError(f"missing documentation insertion anchor {anchor!r}")
    return text.replace(anchor, f"{block}\n\n{anchor}", 1)


def expected_documents(root: Path = ROOT) -> dict[Path, str]:
    state = load_state(root)
    inventory = discover_inventory(root)
    targets = {
        Path("README.md"): (
            README_START,
            README_END,
            "## Intended flow",
            render_readme_block(state, inventory),
        ),
        Path("docs/ARCHITECTURE.md"): (
            ARCH_START,
            ARCH_END,
            "## Module",
            render_architecture_block(state, inventory),
        ),
    }
    expected: dict[Path, str] = {}
    for path, (start, end, anchor, block) in targets.items():
        full_path = root / path
        if not full_path.is_file():
            raise ValueError(f"missing documentation target {path}")
        current = full_path.read_text(encoding="utf-8")
        expected[path] = synchronized_text(
            current, start=start, end=end, anchor=anchor, block=block
        )
    return expected


def sync_documents(root: Path = ROOT, *, write: bool) -> list[str]:
    stale: list[str] = []
    for relative_path, expected in expected_documents(root).items():
        path = root / relative_path
        current = path.read_text(encoding="utf-8")
        if current == expected:
            continue
        stale.append(relative_path.as_posix())
        if write:
            path.write_text(expected, encoding="utf-8")
    return stale


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Synchronize PAM repository inventory and release metadata into public docs."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail when generated docs are stale.")
    mode.add_argument("--write", action="store_true", help="Rewrite generated documentation blocks.")
    args = parser.parse_args()
    write = bool(args.write)
    stale = sync_documents(write=write)
    if bool(args.check) and stale:
        paths = "\n- ".join(stale)
        raise SystemExit(
            "PAM generated documentation is stale; run `make docs-sync` and commit the result:\n- "
            + paths
        )
    if write:
        if stale:
            print("synchronized PAM documentation: " + ", ".join(stale))
        else:
            print("PAM documentation already synchronized")
    else:
        print("PAM documentation synchronization: PASS")


if __name__ == "__main__":
    main()
