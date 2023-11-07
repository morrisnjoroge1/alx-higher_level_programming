#!/usr/bin/python3
"""

This module defines a string-to-JSON function

"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object.

    Args:
        my_obj: The object to serialize.
    """

    return json.dumps(my_obj)
