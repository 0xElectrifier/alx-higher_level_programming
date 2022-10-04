#!/usr/bin/python3
"""First Project"""
import json


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
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of @list_dictionaries

        Args:
            list_dictionaries (list): containing dictionaries to be converted
        """

        ld = list_dictionaries
        if type(ld) is not list:
            return

        if ((len(ld) == 0) or (ld is None)):
            ld = []
        return (json.dumps(ld))
