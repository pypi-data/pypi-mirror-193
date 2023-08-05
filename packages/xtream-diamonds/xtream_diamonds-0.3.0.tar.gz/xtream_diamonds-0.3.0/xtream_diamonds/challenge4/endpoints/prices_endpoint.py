from ..model import get_model
from ..diamond import Diamond
from ...challenge3.dataset_ingestion import prepare
import pandas as pd
from fastapi import APIRouter

router = APIRouter()


@router.post("/prices")
async def get_price(diamond: Diamond) -> float:
    """
    Diamond pricing endpoint.
    Receives a diamond and returns its price by querying the trained model
    """
    model = get_model()
    if model is None:
        raise Exception("Please load the model during startup")

    diamond_dataframe = pd.DataFrame(dict(diamond), index=[0])

    return model.predict(prepare(diamond_dataframe))
