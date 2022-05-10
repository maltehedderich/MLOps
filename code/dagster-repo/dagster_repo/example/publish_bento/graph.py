from dagster_repo.example.publish_bento.containerize_bento import build_image
from dagster_repo.example.publish_bento.write_bento_service import (
    load_mlflow_model,
    pack_model,
    upload_service,
    zip_service,
)
from dagster import config_from_files, file_relative_path, graph
from dagster_mlflow import end_mlflow_on_run_finished, mlflow_tracking


@end_mlflow_on_run_finished
@graph
def publish_bento():
    service_path = pack_model(load_mlflow_model())
    upload_service(zip_service(service_path))
    build_image(service_path)


publish_bento_job = publish_bento.to_job(
    config=config_from_files([file_relative_path(__file__, "run_config.yaml")]),
    resource_defs={"mlflow": mlflow_tracking},
)
