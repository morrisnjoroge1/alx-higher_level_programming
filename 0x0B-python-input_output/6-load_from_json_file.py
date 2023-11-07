#!/usr/bin/python3
"""

 function that creates an Object from a “JSON file”

 """

import json


def load_from_json_file(filename):
    """ creates an object from a JSON file.

    Args:
        filename: path to JSON file

    Return:
        object created from the JSON file.
    """
    with open(filename) as f:
        return json.load(f)
