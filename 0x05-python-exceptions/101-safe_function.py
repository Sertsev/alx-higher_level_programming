#!/usr/bin/python3


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except Exception as err:
        print("Exception:", err)
        return None
