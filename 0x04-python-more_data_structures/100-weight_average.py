#!/usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple"""
    if not my_list:
        return (0)

    weight_score = 0
    weights = 0
    for score, weight in my_list:
        weight_score += (score * weight)
        weights += weight
    average = weight_score / weights

    return (average)
