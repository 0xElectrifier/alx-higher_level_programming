#!/usr/bin/python3

"""Prints #pythoniscool using sys module"""
os = __import__("os")
os.write(1, "Hello World\n".encode("UTF-8"))
