#!/usr/bin/python3

"""Creates a class Square"""


class Square:
    """Defines a square based on '4-square.py'"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)) and (not isinstance(value, float)):
            raise TypeError("size must be a number")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates area of the square"""
        return (self.size ** 2)

    def __eq__(self, other):
        """Defining the '==' comparison of the square"""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Defining the '!=' comparison of the square"""
        return (self.area() != other.area())

    def __gt__(self, other):
        """Defining the '>' comparison of the square"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Defining the '>=' comparison of the square"""
        return (self.area() >= other.area())

    def __lt__(self, other):
        """Defining the '<' comparison of the square"""
        return (self.area() < other.area())

    def __le__(self, other):
        """Defining the '<=' comparison of the square"""
        return (self.area() <= other.area())
