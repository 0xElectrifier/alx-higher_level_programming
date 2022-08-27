#!/usr/bin/python3
"""Program that prints numbers from 0 to 99, separated by ", " """

for number in range(0, 100):
    print("{:02d}".format(number), end="")
    if number != 99:
        print(", ", end="")
    else:
        print("")
