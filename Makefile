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

check: lint format type validate test
