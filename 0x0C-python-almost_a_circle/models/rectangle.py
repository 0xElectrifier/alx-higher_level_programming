#!/usr/bin/python3
"""Creates a class ``Rectangle``"""
from models.base import Base


class Rectangle(Base):
    """Defines a ``Rectangle`` Object."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle.

        Args:
            width (int): rectangle width.
            height (int): rectangle height.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __type_check(self, attribute, value):
        """Handles the type check of each setter methods

        Args:
            attribute (str): name of attribute
            value (object): value to be checked
        """
        if (type(value) is not int):
                raise TypeError("{} must be an integer".format(attribute))

    @property
    def width(self):
        """Returns the width attribute"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """Sets value for the `width` attribute"""
        self.__type_check("width", width)
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Returns the height attribute"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """Sets value for the ``height`` attribute"""
        self.__type_check("height", height)
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Returns the `x` attribute"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """Sets value for the `x` attribute"""
        self.__type_check("x", x)
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Returns the `y` attribute"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """Sets value for the `y` attribute"""
        self.__type_check("y", y)
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the ``Rectangle`` object"""
        return (self.height * self.width)