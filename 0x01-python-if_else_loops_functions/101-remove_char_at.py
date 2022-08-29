#!/usr/bin/python3

def remove_char_at(str, n):
    str_copy = str[:n] + str[(n + 1):]
    return str_copy
