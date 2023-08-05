from typing import Dict
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
from numpy.typing import ArrayLike
from xgboost import XGBRegressor


def train(
    samples: pd.DataFrame,
    targets: pd.Series,
    seed: int,
) -> XGBRegressor:
    """
    Trains a XGBRegressor on a training set.
    Takes a DataFrame of samples, a Series of targets and a seed for reproducibility.
    The model is trained through a randomized search with cross validation on the hyperparameter space.
    """
    regressor = XGBRegressor(random_state=seed)

    hyperparameters = {
        # learning rate
        "eta": np.geomspace(0.1, 1, endpoint=False),
        # L1 regularization
        "alpha": np.linspace(0, 1),
        # L2 regularization
        "lambda": np.linspace(0, 1),
        # subsample rate prior to growing the trees
        "subsample": np.linspace(0.1, 1),
        # max_depth set low for interpretability
        "max_depth": [3],
        # number of trees (preferring lower estimators solutions)
        "n_estimators": list(range(1, 10)),
    }

    hyperparameter_search = RandomizedSearchCV(
        regressor,
        hyperparameters,
        scoring="r2",
        cv=3,
        n_iter=500,
        verbose=3,
        random_state=0,
    )

    hyperparameter_search.fit(samples, targets)
    return hyperparameter_search.best_estimator_
