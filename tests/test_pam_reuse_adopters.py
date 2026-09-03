from __future__ import annotations

from scripts.pam_core import ROOT, load_json
from scripts.pam_reuse import validate_reuse_assessment


def test_time_to_crawl_second_adopter_replay_passes_without_special_cases() -> None:
    assessment = load_json(ROOT / "fixtures" / "reuse" / "time-to-crawl-replay.json")
    validate_reuse_assessment(assessment, project_facts={"benchmark_or_dataset_use": False})
