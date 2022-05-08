from dagster_repo.example.publish_to_triton.convert_to_onnx import (
    load_sklearn_model,
    sklearn_to_onnx,
    publish_to_mlflow,
)
from dagster import config_from_files, file_relative_path, graph
from dagster_mlflow import end_mlflow_on_run_finished, mlflow_tracking
from dagster_repo.example.publish_to_triton.deploy_to_triton import deploy_to_triton


@end_mlflow_on_run_finished
@graph
def publish_sklearn():
    deploy_to_triton(publish_to_mlflow(sklearn_to_onnx(load_sklearn_model())))


publish_sklearn_job = publish_sklearn.to_job(
    config=config_from_files([file_relative_path(__file__, "run_config.yaml")]),
    resource_defs={"mlflow": mlflow_tracking},
)
