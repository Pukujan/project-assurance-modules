.PHONY: lint format type test validate check

lint:
	ruff check scripts tests

format:
	ruff format --check --diff scripts tests

type:
	mypy scripts tests

test:
	pytest -q

validate:
	python scripts/pam_validate.py examples/PROJECT_ASSURANCE.example.json

check: lint format type validate test
