#!/usr/bin/python3
"""This is a module to manage files."""


def read_file(filename="", encoding="utf-8"):
    """This is the function for resding the file
    and printing the  ouptput to std out."""
    with open(filename, "r") as f:
        print(f.read(), end="")
