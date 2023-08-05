from xgboost import XGBRegressor


def save(model: XGBRegressor, path: str) -> None:
    """
    Save a XGBRegressor to file, may be txt or json.
    """
    model.save_model(path)
