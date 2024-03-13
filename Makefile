SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy pyleetcode_utils tests
	poetry run flake8 .

.PHONY: lint-docs
lint-docs:
	poetry run doc8 -q docs

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check

.PHONY: test-local
test-local: lint package unit

.PHONY: test
test: lint lint-docs package unit
