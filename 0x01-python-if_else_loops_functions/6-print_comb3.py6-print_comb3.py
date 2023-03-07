#!/usr/bin/python3

for i in range(1, 10):
    for j in range(i+1, 10):
        print("{0:}{1:}".format(i-1, j-1), end=", " if i < 9 else "\n")

