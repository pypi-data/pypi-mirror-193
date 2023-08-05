import sys


def parse_cli_arguments():
    """
    Parse the dataset path as a position CLI argument
    """
    try:
        return sys.argv[1]
    except IndexError:
        raise Exception("Please provide dataset path as first positional argument")
