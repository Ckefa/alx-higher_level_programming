#!/usr/bin/python3

"""Define class square."""


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeErrorrr("size must be an integer")
        elif val < 0:
            raise TypeError("size must be >= 0")
        self.__size = val

    def area(self):
        return self.__size * self.__size
