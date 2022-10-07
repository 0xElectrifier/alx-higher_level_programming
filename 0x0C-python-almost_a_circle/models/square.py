#!/usr/bin/python3
"""contains a class ``Square``"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a ``Square`` instance, which inherits from ``Rectangle``"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the `Square`

        Args:
            size (int): the size of the square
            x (int): handles the padding from the left on display of
                        the square
            y (int): handles the padding from the top on display of
                        the square
            id (int): the id of each square instance
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter method for `self.__size` attribute"""
        return (self.__width)

    @size.setter
    def size(self, size):
        """Setter method for `self.__size attribute

        Args:
            size (int): the value to be assigned
        """
        if (type(size) is not int):
            raise TypeError("width must be an integer")
        if (size <= 0):
            raise ValueError("width must be > 0")
        self.__width = size
        self.__height = size

    def update(self, *args, **kwargs):
        """Updates attributes of a `Square` instance

        Args:
            args (list): contains extra unknown arguments
                - 1st argument is the `id` attribute
                - 2nd argument is the `size` attribute
                - 3rd argument is the `x` attribute
                - 4th argument is the `y` attibute
            kwargs (list): just like args, contains list of key/word args
        """
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        if (args):
            return
        for key, value in list(kwargs.items()):
            if (key is "id"):
                self.id = key
            elif (key is "size"):
                self.size = key
            elif (key is "x"):
                self.x = key
            elif (key is "y"):
                self.y = key

    def to_dictionary(self):
        """Returns the dictionary representation of the `Square` instance"""
        r_dict = dict(id=self.id, size=self.size, x=self.x, y=self.y)

        return (r_dict)

    def __str__(self):
        """Returns information about the `Square`"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.size))
