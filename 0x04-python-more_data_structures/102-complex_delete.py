#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary"""
    prev_k = None
    for k, v in list(a_dictionary.items()):
        if v is value:
            del a_dictionary[k]

    return (a_dictionary)
