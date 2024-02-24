ARG SPARK_DOCKER_IMAGE=rikemorais/spark
FROM ${SPARK_DOCKER_IMAGE}

USER root

ARG REQUIREMENTS_FILE=requirements.txt
ENV REQUIREMENTS_FILE=${REQUIREMENTS_FILE}

ENV SPARK_DOCKER_IMAGE=${SPARK_DOCKER_IMAGE}
ENV AIRFLOW_HOME=/opt/airflow

RUN mkdir -p ${AIRFLOW_HOME}

COPY requirements.txt ${AIRFLOW_HOME}
COPY $REQUIREMENTS_FILE ${AIRFLOW_HOME}

WORKDIR ${AIRFLOW_HOME}

RUN pip install --no-cache-dir -r ${REQUIREMENTS_FILE} --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.8.txt" && \
    rm -rf ~/.cache/pip

COPY entrypoint.sh /entrypoint.sh
COPY dags ${AIRFLOW_HOME}/dags
COPY plugins ${AIRFLOW_HOME}/plugins
COPY spark ${AIRFLOW_HOME}/spark
COPY tests ${AIRFLOW_HOME}/tests

ENV PYTHONPATH=${AIRFLOW_HOME}/spark:${AIRFLOW_HOME}/tests:${AIRFLOW_HOME}/plugins:$PYTHONPATH

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]