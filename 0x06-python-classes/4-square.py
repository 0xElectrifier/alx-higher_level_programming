#!/usr/bin/python3

"""Defines a class"""


class Square:
    """defines a square based on '3-square.py'"""
    def __init__(self, size=0):
        """Initializes the Square

        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """Getter function for self.__size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter function for square

        Args:
            value (int): value used to initialize self.__size
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >=  0")
        self.__size = value

    def area(self):
        """Calculates area of the square"""

        return (self.__size ** 2)
