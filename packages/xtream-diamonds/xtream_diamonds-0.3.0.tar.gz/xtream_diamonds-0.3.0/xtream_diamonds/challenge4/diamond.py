from typing import Literal
from pydantic import BaseModel, StrictFloat


CLARITY = Literal["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"]

CUT = Literal["Ideal", "Premium", "Very Good", "Good", "Fair"]

COLORLESS = Literal["D", "E", "F"]
NEAR_COLORLESS = Literal["G", "H", "I", "J"]
FAINT_YELLOW = Literal["K", "L", "M"]
VERY_LIGHT_YELLOW = Literal["N", "O", "P", "Q", "R"]
LIGHT_YELLOW = Literal["S", "T", "U", "V", "W", "X", "Y", "Z"]
COLOR = Literal[
    COLORLESS, NEAR_COLORLESS, FAINT_YELLOW, VERY_LIGHT_YELLOW, LIGHT_YELLOW
]


class Diamond(BaseModel):
    """
    Diamond description.
    Inherits from Pydantic's BaseModel thus it takes care automatically
    of input conformity and validation.
    """

    carat: StrictFloat
    cut: CUT
    color: COLOR
    clarity: CLARITY
    depth: StrictFloat
    table: StrictFloat
    x: StrictFloat
    y: StrictFloat
    z: StrictFloat
