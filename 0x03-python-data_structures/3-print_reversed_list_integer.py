#!/usr/bin/python3

def print_reversed_list_integer(my_list):
    """Prints all integers of a list, in reverse order"""
    if (my_list):
        print(my_list[len(my_list) - 1])
        print_reversed_list_integer(my_list[:-1])
