import pandas as pd
import mlflow

from dagster import op
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


@op
def split_data(context, data_df: pd.DataFrame) -> dict:
    context.log.info(f"{len(data_df)} records received.")
    train, test = train_test_split(data_df, test_size=context.op_config["test_size"])
    context.log.info(
        f"The training data set contains {len(train)} entries, the test data set {len(test)}."
    )
    train_x = train.iloc[:, :-1]
    train_y = train.iloc[:, -1]
    test_x = train.iloc[:, :-1]
    test_y = train.iloc[:, -1]
    return {"train_x": train_x, "train_y": train_y, "test_x": test_x, "test_y": test_y}


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
