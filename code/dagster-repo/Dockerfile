FROM python:3.9.12
ENV POETRY_HOME=/opt/poetry POETRY_VIRTUALENVS_CREATE=false PYTHONPATH=/app CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=ON"

# Install poetry and do some cleanup afterwards
RUN apt-get update && apt-get install curl cmake libprotobuf-dev protobuf-compiler build-essential -y
RUN curl -fsS -o get-poetry.py https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py && \
    python get-poetry.py -y
RUN apt-get remove curl -y && rm -rf /var/lib/apt/lists/*

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagit and dagster-daemon, and to load the DagsterInstance
COPY  code/dagster-repo/poetry.lock code/dagster-repo/pyproject.toml /app/
WORKDIR /app/
RUN . $POETRY_HOME/env && poetry install --no-dev --no-interaction --no-root
COPY code/dagster-repo/dagster_repo /app/dagster_repo

# Run dagster gRPC server on port 4000

EXPOSE 4000

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-f", "dagster_repo/repo.py"]