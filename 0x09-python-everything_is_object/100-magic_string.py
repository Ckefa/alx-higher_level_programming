#!/usr/bin/python3
magic_string():
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join("BestSchool" for i in range(magic_string.count))
