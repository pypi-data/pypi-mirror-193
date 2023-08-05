#!/usr/bin/env python3

from typing import Optional
from xgboost import XGBRegressor


_model: Optional[XGBRegressor] = None


def load_model(path: str) -> None:
    """Load the model from a json file"""
    global _model
    _model = XGBRegressor()
    _model.load_model(path)


def get_model() -> Optional[XGBRegressor]:
    """
    Get the model.
    If the model has not yet been loaded returns None
    """
    return _model
