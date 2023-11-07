#!/usr/bin/python3
"""

function that returns the dictionary description with simple
data structure for json serialization of object

"""


def class_to_json(obj):
  """Returns the dictionary description with simple data structure 
    (list, dictionary, string, integer and boolean) for JSON serialization of an object.

  Args:
    obj: An instance of a class.

  Returns:
    A dictionary representation of the object.
  """

  return obj.__dict__
