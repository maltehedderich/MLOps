import pandas as pd

from dagster import Nothing, op

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


@op
def train_rfc(context, data_dict: dict) -> RandomForestClassifier:
    rfc = RandomForestClassifier(
        n_estimators=context.op_config["n_estimators"],
        max_depth=context.op_config["max_depth"],
    )
    rfc.fit(data_dict["train_x"], data_dict["train_y"])
    return rfc


@op
def evaluate_rfc(context, data_dict: dict, rfc: RandomForestClassifier) -> Nothing:
    test_score = rfc.score(data_dict["test_x"], data_dict["test_y"])
    context.log.info(
        f"The mean accuracy on the given test data and labels is {test_score}."
    )
