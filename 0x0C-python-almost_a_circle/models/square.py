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

    def __str__(self):
        """Returns information about the `Square`"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.height))
