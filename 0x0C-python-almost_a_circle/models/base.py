#!/usr/bin/python3
"""
Base model class


"""

import json
import csv
import turtle


class Base:
    """Represent a base model

    base for all classes in 0x0C* project

    Attributes:
        __nb_objects (int): instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes new Base.

        Args:
            id (int): identity of new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethods
    def to_json_string(list_dictionaries):
        """converts a list of dictionaries to JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            JSON serialization of a list of dictionaries
        """

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_of_dicts)
