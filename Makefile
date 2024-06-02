.PHONY: test
test:
	poetry run python -m pytest tests/

.PHONY: build
build:
	poetry build


.PHONY: coverage
coverage:
	poetry run coverage run -m pytest tests/


.PHONY: coverage-report
coverage-report: coverage;
	poetry run coverage report -m


.PHONY: cleancode
cleancode:
	isort .
	black .
	mypy .