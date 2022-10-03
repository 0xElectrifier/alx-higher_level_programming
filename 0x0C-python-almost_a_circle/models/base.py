#!/usr/bin/python3
"""First Project"""


class Base:
    """Base class of all other classes in this project. It manages
    ``id`` attribute in all other classes, to avoid duplicating the
    same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Object

        Args:
            id (int): id of objects
        """
        if (id is not None):
            __nb_objects += 1
            self.id = id
