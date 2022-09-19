#!/usr/bin/python3

"""Creates a class Square"""


class Square:
    """Defines a square based on '5-square.py'"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square

        Args:
            size (int): size of the square
            position (int): f
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for self.size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for self.size

        Args:
            value (int): size of square
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for self.size"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method for self.position

        Args:
            value (int): size of square
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                (not isinstance(value[0], int)) or (value[0] < 0) or
                (not isinstance(value[1], int)) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints out the square with the character '#'"""
        if (self.size == 0):
            print("")
            return

        [print("") for i in range(self.position[1])]
        for i in range(self.size):
            [print(" ", end="") for j in range(self.position[0])]
            [print("#", end="") for j in range(self.size)]
            print("")
