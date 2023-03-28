#!/usr/bin/python3

"""Defines class square."""


class Square:
    """Represent square."""

    def __init__(self, size=0):
        """
        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise Exception("size must be an integer")
        elif size < 0:
            raise ValueError
        self.__size = size
