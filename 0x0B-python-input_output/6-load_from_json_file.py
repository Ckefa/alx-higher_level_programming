#!/usr/bin/python3
"""My main module."""
import json


def load_from_json_file(filename):
    """Function to load json object from file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f.read())
