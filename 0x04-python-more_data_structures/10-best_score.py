#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if not a_dictionary:
        return None
    max_value_key = max(a_dictionary, key=a_dictionary.get)

    return (max_value_key)
