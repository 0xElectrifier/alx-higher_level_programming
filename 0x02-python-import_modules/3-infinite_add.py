#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result of the addition of all arguments"""
    from sys import argv as argv

    sum = 0
    argc = len(argv)
    for arg in range(1, argc):
        sum += int(argv[arg])

    print(sum)
