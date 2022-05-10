import pandas as pd
import mlflow
import boto3
import shutil
from pathlib import Path
from time import sleep
from dagster import op

from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import DataframeInput
from bentoml.frameworks.sklearn import SklearnModelArtifact


def service_factory(class_name: str, env_params: dict, artifacts_list: list):
    @env(**env_params)
    @artifacts(artifacts_list)
    class NewClass(BentoService):
        @api(input=DataframeInput(), batch=True)
        def predict(self, df: pd.DataFrame):
            return self.artifacts.model.predict(df)

    NewClass.__name__ = class_name
    return NewClass


@op(required_resource_keys={"mlflow"})
def load_mlflow_model(context):
    model_uri = context.op_config["model_uri"]
    context.log.info(f"Retrieving Model: {model_uri}.")
    model = mlflow.sklearn.load_model(model_uri)
    return model


@op
def pack_model(context, model):
    service_class = service_factory(
        context.op_config["service_name"],
        {"infer_pip_packages": True},
        [SklearnModelArtifact("model")],
    )
    context.log.info(f"Created service class {service_class.__name__}")
    service = service_class()
    service.pack("model", model)
    saved_path = service.save()
    context.log.info(f"Saved prediction service in {saved_path}")
    return Path(saved_path)


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
    sleep(120)
