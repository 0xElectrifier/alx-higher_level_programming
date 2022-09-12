#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in my_list, only once for each integer"""
    res = 0
    new_list = set(my_list)
    for item in new_list:
        res += item

    return res
