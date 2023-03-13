#!/usr/bin/python3

def no_c(my_string):
    return "".join(map(lambda x: "" if x == 'c' or x == 'C' else x, my_string))
