#!/usr/bin/env python3
from fastapi import FastAPI
import uvicorn


def start_server(
    app: FastAPI, host_address: str, port: int, log_level: str = "info"
) -> None:
    """
    Start the uvicorn web server.
    Takes a FastApi app, an IP address, a port and optionally the server log level
    """
    uvicorn.run(app, host=host_address, port=port, log_level=log_level)
