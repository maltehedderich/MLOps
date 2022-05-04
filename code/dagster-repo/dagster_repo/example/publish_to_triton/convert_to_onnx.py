import mlflow
from dagster import Nothing, op
from sklearn.base import ClassifierMixin
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from onnx.onnx_ml_pb2 import ModelProto


@op
def load_sklearn_model(context) -> ClassifierMixin:
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
def publish_to_mlflow(context, onnx_model) -> Nothing:
    mlflow.onnx.log_model(
        onnx_model,
        "triton",
        registered_model_name=context.op_config["registered_model_name"],
    )
