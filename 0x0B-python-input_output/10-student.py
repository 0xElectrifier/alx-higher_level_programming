#!/usr/bin/python3
"""Creates a class ``student``"""


class Student:
    """Defines a student object (based on ``9-student.py``"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student object.

        Args:
            first_name (str): student's first name.
            last_name (str): student's lastname.
            age (int): student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of ``Student`` object"""
        if (attrs is None):
            return (self.__dict__)

        my_dict = {}
        for key in attrs:
            if (hasattr(self, key)):
                my_dict[key] = getattr(self, key, None)
        return (my_dict)
