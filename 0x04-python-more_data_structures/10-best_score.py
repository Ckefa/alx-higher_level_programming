#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return "None"
    else:
        return reduce(lambda x, y: y[0] if y[1] > x else x, a_dictionary)
