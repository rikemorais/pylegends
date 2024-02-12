.DEFAULT_GOAL = help

help:
	@echo "-------------------------------HELP-------------------------------"
	@echo
	@echo "- make docs: Open the browser and load the documentation."
	@echo "- make interrogate: To check documentation coverage type."
	@echo "- make linters: To check the code formatting."
	@echo "- make pre-commit: Performs compliance checking of commits."
	@echo "- make test: To test the project type."
	@echo
	@echo "------------------------------------------------------------------"

.PHONY: docs
docs:
	open http://127.0.0.1:8000/
	mkdocs serve

.PHONY: interrogate
interrogate:
	interrogate -v ./

.PHONY: linters
linters:
	isort .
	black .
	poetry run python -m flake8 ./ --extend-exclude=dist,build --show-source --statistics

.PHONY: pre-commit
pre-commit:
	pre-commit run --all-files

.PHONY: test
test:
	poetry run pytest -vv
