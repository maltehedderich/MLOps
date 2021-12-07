# 01. Training - Orchestrated Experimentation

This section structures the process for experimenting with new data or use cases. For this purpose, a pipeline for orchestrated experimentation is created.

This process defined by Google can also be divided into two separate processes. The first three process steps correspond to those of a data engineer who could make the fully processed data available in a feature store for further processing. The data scientists could then use this data for their models.

## Pipeline Steps

**Input**: Development Dataset

    1. Data Extraction
    2. Data Validation
    3. Data Preperation
    4. Model Training
    5. Model Evaluation
    6. Model Validation

**Output**: Source Code in Source Repository

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

TBD

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
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

- [An introduction to MLOps on Google Cloud](https://www.youtube.com/watch?v=6gdrwFMaEZ0)
