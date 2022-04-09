# 03. Training - Continuous Training

With the help of the artifacts from the previous step, a continuous training process is enabled in this step. Depending on the requirement, this is either carried out at time intervals or alternatively based on a trigger, such as the availability of new data. The steps for this are similar to those for Orchestrated Experiments, but the output here is the trained model rather than the source code for training. This similarity is important to keep the development and production environment as comparable as possible to avoid unexpected errors.

## Pipeline Steps

**Input**: Training Dataset

    1. Data Extraction
    2. Data Validation
    3. Data Preperation
    4. Model Training
    5. Model Evaluation
    6. Model Validation

**Output**: Trained Models in Model Registry

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
