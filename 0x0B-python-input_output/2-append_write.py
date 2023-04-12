#!/usr/bin/python3
"""This is the file handler module."""


def append_write(filename="", text=""):
    """A a function that appends a string at the end of a text file."""
    def append_write(filename="", text=""):
        with open(filename, "a", encoding="utf-8") as f:
            writer = f.write(text)
            return writer
