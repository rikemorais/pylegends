#!/bin/bash

# Fail On Any Error
set -e

# Check if the Environment is Set to Development
if [ "$AIRFLOW_ENV" = "development" ]; then
    # Initialize the database (only in development)
    echo "Initializing Database..."
    airflow db init

    # Run Any Migrations Necessary
    echo "Running Migrations..."
    airflow db migrate

    # Create a Default User
    echo "Creating Default User..."
    airflow users create \
        --username admin \
        --firstname Airflow \
        --lastname Admin \
        --role Admin \
        --email admin@example.com \
        --password admin

    echo "Creating Variables..."
    airflow variables import $AIRFLOW_HOME/variables.json

    echo "Creating Connections..."
    airflow connections import $AIRFLOW_HOME/connections.json --overwrite
fi

if [ "$ISTIO_KILLER" = "true" ]; then
  # Gracefully Shutdown Istio Sidecar When Exiting
  trap "echo 'Exiting, calling quitquitquit'; curl --max-time 2 -s -f -XPOST http://127.0.0.1:15000/quitquitquit" EXIT

  # Wait for Istio to be ready
  while ! curl -s -f http://127.0.0.1:15020/healthz/ready; do
    echo "Waiting Istio to be Ready."
    sleep 1
  done

  sleep 2

  # Function to forward signals to the child process
  forward_signals() {
    child_pid=$!
    trap "kill -TERM $child_pid" SIGTERM
    trap "kill -HUP $child_pid" SIGHUP
    wait $child_pid
  }

  "$@" &
    forward_signals
else
  exec "$@"
fi
