SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy pyleetcode_utils tests
	poetry run flake8 .

.PHONY: lint-docs
lint-docs:
	if poetry run command -v doc8 > /dev/null 2>&1; then poetry run doc8 -q docs; fi

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
