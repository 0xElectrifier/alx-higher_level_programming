#!/usr/bin/python3

"""Prints #pythoniscool using sys module"""
os = __import__("os")
write = os.write
write(1, "Hello World\n".encode("UTF-8"))
