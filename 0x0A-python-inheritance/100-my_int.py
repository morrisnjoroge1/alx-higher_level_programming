#!/usr/bin/python3
"""

function module that defines calss MyInt that inherits from int

"""


class MyInt(int):
    """ flips behavior of == and !="""

    def __eq__(self, value):
        """ altered to return inverse __eq__"""
        return (self.real != value)

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
