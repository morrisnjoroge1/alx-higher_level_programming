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

    @property
    def width(self):
        """Retrive the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting and validating width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting and validating height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting and validating x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for  y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting and validating y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for i in range(self.__y):
            print()

        for i in range(self.__height):
            for n in range(self.__width + self.__x):
                if n < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()
    def __str__(self):
        """Return the string representation of the Rectangle instance."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, 
                self.__x, self.__y, self.__width, self.__height)
