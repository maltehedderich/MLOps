# 06. Serving - Monitor Production

After the deployment in production, it is essential to continuously evaluate the model performance in order to be able to react appropriately in case of poor performance. Live data often differs significantly from training data and in many cases will change over time.

## Pipeline Steps

    - **Input**: Live Data

    1. Predict
    2. Explain
    3. Evaluate
    4. Monitor

    - **Output**: Performance and Event Logs in Log Store & Evaluations, Data Drif and Concept Drift Notifications in ML Metadata

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
