#!/usr/bin/python3
""" a class to define a size of square """


square0 = __import__("0-square").Square


class Square(square0):
    """ an inherited class from Square definition class
    Args:
        square0 (class): a class which defin a square
    """

    def __init__(self, size):
        """initialization function
        Args:
            size (integer): a size attribute passed
        """
        self.__size = size
