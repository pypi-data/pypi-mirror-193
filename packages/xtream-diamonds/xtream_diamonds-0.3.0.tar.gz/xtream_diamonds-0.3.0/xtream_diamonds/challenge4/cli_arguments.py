import argparse
from typing import Tuple


def read_cli_arguments() -> Tuple[str, str]:
    """
    Read CLI arguments:
    - --model/-m path to the json-serialized model
    - --address/-a server address
    Returns a tuple (model_path, server_address)
    """
    parser = argparse.ArgumentParser(
        prog="xtream-assignments-diamond",
        description="REST API Server for pricing diamonds",
        epilog="",
    )

    parser.add_argument(
        "-m", "--model", required=True, help="path to the json-serialized model"
    )
    parser.add_argument(
        "-a", "--address", required=True, help="server address e.g. 127.0.0.1:8000"
    )
    args = vars(parser.parse_args())

    return args["model"], args["address"]
