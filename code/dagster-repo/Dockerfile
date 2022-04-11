FROM python:3.8
ENV POETRY_HOME=/opt/poetry POETRY_VIRTUALENVS_CREATE=false PYTHONPATH=/app


# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagit and dagster-daemon, and to load the DagsterInstance
COPY  code/dagster-repo/poetry.lock code/dagster-repo/pyproject.toml /app/
WORKDIR /app/
RUN curl -fsS -o get-poetry.py https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py && \
    python get-poetry.py -y && . $POETRY_HOME/env && \
    poetry install --no-dev --no-interaction --no-root
COPY code/dagster-repo/dagster_repo /app/dagster_repo

# Run dagster gRPC server on port 4000

EXPOSE 4000

# CMD allows this to be overridden from run launchers or executors that want
# to run other commands against your repository
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-f", "dagster_repo/repo.py"]