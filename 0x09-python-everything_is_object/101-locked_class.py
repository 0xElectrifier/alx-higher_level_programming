#!/usr/bin/python3

"""Creates a class ``LockedClass``"""


class LockedClass:
    """Only allows dynamic creation of `first_name` attribute"""
    __slot__ = ('first_name')
