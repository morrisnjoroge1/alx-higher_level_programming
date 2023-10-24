#!/usr/bin/python3

"""class that defines a square by: (based on 2-square.py)"""


class square:
    """represents a square""

        def __init__(self, size=0):
        """Initialize a new square."""

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate area of the square"""
        """Return the current area of the square."""
        return (self.__size * self.__size)
