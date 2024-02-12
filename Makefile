.DEFAULT_GOAL = help

help:
	@echo "-------------------------------HELP-------------------------------"
	@echo
	@echo "- make app: Starts with Dash App."
	@echo "- make docs: Open the browser and load the documentation."
	@echo "- make interrogate: To check documentation coverage type."
	@echo "- make linters: To check the code formatting."
	@echo "- make pre-commit: Performs compliance checking of commits."
	@echo "- make run: Run Application"
	@echo "- make test: To test the project type."
	@echo
	@echo "------------------------------------------------------------------"

.PHONY: app
app:
	python -m pylegends.dash.app

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

.PHONY: run
run:
	python -m jobs.job_riot

.PHONY: test
test:
	poetry run pytest -vv
