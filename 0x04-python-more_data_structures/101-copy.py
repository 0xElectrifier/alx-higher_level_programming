#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """Returns a list with all values multiplied without using loops"""
    return (list(map(lambda x: list(map(lambda i: i**2, x)), matrix)))
