from dagster import Nothing, graph, op
from minio import Minio


@op
def make_buckets(context) -> Nothing:
    context.log.info(context.op_config["minio_endpoint"])
    client = Minio(
        context.op_config["minio_endpoint"],
        context.op_config["minio_access_key"],
        context.op_config["minio_secret_key"],
        secure=False,
    )
    for bucket_name in context.op_config["bucket_names"]:
        if client.bucket_exists(bucket_name):
            context.log.info(f"Bucket {bucket_name} already exists.")
        else:
            client.make_bucket(bucket_name)
            context.log.info(f"Bucket {bucket_name} created.")


@graph
def create_buckets():
    make_buckets()


create_buckets_test_job = create_buckets.to_job(
    config={
        "ops": {
            "make_buckets": {
                "config": {
                    "bucket_names": ["mlflow"],
                    "minio_endpoint": "localhost:9000",
                    "minio_access_key": "minio_user",
                    "minio_secret_key": "minio_password",
                },
            },
        }
    }
)

create_buckets_dev_job = create_buckets.to_job(
    config={
        "ops": {
            "make_buckets": {
                "config": {
                    "bucket_names": ["mlflow"],
                    "minio_endpoint": "minio:9000",
                    "minio_access_key": "minio_user",
                    "minio_secret_key": "minio_password",
                },
            },
        }
    }
)

if __name__ == "__main__":
    # start_presets_main
    result = create_buckets_test_job.execute_in_process()
    # end_presets_main
    assert result.success
