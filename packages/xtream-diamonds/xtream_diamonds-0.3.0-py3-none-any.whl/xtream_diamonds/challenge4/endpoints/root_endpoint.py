from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    """
    Root endpoint.
    Useful to display a message on the 'homepage' if the server gets accessed by browser.
    """
    return {"Xtream": "Assignment"}
