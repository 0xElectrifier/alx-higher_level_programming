#!/usr/bin/python3

from os import write
def safe_print_integer_err(value):
    """Prints an integer

    Args:
        value (int): value to be printed

    Return:
        True if value is an integer otherwise, False
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        write(2, "Exception: {}\n".format(err).encode("utf-8"))
        return (False)
    else:
        return (True)
