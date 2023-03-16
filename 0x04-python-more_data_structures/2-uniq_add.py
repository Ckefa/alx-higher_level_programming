#!/usr/bin/python3
def uniq_add(my_list=[]):
    return reduce(lambda x,y: x+y if my_list.count(x) < 2 and my_list.count(y) < 2, my_list)
