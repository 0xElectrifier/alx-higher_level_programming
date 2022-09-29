#!/usr/bin/python3

"""Creates a class Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines an object which is a subclass of `Rectangle`"""

    def __init__(self, size):
        """Initializes the square.

        Args:
            size (int): size of square.
        """
        super().__init__(size, size)
        self.__size = size
