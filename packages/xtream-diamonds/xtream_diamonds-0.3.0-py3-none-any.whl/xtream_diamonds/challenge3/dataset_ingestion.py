import pandas as pd
from typing import List, Dict
from functools import reduce
from .categorical_mappings import mappings


def _read_dataset(path: str) -> pd.DataFrame:
    """Read dataset from csv"""
    return pd.read_csv(path)


def _convert_to_ordinal(
    dataset: pd.DataFrame, feature_map: Dict[str, int]
) -> pd.DataFrame:
    """Convert a categorical feature to ordinal in a given dataset"""
    return dataset.replace(feature_map)


def _convert_all_to_ordinal(
    dataset: pd.DataFrame, feature_maps: List[Dict[str, int]]
) -> pd.DataFrame:
    """Convert a list of categorical features to ordinal in a given dataset"""
    return reduce(_convert_to_ordinal, feature_maps, dataset)


def _clean(dataset: pd.DataFrame):
    """
    Cleans a diamonds' dataset:
    - drops all diamonds with a price less than 0
    - drop all diamonds with x, y, z equals to 0
    """
    # remove diamonds with price <= 0
    cleaned_dataset = dataset.drop(dataset[dataset.price <= 0].index)

    # remove diamonds with x, y or z equal to 0
    cleaned_dataset = cleaned_dataset.drop(
        cleaned_dataset[
            (cleaned_dataset["x"] == 0)
            | (cleaned_dataset["y"] == 0)
            | (cleaned_dataset["z"] == 0)
        ].index
    )
    return cleaned_dataset


def prepare(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Prepares the dataset to be fed to a tree-based regression model:
    - x, y, z are dropped because they are correlated among themselves and with carat
    - categorical features are converted to ordinal integers
    No normalization is carried out because tree-based algorithms do not need it.

    """
    # remove correlated features
    prepared_dataset = dataset.drop(["x", "y", "z"], axis=1)

    # convert ordinal values to numeric
    prepared_dataset = _convert_all_to_ordinal(prepared_dataset, mappings)

    return prepared_dataset


def ingest(path: str) -> pd.DataFrame:
    """
    Dataset ingestion pipeline:
    - read dataset from file
    - clean dataset from bad samples
    - prepare dataset for training
    """
    dataset = _read_dataset(path)

    cleaned_dataset = _clean(dataset)

    prepared_dataset = prepare(cleaned_dataset)

    return prepared_dataset
