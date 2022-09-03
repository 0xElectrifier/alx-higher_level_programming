#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of matrix"""
    copy = [[x**2 for x in arr] for arr in matrix]
    return (copy)
