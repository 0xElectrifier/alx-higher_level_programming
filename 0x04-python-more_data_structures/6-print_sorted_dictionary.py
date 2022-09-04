#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    key_list = sorted(a_dictionary)
    for item in key_list:
        print("{}: {}".format(item, a_dictionary[item]))
