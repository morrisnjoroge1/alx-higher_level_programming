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


    @classmethod
    def save_to_file(cls,list_of_objects):
        """Saves the JSON serialization of a list of objects to a file.

        Args:
            lists_obj(list) - list pof inherited Base inheritance
        """

       filename = cls.__name__ + ".json"

       with open(filename, "w") as jsonfile:
           if not list_objs:
               jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))


    @staticmethod
    def from_json_string(json_str):
        """Deserialize a JSON string.

        Args:
            json_str (str): A JSON string representing a list of dictionaries.
        Returns:
            If json_str is None or empty - an empty list.
            Otherwise - the Python list represented by json_str.
        """
        if not json_str or json_str == "[]":
            return []
        return json.loads(json_str)

    
    `

