from dagster import Nothing, op
from mlflow.deployments import get_deploy_client
from mlflow.models.model import ModelInfo


@op
def deploy_to_triton(context, model_info: ModelInfo) -> Nothing:
    client = get_deploy_client("triton")
    context.log.info(f"Loading Model: {model_info}.")
    client.create_deployment(
        name=context.op_config["registered_model_name"],
        model_uri=context.op_config["model_uri"],
        flavor="onnx",
    )
