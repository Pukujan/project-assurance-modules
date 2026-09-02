.PHONY: lint format type test validate check

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
	python -m scripts.pam_handoff examples/HANDOFF_STATE.example.json
	python -m scripts.pam_handoff examples/HANDOFF_STATE.v0.2.example.json
	python -m scripts.pam_bootstrap examples/BOOTSTRAP_ACQUISITION.example.json

check: lint format type validate test
