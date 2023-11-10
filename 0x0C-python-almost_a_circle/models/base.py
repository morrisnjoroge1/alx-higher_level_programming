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
