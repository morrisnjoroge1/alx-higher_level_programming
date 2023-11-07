#!/usr/bin/python3
"""

function that writes a string to a text file (UTF8) and
returns the number of characters written

"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns
        the number of characters written.

    Args:
        filename: The path to the file to write to.
        text: The string to write to the file.

    Returns:
        number of characters written to the file.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
