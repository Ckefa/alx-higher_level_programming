#!/usr/bin/python3

"""Define class square."""


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    """Getting the value ofsize."""
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        """Setting the value of size."""
        if not isinstance(val, int):
            raise TypeErrorrr("size must be an integer")
        elif val < 0:
            raise TypeError("size must be >= 0")
        self.__size = val

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size