import mlflow

from dagster import op
from sklearn.ensemble import RandomForestClassifier
from mlflow.models.signature import ModelSignature


@op(required_resource_keys={"mlflow"})
def train_rfc(
    context, data_dict: dict, signature: ModelSignature
) -> RandomForestClassifier:
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
        registered_model_name="wine-rfc",
        signature=signature,
    )
    return rfc
