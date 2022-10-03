#!/usr/bin/python3
"""Creates a class ``Rectangle``"""
Base = __import__("Base").Base


class Rectangle(Base):
    """Defines a ``Rectangle`` Object."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle.

        Args:
            width (int): rectangle width.
            height (int): rectangle height.
        """
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width attribute"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """Sets value for the `width` attribute"""
        self.__width = width

    @property
    def height(self):
        """Returns the height attribute"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """Sets value for the ``height`` attribute"""
        self.__height = height

    @property
    def x(self):
        """Returns the `x` attribute"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """Sets value for the `x` attribute"""
        self.__x = x

    @property
    def y(self):
        """Returns the `y` attribute"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """Sets value for the `y` attribute"""
        self.__y = y
