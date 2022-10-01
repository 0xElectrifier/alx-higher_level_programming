#!/usr/bin/python3
"""Defines a function `class_to_json`"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure, for
    JSON serialization of an object
    """
    if not hasattr(obj, "__dict__"):
        return
    return (obj.__dict__)
