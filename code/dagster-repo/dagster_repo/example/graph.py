from dagster_repo.example import (
    data_collection,
    feature_engineering,
    training,
    evaluate,
)
from dagster import config_from_files, file_relative_path, graph
from dagster_mlflow import end_mlflow_on_run_finished, mlflow_tracking


@end_mlflow_on_run_finished
@graph
def wine_rfc():
    data_dict = training.split_data(
        feature_engineering.remove_outliers(data_collection.download_dataset())
    )
    rfc = training.train_rfc(data_dict)
    evaluate.evaluate_rfc(data_dict, rfc)


wine_rfc_test_job = wine_rfc.to_job(
    config={
        "ops": {
            "download_dataset": {
                "config": {
                    "url": "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
                }
            },
            "split_data": {"config": {"test_size": 0.5}},
            "train_rfc": {"config": {"n_estimators": 50, "max_depth": 10}},
        },
        "resources": {
            "mlflow": {
                "config": {
                    "experiment_name": "test_wine_rfc",
                    "mlflow_tracking_uri": "http://localhost:4000",
                    # env variables to pass to mlflow
                    "env": {
                        "MLFLOW_S3_ENDPOINT_URL": "http://localhost:9000",
                        "AWS_ACCESS_KEY_ID": "minio_user",
                        "AWS_SECRET_ACCESS_KEY": "minio_password",
                    },
                }
            }
        },
    },
    resource_defs={"mlflow": mlflow_tracking},
)

wine_rfc_dev_job = wine_rfc.to_job(
    config=config_from_files([file_relative_path(__file__, "run_config.yaml")]),
    resource_defs={"mlflow": mlflow_tracking},
)

if __name__ == "__main__":
    # start_presets_main
    result = wine_rfc_test_job.execute_in_process()
    # end_presets_main
    assert result.success
