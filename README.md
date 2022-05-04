# MLOps in the Cloud

This project was created within the context of the master's thesis "MLOps in the Cloud: Components, Patterns & Best Practices". The project serves as an example of the application of the best practices.

## Installation

The easiest way to install the necessary components on MacOS and Linux is via [Homebrew](https://brew.sh/).

`brew install protobuf`

### apt installations

`sudo apt install cmake libprotobuf-dev protobuf-compiler build-essential`

### Installation of HashiCorp Stack

The easiest way to install the necessary components on MacOS and Linux is via [Homebrew](https://brew.sh/).

The first step is to add the HashiCorp repository to Homebrew.

```bash
  brew tap hashicorp/tap
```

Nomad, the workload orchestrator to deploy and manage applications, can then be installed using the following command.

```bash
  brew install hashicorp/tap/nomad
```

Nomad updates can be realised later via the following command.

```bash
  brew upgrade hashicorp/tap/nomad
```

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

## Acknowledgements

TBD

- []()
