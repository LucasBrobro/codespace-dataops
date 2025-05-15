# Dockerfile
FROM apache/airflow:2.5.0

USER root

# Install required system packages
RUN apt-get update && apt-get install -y gcc build-essential

USER airflow

# Upgrade pip and install dependencies (sans protobuf conflict)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
        dbt-postgres==1.5.2 \
        great-expectations==0.15.46 \
        nbformat>=5.1.0 \
        openpyxl