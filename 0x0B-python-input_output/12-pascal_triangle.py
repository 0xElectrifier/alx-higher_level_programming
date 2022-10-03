#!/usr/bin/python3
"""Defines a function, ``pascal_triangle``"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal's triangle of n"""
    triangle = []

    for m in range(n):
        poww = str(11 ** m)
        triangle.append(int(i) for i in poww)

    return (triangle)
