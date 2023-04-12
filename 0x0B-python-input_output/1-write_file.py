#!/usr/bin/python3
"""This is file manager module."""


def write_file(filename="", text=""):
    """This is the function to write the file."""
    with open(filename, "w", encoding="utf-8") as f:
        writer = f.write(text)
        return writer
