#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replacess my_list at idx with element without modifying my_list"""
    list_copy = []
    for item in my_list:
        list_copy.append(item)

    if idx < 0 or idx >= len(my_list):
        return (list_copy)
    list_copy[idx] = element

    return (list_copy)
