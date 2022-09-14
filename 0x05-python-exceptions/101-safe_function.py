#!/usr/bin/pyhon3
from os import write


def safe_function(fct, *args):
    """executes a functon safely"""
    try:
        res = fct(*args)
    except Exception as err:
        write(2, "Exception: {}\n".format(err).encode("utf-8"))
        return (None)
    else:
        return (res)
