#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another in a new list"""
    new_list = list(map(lambda x: x if x is not search else replace, my_list))
    return (new_list)
