def add_integer(a, b=98):
    if type(a) != int or type(b) != int and type(a) != float or type(b) != float:
        raise TypeError("a must be an integer or b must be an integer")