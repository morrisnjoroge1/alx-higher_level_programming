#!/usr/bin/python3
"""

function that defines an integer addition

"""


def add_integer(a, b=98):
    """ adds two integer or float number

    Args:
        a:first number
        b:second number

    Returns:
         The addition of a and b

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

        """

        if ((not isinstance(a, int) and not isinstance(a, float))):
           raise TypeError("a must be an integer")
        if ((not isinstance(b, int) and not isinstance(b, float))):
           raise TypeError("b must be an integer")
        return (int(a) + int(b))
