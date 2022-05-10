import mlflow
from mlflow.models.model import ModelInfo
from dagster import op
from sklearn.base import ClassifierMixin
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from onnx.onnx_ml_pb2 import ModelProto


@op
def load_sklearn_model(context) -> ClassifierMixin:
    #    client = mlflow.tracking.MlflowClient()
    #    model = client.get_model_version(
    #        context.op_config["model_name"], context.op_config["model_version"]
    #    )
    model_uri = context.op_config["model_uri"]

    context.log.info(f"Loading Model: {model_uri}.")
    model = mlflow.sklearn.load_model(model_uri)
    return model


@op
def sklearn_to_onnx(context, sklearn_model) -> ModelProto:
    input_type = context.op_config["input_type"]
    if input_type == "float_input":
        initial_type = [("float_input", FloatTensorType([None, 11]))]
    else:
        context.log.error(f"Input Type {input_type} not defined.")
    onnx_model = convert_sklearn(sklearn_model, initial_types=initial_type)
    context.log.info(f"Output type {type(onnx_model)}")
    return onnx_model


@op
def publish_to_mlflow(context, onnx_model: ModelProto) -> ModelInfo:
    registered_model_name = context.op_config["registered_model_name"]
    model_info = mlflow.onnx.log_model(
        onnx_model,
        "onnx-model",
        registered_model_name=registered_model_name,
    )
    return model_info
