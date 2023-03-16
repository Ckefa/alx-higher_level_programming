#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(filter(lambda x: my_list.count(x) < 2, my_list))
