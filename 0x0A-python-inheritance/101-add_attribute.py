#!/usr/bin/python3

"""Defines a function, add_attribute"""


def add_attribute(self, var, value):
    """This function is equivalent to self.var = value

    Args:
        var (any): the variable to be added as attribute
        value (any): the value to be assigned to the variablea
    """
    if not hasattr(self, "__dict__"):
        raise TypeError("can't add new attributes")
    setattr(self, var, value)
