#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    import copy

    cache = copy.deepcopy(my_list)
    cache[idx] = element
    return cache
