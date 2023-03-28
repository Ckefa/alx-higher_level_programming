#!/usr/bin/python3

"""Defines class square."""


class Square:
    """Represent square."""

    def __init__(self, size=0):
        """
        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) != int:
            raise Exception("size must be an integer")
        if val < 0:
            raise ValueError
