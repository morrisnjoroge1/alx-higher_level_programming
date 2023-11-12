#!/usr/bin/python3
"""

class Rectangle that inherits from Base

"""

from models.base import Base


class Rectangle(Base):
    """ subclass from class Base

    private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances for class rectangle"""

        super().__init__(id)   #super class calling
        self.height = height
        self.width = width
        self.x = x
        self.y = y

