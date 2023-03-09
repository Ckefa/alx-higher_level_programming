#!/usr/bin/python3

from sys import argv

L = len(argv) - 1
print("{} argument{}{}".format(L, '' if L == 1 else 's', '.' if not L else ':'))

for i, v in enumerate(argv):
    if not i:
        continue
    print("{}: {}".format(i, v))
