# MLOps in the Cloud

This project was created within the context of the master's thesis "Open Source MLOps: How to Productionize AI Solutions". The project serves as an example of the application of the best practices.

## Installation

All setup steps were carried out with Ubuntu 20.04. Other Linux distributions are most likely also compatible, while macOS and Windows require adaptations.

### Install build dependencies

#### Dependencies to install the Python project locally (optional)

If the python packages are intended to be use locally in addition to the Docker deployment, the following additional steps are necessary.

```bash
  sudo apt install cmake libprotobuf-dev protobuf-compiler build-essential libedit-dev
```

```bash
  curl https://pyenv.run | bash
  pyenv update
  pyenv install 3.9.12
```

#

### Installation of local dagster-repo

#### Install build requirements

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

#### Install python project

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

## Deployment

TBD

To deploy this project run

```bash
  npm run deploy
```

## Run Locally

Clone the project

```bash
  git clone git@github.com:MalteHe/MLOps.git
```

Run the nomad agent

```bash
  sudo nomad agent -dev -bind 0.0.0.0 -log-level INFO
```

Use another terminal session to discover the nomad agent

```bash
  nomad node status
```

Start the server

```bash
  npm run start
```

## Usage/Examples

```javascript
import Component from "my-project";

function App() {
  return <Component />;
}
```

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Authors

- [@MalteHe](https://github.com/MalteHe)

## Troubleshooting

### triton-server container not starting

```bash
error: creating server: Internal - Could not get MetaData for bucket with name triton due to exception: , error message: No response body.
```

The most common reason for this is that the configured model registry path is not accessible. If the example is used here, the bucket must first be accessed via Minio's web interface http://localhost:9000 or by executing the create bucket pipeline in dagster dagit http://localhost:3000. A subsequent restart of the triton-server container should solve the problem.

The run config for the create buckets pipeline shown below serves as an example.

```yml
ops:
  make_buckets:
    config:
      bucket_names:
        - mlflow
        - triton
        - dvc
      minio_access_key: minio_user
      minio_endpoint: minio:9000
      minio_secret_key: minio_password
```

### 'poetry install' error

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

## Acknowledgements

TBD

- []()
