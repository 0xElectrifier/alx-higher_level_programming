#!/usr/bin/python3
"""Program that prints numbers from 0 to 99, separated by ", " """

for number in range(0, 100):
    if number == 99:
        print("{:02}".format(number))
    else:
        print("{:02}".format(number), end=", ")
