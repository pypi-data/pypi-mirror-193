from typing import Tuple


def parse_address(address: str) -> Tuple[str, int]:
    """
    Takes a full ip address and returns host address and port.
    The allowed address formats are:
    - 127.0.0.1:8000
    - http://127.0.0.1:8000
    - https://127.0.0.1:8000
    """
    address = address.replace("http://", "")
    address = address.replace("https://", "")

    if not ":" in address:
        raise Exception("Please specify port in the address e.g. 127.0.0.1:8000")
    address, port = tuple(address.split(":"))

    try:
        port = int(port)
    except ValueError:
        raise Exception(
            "Invalid port " + str(port) + " a valid address is 127.0.0.1:8000"
        )
    return address, port
