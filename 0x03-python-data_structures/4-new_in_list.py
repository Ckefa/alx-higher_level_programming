#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    cache = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return cache
    else:
        cache[idx] = element
        return cache
