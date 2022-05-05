FROM python:3.9.12

ARG MLFLOW_POSTGRES_USER
ARG MLFLOW_POSTGRES_PASSWORD
ARG MLFLOW_POSTGRES_DB
ARG MLFLOW_S3_ENDPOINT_URL
ARG MINIO_BUCKET_NAME
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

ENV MLFLOW_POSTGRES_URI="postgresql://${MLFLOW_POSTGRES_USER}:${MLFLOW_POSTGRES_PASSWORD}@mlflow_postgres:5432/${MLFLOW_POSTGRES_DB}"

# install mlflow
RUN apt update && apt install -y python3-pip python3-setuptools git
RUN pip3 install psycopg2-binary mlflow

# install MLflow Triton plugin
RUN mkdir triton-server
RUN git clone https://github.com/triton-inference-server/server.git /triton-server
WORKDIR /triton-server/deploy/mlflow-triton-plugin/
RUN python3 setup.py install

WORKDIR /
RUN rm -rf /triton-server

ENTRYPOINT mlflow server --host "0.0.0.0" --port "4000" --backend-store-uri $MLFLOW_POSTGRES_URI --default-artifact-root "S3://mlflow" 