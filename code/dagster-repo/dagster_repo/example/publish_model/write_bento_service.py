import mlflow
import boto3
import shutil
import importlib
import os
from pathlib import Path
from dagster import op


def service_factory(class_name: str, env_params: dict):
    module = Path("bento_service")
    os.makedirs(module)
    open(module / "__init__.py", "a").close()
    lines = [
        "import pandas as pd\n",
        "from bentoml import env, artifacts, api, BentoService\n",
        "from bentoml.adapters import JsonInput\n",
        "from bentoml.frameworks.sklearn import SklearnModelArtifact\n",
        f"env_params = {env_params}\n",
        "@env(**env_params)\n",
        "@artifacts([SklearnModelArtifact('model')])\n",
        f"class {class_name}(BentoService):\n",
        "    @api(input=JsonInput(), batch=True)\n",
        "    def predict(self, model_input):\n",
        "        return self.artifacts.model.predict(model_input)\n",
    ]
    with open(module / "service_class.py", "w") as file:
        file.writelines(lines)


@op(required_resource_keys={"mlflow"})
def load_model(context):
    model_uri = context.op_config["model_uri"]
    context.log.info(f"Retrieving Model: {model_uri}.")
    model = mlflow.sklearn.load_model(model_uri)
    return model


@op
def create_service(context):
    service_name = context.op_config["service_name"]
    service_factory(service_name, {"infer_pip_packages": True})
    context.log.info(f"Created service_class.py with class {service_name}")
    return service_name


@op
def pack_model(
    context,
    model,
    service_name,
):
    module = importlib.import_module("bento_service.service_class")
    service_class = getattr(module, service_name)
    service = service_class()
    service.pack("model", model)
    saved_path = Path(service.save())
    context.log.info(f"Saved prediction service in {saved_path}")
    with open(saved_path / "python_version", "w") as file:
        file.write(context.op_config["python_version"])
    return saved_path


@op
def zip_service(context, saved_path):
    output_name = "-".join(saved_path.parts[-2:])
    context.log.info(f"Creating Zip File for {saved_path}")
    zip_name = shutil.make_archive(output_name, "zip", saved_path.parent)
    context.log.info(f"Created Zip File {zip_name}")
    return zip_name


@op
def upload_service(context, zip_name):
    client = boto3.resource("s3", endpoint_url=context.op_config["s3_endpoint"])
    client.Bucket(context.op_config["bucket_name"]).upload_file(
        zip_name, zip_name.split("/")[-1]
    )
