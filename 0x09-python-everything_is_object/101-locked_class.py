#!/usr/bin/python3

"""Define class locked."""


class LockedClass:
    """Represent a locked class."""
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        if key != "first_name":
            raise raise AttributeError("'LockedClass' object has no attribute '" + key + "'")
        self.__dict__[key] = value
