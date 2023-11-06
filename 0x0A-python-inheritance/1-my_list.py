#!/usr/bin/python3
"""

class Mylist that inherits from list

"""


class MyList(list):
    """ class thta inherits from list

    Args:
        self(int)

    """

    def print_sorted(self):
        self.sort()
        print(self)
