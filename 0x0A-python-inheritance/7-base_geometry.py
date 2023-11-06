#!/usr/bin/python3
"""

function that defines BaseGeometry

"""


class BaseGeometry:
    """ rep base geometry"""

    def area(self):
        """not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value as integer.

        Args:
            name(str): name of parameter
            valeu(int): parameter to validate.
        Raises:
            TypeError: if value not integer.
            ValueError: if value is <=0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
