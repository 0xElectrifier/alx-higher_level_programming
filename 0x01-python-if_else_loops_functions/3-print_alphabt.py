#!/usr/bin/python3
"""Funvtion that prints all ASCII lowercase alphabets except q"""

for letter in range(97, 123):
    if letter == 101 or letter == 113:
        continue
    print("{}".format(chr(letter)), end="")
