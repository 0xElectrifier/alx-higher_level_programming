#!/usr/bin/python3
"""Prints all numbers from 0 to 98 in decimal and hexadecimal"""

for number in range(0, 99):
    print("{} = {:s}".format(number, hex(number)))
