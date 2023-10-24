#!/usr/bin/python3

"""Defines a square by: (based on 3-square.py)"""


class square:
""""represents a square"""

def __init__(self, size=0):
"""
initialization of square class
Args:
size: size of square defined
TypeError: if size is not integer
ValueError: if size is less than zero
"""

if not isinstance(size, int):
raise TypeError('size must be an integer')
if size < 0:
raise ValueError('size must be >= 0')

self.__size = size

@property
def size(self, value):
if not isinstance(value, int):
raise TypeError('size must be an integer')
if value < 0:
raise ValueError('size must be >= 0')
self.__size = value

def area(self):
"""
Calculate area of the square
Returns: The square of the size
"""

return (self.__size ** 2)
