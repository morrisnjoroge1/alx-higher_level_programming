#!/usr/bin/python3
"""This module defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
  """Returns the JSON representation of an object (string).

  Args:
    my_obj: The object to serialize.

  Returns:
    The JSON representation of the object (string).
  """

  def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
