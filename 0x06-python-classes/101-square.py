#!/usr/bin/python3

"""Creates a class Square"""


class Square:
    """Definees a square based on '6-square.py'"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        if (self.size == 0):
            print("")
            return
        [print("") for i in range(position[1])]
        for j in range(self.size):
            [print(" ", end="") for a in range(position[0])]
            [print("#", end="") for b in range(self.size)]
            print("")

    def __str__(self):
        if (self.size == 0):
            return ("")
        value = ""
        for i in range(self.position[1]):
            value += "\n"
        for j in range(self.size):
            for a in range(self.position[0]):
                value += " "
            for b in range(self.size):
                value += "#"
            if (j is not range(self.size)[-1]):
                value += "\n"

        return (value)
