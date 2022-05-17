import pandas as pd
import numpy as np

from mlflow.models.signature import ModelSignature
from mlflow.types.schema import Schema, ColSpec, DataType
from scipy import stats
from dagster import op
from sklearn.model_selection import train_test_split


@op
def download_dataset(context) -> pd.DataFrame:
    data = pd.read_csv(context.op_config["url"], sep=";")
    context.log.info(
        f"Read {len(data)} lines with {len(data.columns)-1} features from {context.op_config['url']}"
    )
    return data


@op
def get_signature(df: pd.DataFrame) -> ModelSignature:
    dtypes = [dtype.to_pandas() for dtype in DataType]
    schema_list = []
    for name, dtype in zip(df.columns, df.dtypes):
        type_index = dtypes.index(dtype) + 1
        schema_list.append(ColSpec(DataType(type_index), name))
    input_schema = Schema(schema_list[:-1])
    output_schema = Schema([schema_list.pop()])
    signature = ModelSignature(input_schema, output_schema)
    return signature


@op
def remove_outliers(context, data_df: pd.DataFrame) -> pd.DataFrame:
    data_x = data_df.iloc[:, :-1]
    z_scores = stats.zscore(data_x)
    # use absolute z-score to include negative and positive outliers
    data_filter = (np.abs(z_scores) < 3).all(axis=1)
    context.log.info(
        f"{data_filter.value_counts()[0]} lines with outliers were removed. {data_filter.value_counts()[1]} lines remain."
    )
    return data_df[data_filter]


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
