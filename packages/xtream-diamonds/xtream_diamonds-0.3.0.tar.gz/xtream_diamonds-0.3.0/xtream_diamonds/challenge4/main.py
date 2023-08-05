from fastapi import FastAPI

from .parsing import parse_address
from .endpoints import prices_endpoint, root_endpoint
from .cli_arguments import read_cli_arguments
from .server import start_server
from .model import load_model
from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from collections import defaultdict
from fastapi.encoders import jsonable_encoder


app = FastAPI()
app.include_router(prices_endpoint.router)
app.include_router(root_endpoint.router)


def main():
    """
    The assignment-server cli command executes this function:
    1. parse cli arguments (model_path, server_address)
    2. load the model from the given path
    3. start the web server at the given address
    """

    model_path, server_address = read_cli_arguments()

    load_model(model_path)

    address, port = parse_address(server_address)

    start_server(app, address, port)


@app.exception_handler(RequestValidationError)
async def custom_form_validation_error(request, exc):
    """
    Custom validation error logic.
    When a malformed diamond (e.g. missing a feature) is received the user receives a detailed error response.
    Example, the user sends a malformed diamond:
    - missing the carat field;
    - with cut being an unsupport categorical value;
    - with table not being a float;
    - missing the depth field.
    The response is:
    {"detail":"Invalid request",
    "errors":
        {"carat": ["field required"],
        "cut": ["unexpected value; permitted: 'Ideal', 'Premium', 'Very Good', 'Good', 'Fair'"],
        "depth": ["field required"]
        "table": ["value is not a valid float"]}}
    """
    reformatted_message = defaultdict(list)
    for pydantic_error in exc.errors():
        loc, msg = pydantic_error["loc"], pydantic_error["msg"]
        filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
        field_string = ".".join(filtered_loc)  # nested fields with dot-notation
        reformatted_message[field_string].append(msg)

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {"detail": "Invalid request", "errors": reformatted_message}
        ),
    )
