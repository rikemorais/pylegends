default: build

help:
	@echo "-------------------------------HELP-------------------------------"
	@echo
	@echo "- make build: Creates the local environment."
	@echo "- make run: Builds (if necessary) and starts the services defined in the Docker Compose file."
	@echo "- make check-services: Checks if the necessary Docker services are running."
	@echo "- make bootstrap: Performs the bootstrap process."
	@echo "- make jupyter: Builds and runs the Jupyter notebook container."
	@echo "- make linter: To check the code formatting."
	@echo
	@echo "------------------------------------------------------------------"

build:
	@docker compose build

run: build
	@docker compose up

check-services:
	@echo "Checking if services are running..."
	@docker compose ps | grep 'Up' > /dev/null 2>&1 || (echo "Error: Services are not running. Please start services using 'make run'." && exit 1)
	@echo "Services are running."

bootstrap: check-services
	@echo "Running the bootstrap process..."
	@docker compose exec airflow python3 tests/fixtures/bootstrap_files.py

jupyter: check-services
	@docker build --build-arg="AIRFLOW_DOCKER_IMAGE=rikemorais/pylegends:latest" -t jupyter-notebook:latest -f Dockerfile-Jupyter .
	@echo "Starting Jupyter notebook..."
	@docker run --rm -p 8888:8888 --network=$(shell basename "$(PWD)")_default -v ./dags:/opt/airflow/dags -v ./plugins:/opt/airflow/plugins -v ./spark:/opt/airflow/spark -v ./tests:/opt/airflow/tests -v ./tmp/jupyter:/opt/jupyter -v ./config/spark-defaults-dev.conf:/opt/spark/conf/spark-defaults.conf --env AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow jupyter-notebook:latest

# Define Phony Targets
.PHONY: linter
linter:
	black .
	isort .
	flake8 .