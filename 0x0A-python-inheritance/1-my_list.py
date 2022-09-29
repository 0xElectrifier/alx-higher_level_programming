#!/usr/bin/python3

"""Defines a class MyList"""


class MyList(list):
    """Creates an improved list object"""

    def print_sorted(self):
        """Prints element of the list in sorted ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)

        return (sorted_list)
