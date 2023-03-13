#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if not i:
            print()
            break
        else:
            for j in i:
                print("{:d}".format(j), end="\n" if i.index(j) >= len(i) - 1 else " ")
