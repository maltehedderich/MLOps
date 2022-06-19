# Open Source MLOps

This project was created within the context of the master's thesis "Open Source MLOps: How to Unlock the Potential of Machine Learning". The project serves as additional validation step for the designed MLOps Architecture.

## Installation

All setup steps were carried out with Ubuntu 20.04. Other Linux distributions are most likely also compatible, while macOS and Windows require adaptations.

### Install Build Dependencies

#### Dependencies to Install the Python Project Locally (Optional)

If the python packages are intended to be use locally in addition to the Docker deployment, the following additional steps are necessary.

```bash
  sudo apt install cmake libprotobuf-dev protobuf-compiler build-essential libedit-dev libffi-dev
```

```bash
  curl https://pyenv.run | bash
  pyenv update
  pyenv install 3.10.4
```

### Installation of Local Dagster-Repo

#### Install Build Requirements

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

#### Install Python Project

```bash
  cd ./code/dagster-repo
```

Change directory to the dagster-repo root folder.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`COMPOSE_PROJECT_NAME`
`AWS_ACCESS_KEY_ID`
`AWS_SECRET_ACCESS_KEY`
`MINIO_BUCKET_NAME`
`MLFLOW_POSTGRES_USER`
`MLFLOW_POSTGRES_PASSWORD`
`MLFLOW_POSTGRES_DB`
`MLFLOW_S3_ENDPOINT_URL`
`MLFLOW_TRACKING_URI`
`DAGSTER_POSTGRES_USER`
`DAGSTER_POSTGRES_PASSWORD`
`DAGSTER_POSTGRES_DB`
`DAGSTER_CURRENT_IMAGE`

After the creation of your .env file run

```bash
docker-compose --profile mlflow --profile dagster up -d --build
```

### Default Login Credentials

- Minio
  - Username: minio_user
  - Password: minio_password
- Grafana
  - Username: admin
  - Password: admin

## Architecture Overview

![MLOps Architecture Overview](https://github.com/MalteHe/MLOps/blob/main/images/architecture.png?raw=true)

## Authors

- [@MalteHe](https://github.com/MalteHe)

## Troubleshooting

### 'poetry install' error

#### setuptools not available

```bash
    × python setup.py egg_info did not run successfully.
    │ exit code: 1
    ╰─> [1 lines of output]
        ERROR: Can not execute `setup.py` since setuptools is not available in the build environment.
        [end of output]
```

The reason for this is often an outdated setuptools version. The solution is an update:

```bash
  poetry run pip install setuptools --upgrade
```

#### ModuleNotFoundError: No module named '\_ctypes'

The reason for this is often that the 'libffi-dev' package was not installed at the time where the python environment where created.

```bash
  sudo apt install libffi-dev
  pyenv uninstall 3.10.4
  pyenv install 3.10.4
```
