#!/usr/bin/python3
"""Script that adds all arguments to a Python list, and then saves them
to a file"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

args = argv[1:]
filename = "add_item.json"
save_to_json_file(args, filename)
print(argv)
