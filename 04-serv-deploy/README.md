# 04. Serving - Model Deployment CI/CD

In the following, the trained model together with the source code will be used to deploy services in production. Here it is important to implement additional tests (for latency requirements etc.) and release gates. These should ensure that the new model really outperforms the one currently used in production and meets the quality standards.

## Pipeline Steps

    - **Input**: Source Code and Trained Model

    1. Build Prediction Serivce
    2. Run Automated Tests
    3. Deploy to Target Environment

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
