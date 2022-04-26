import pandas as pd

from dagster import op


@op
def download_dataset(context) -> pd.DataFrame:
    data = pd.read_csv(context.op_config["url"], sep=";")
    context.log.info(
        f"Read {len(data)} lines with {len(data.columns)-1} features from {context.op_config['url']}"
    )
    return data
