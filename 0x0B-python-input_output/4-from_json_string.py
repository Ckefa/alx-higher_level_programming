#!/usr/bin/python3
"""Main module."""
import json


def from_json_string(my_str):
    """A function to convert json to object.

    Args:
    my_str (str): The string to be converted to an object.
    """
    return json.loads(mystr)
