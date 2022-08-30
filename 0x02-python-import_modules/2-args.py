#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and list of its arguments"""
    from sys import argv as argv

    argc = len(argv) - 1
    str = "argument" if argc == 1 else "arguments"
    s = "." if argc == 0 else ":"
    print("{} {}{}".format(argc, str, s))

    for arg in range(1, argc + 1):
        print("{}: {}".format(arg, argv[arg]))
