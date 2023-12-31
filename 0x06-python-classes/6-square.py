#!/usr/bin/python3

"""Define a class Square by: (based on 5-square.py)."""


class Square:
    """represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not (all isinstance(a, int) and a >= 0 for a in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        [print("") for a in range(0, self.__position)]
        for a in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__poosition[0])]
            [print("#", end="" for z in range(0, self.__size))]
            print("")
