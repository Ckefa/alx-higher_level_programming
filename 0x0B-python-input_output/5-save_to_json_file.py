#!/usr/bin/python3
"""This is my module."""
import json


def save_to_json_file(my_obj, filename):
    """Function to save the object as json to the file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
