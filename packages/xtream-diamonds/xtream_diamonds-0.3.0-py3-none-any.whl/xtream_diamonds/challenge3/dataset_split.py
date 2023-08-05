import pandas as pd
from typing import Tuple
from sklearn.model_selection import train_test_split


def split(
    dataset: pd.DataFrame, target: str, test_size: float, seed: int
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """
    Split a dataset in train and test with a given test size and a fixed seed for reproducibility.
    The train and test set are then split in a samples DataFrame and a corresponding target
    """
    training_set, test_set = train_test_split(
        dataset, test_size=test_size, random_state=seed
    )
    samples_train = training_set.drop([target], axis=1)
    targets_train = training_set[target]
    samples_test = test_set.drop([target], axis=1)
    targets_test = test_set[target]
    return samples_train, targets_train, samples_test, targets_test
