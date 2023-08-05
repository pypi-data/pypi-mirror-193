import pandas as pd
from xgboost import XGBRegressor


def evaluate(
    estimator: XGBRegressor, samples: pd.DataFrame, targets: pd.Series
) -> float:
    """
    A XGBRegressor gets evaluated on a DataFrame of samples and a corresponding Series of targets
    """
    return estimator.score(samples, targets)
