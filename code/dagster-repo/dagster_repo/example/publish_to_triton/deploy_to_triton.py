from pkgutil import ModuleInfo
from dagster import Nothing, op
from mlflow.deployments import get_deploy_client
from mlflow.models.model import ModelInfo


@op
def deploy_to_triton(context, model_info: ModelInfo) -> Nothing:
    client = get_deploy_client("triton")
    client.create_deployment(
        model_name=context.op_config["registered_model_name"],
        model_uri=model_info.model_uri,
        flavor="triton",
    )
