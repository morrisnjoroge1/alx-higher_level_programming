#!/usr/bin/python3
"""

class Student that defines a student.

"""


class Student:
    """represents students"""

    def __init__(self, first_name, last_name, age):
        """initialize new student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student.

        Args:
            retrieves a dictionary representation of a Student
            instance (same as 8-class_to_json.py):
            
            If attrs is a list of strings, only attribute names
            contained in this list must be retrieved

            Otherwise, all attributes must be retrieved
        """

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
