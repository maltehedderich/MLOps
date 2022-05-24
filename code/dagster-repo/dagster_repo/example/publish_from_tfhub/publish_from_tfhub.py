from dagster_mlflow import end_mlflow_on_run_finished, mlflow_tracking
import tensorflow as tf
import tensorflow_hub as hub
import mlflow

from dagster import config_from_files, file_relative_path, graph, op
from mlflow.models.signature import infer_signature
from pathlib import Path


@op
def split_url(context):
    url = context.op_config["url"]
    url_parts = url.split("/")
    version = url_parts[-1]
    name = url_parts[-2]
    url_info = {"url": url, "name": name, "version": version}
    return url_info


@op
def download_model(context, url_info):
    save_path = Path(f'models/{url_info["name"]}/{url_info["version"]}')
    context.log.info(f"Save Path: {save_path}")
    model = hub.load(url_info["url"])
    example_input = context.op_config["example_input"]
    if example_input:
        signature = infer_signature([example_input], model(example_input))
    else:
        signature = None
    tf.saved_model.save(model, save_path, signatures=model.signatures)
    return {"save_path": save_path, "signature": signature}


@op(required_resource_keys={"mlflow"})
def log_model(context, model_info, url_info):
    model_name = f"{url_info['name']}-{url_info['version']}"
    mlflow.tensorflow.log_model(
        tf_saved_model_dir=model_info["save_path"],
        tf_meta_graph_tags=None,
        tf_signature_def_key="serving_default",
        signature=model_info["signature"],
        registered_model_name=model_name,
    )


@end_mlflow_on_run_finished
@graph
def tfhub():
    url_info = split_url()
    model_info = download_model(url_info)
    log_model(model_info, url_info)


tfhub_job = tfhub.to_job(
    config=config_from_files([file_relative_path(__file__, "run_config.yaml")]),
    resource_defs={"mlflow": mlflow_tracking},
)
