#!/usr/bin/python3
"""

Defines a text file-reading function.

"""


def read_file(filename=""):
    """Reads a text file UTF-8 text file to stdout.

    Args:
        filename: The path to the file to read.
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
