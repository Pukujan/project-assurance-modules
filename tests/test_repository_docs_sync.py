from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from scripts.sync_repository_docs import (
    README_END,
    README_START,
    discover_inventory,
    load_state,
    sync_documents,
    synchronized_text,
)


def _state() -> dict[str, object]:
    return {
        "schema_version": "pam-repository-state/1.0.0",
        "landed_methodology": {
            "label": "bounded PAM v0.2",
            "landing_merge_commit": "a" * 40,
            "frozen_tested_revision": "b" * 40,
            "status": "landed",
        },
        "stability": {
            "level": "pre-v1",
            "consumer_rule": "Pin an exact Git commit.",
        },
        "reference": {
            "source_adopter": "Pukujan/research-assurance",
            "boundary": "Reference source only.",
        },
    }


def _write_yaml(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


def _fixture(root: Path) -> None:
    (root / "docs").mkdir(parents=True)
    (root / "schemas").mkdir()
    (root / "docs/repository-state.json").write_text(json.dumps(_state()), encoding="utf-8")
    (root / "README.md").write_text("# PAM\n\n## Intended flow\n", encoding="utf-8")
    (root / "docs/ARCHITECTURE.md").write_text("# Architecture\n\n## Module\n", encoding="utf-8")
    (root / "schemas/module.schema.json").write_text("{}\n", encoding="utf-8")
    _write_yaml(
        root / "modules/example/module.yaml",
        {
            "schema_version": "pam-module/0.2.0",
            "module_id": "planning.example",
            "version": "0.1.0",
            "title": "Example module",
        },
    )
    _write_yaml(
        root / "profiles/example/profile.yaml",
        {
            "schema_version": "pam-profile/0.1.0",
            "profile_id": "projectization.example",
            "version": "0.1.0",
            "title": "Example profile",
        },
    )


def test_write_then_check_is_stable(tmp_path: Path) -> None:
    _fixture(tmp_path)

    assert sorted(sync_documents(tmp_path, write=True)) == [
        "README.md",
        "docs/ARCHITECTURE.md",
    ]
    assert sync_documents(tmp_path, write=False) == []

    readme = (tmp_path / "README.md").read_text(encoding="utf-8")
    assert "planning.example@0.1.0" in readme
    assert "projectization.example@0.1.0" in readme
    assert "schemas/module.schema.json" in readme


def test_inventory_change_makes_generated_docs_stale(tmp_path: Path) -> None:
    _fixture(tmp_path)
    sync_documents(tmp_path, write=True)

    _write_yaml(
        tmp_path / "modules/extra/module.yaml",
        {
            "schema_version": "pam-module/0.2.0",
            "module_id": "benchmark.extra",
            "version": "0.1.0",
            "title": "Extra module",
        },
    )

    assert sorted(sync_documents(tmp_path, write=False)) == [
        "README.md",
        "docs/ARCHITECTURE.md",
    ]


def test_manual_generated_edit_is_detected(tmp_path: Path) -> None:
    _fixture(tmp_path)
    sync_documents(tmp_path, write=True)
    readme = tmp_path / "README.md"
    readme.write_text(
        readme.read_text(encoding="utf-8").replace("bounded PAM v0.2", "stale release"),
        encoding="utf-8",
    )

    assert sync_documents(tmp_path, write=False) == ["README.md"]


def test_unpaired_markers_fail_closed() -> None:
    with pytest.raises(ValueError, match="must be absent or appear exactly once"):
        synchronized_text(
            f"# PAM\n{README_START}\nstale\n## Intended flow\n",
            start=README_START,
            end=README_END,
            anchor="## Intended flow",
            block=f"{README_START}\nfresh\n{README_END}",
        )


def test_duplicate_inventory_identity_fails_closed(tmp_path: Path) -> None:
    _fixture(tmp_path)
    _write_yaml(
        tmp_path / "modules/duplicate/module.yaml",
        {
            "schema_version": "pam-module/0.2.0",
            "module_id": "planning.example",
            "version": "0.1.0",
            "title": "Duplicate module",
        },
    )

    with pytest.raises(ValueError, match="duplicate module identity"):
        discover_inventory(tmp_path)


def test_unknown_repository_state_schema_fails_closed(tmp_path: Path) -> None:
    (tmp_path / "docs").mkdir()
    state = _state()
    state["schema_version"] = "pam-repository-state/9.9.9"
    (tmp_path / "docs/repository-state.json").write_text(json.dumps(state), encoding="utf-8")

    with pytest.raises(ValueError, match="schema_version"):
        load_state(tmp_path)
