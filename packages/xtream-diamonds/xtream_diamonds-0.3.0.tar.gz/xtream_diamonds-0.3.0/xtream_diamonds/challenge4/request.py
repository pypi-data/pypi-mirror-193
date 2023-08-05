#!/usr/bin/env python3
import requests
import argparse
import json

from .parsing import parse_address


def post():
    """
    This function is executed by the assignment-price CLI command.
    Create a post with a given diamond
    """
    parser = argparse.ArgumentParser(
        prog="xtream-assignments-diamond",
        description="REST API Server for pricing diamonds",
        epilog="",
    )

    parser.add_argument("-d", "--diamond", required=True)
    parser.add_argument("-a", "--address", required=True)
    args = vars(parser.parse_args())
    address, port = parse_address(args["address"])

    diamond = json.load(open(args["diamond"]))
    price = requests.post(
        "http://" + address + ":" + str(port) + "/prices", json=diamond
    )
    print(price.text)
