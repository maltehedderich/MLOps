# MLOps in the Cloud

This project was created within the context of the master's thesis "MLOps in the Cloud: Components, Patterns & Best Practices". The project serves as an example of the application of the best practices developed on the HashiCorp stack.

## Installation

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

TBD

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

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
