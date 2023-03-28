#!/usr/bin/python3

"""Define class square."""


class Square:
    """Represent class square"""

    def __init__(self, size=0):
        if isinstance(size, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
