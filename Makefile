.PHONY: lint format type test validate docs-sync docs-check check

lint:
	ruff check scripts tests

format:
	ruff format --check --diff scripts tests

type:
	mypy scripts tests

test:
	python -m pytest -q

validate:
	python -m scripts.pam_validate examples/PROJECT_ASSURANCE.example.json
	python -m scripts.pam_reuse examples/REUSE_ASSESSMENT.example.json
	python -m scripts.pam_handoff examples/HANDOFF_STATE.example.json
	python -m scripts.pam_handoff examples/HANDOFF_STATE.v0.2.example.json
	python -m scripts.pam_bootstrap examples/BOOTSTRAP_ACQUISITION.example.json

docs-sync:
	python -m scripts.sync_repository_docs --write

docs-check:
	python -m scripts.sync_repository_docs --check

check: lint format type validate docs-check test
