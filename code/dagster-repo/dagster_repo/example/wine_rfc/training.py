import mlflow

from dagster import op
from sklearn.ensemble import RandomForestClassifier


@op(required_resource_keys={"mlflow"})
def train_rfc(context, data_dict: dict) -> RandomForestClassifier:
    params = {
        "n_estimators": context.op_config["n_estimators"],
        "max_depth": context.op_config["max_depth"],
    }

    rfc = RandomForestClassifier(**params)
    rfc.fit(data_dict["train_x"], data_dict["train_y"])

    score = rfc.score(data_dict["test_x"], data_dict["test_y"])

    mlflow.log_params(params)
    mlflow.log_metrics({"Mean Accuracy": score})
    mlflow.sklearn.log_model(
        sk_model=rfc,
        artifact_path="sklearn-model",
        registered_model_name="wine_rfc",
    )
    return rfc
