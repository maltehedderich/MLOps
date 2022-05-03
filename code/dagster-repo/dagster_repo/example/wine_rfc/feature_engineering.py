import pandas as pd
import numpy as np

from scipy import stats

from dagster import op


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
