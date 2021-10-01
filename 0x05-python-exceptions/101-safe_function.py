#!/usr/bin/python3


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        print("Exception:", err)
        return None

def print_message():
    print("Hello")

result = safe_function(print_message)
print(result)
