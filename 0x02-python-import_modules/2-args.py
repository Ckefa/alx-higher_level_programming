#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    L = len(argv) - 1

    print("{:d} argument{:s}{:s}".format(L,'' if L == 1 else 's', '.' if L < 1 else ':'))

    for i, v in enumerate(argv):
        if not i:
            continue
        else:
            print("{:d}: {:s}".format(i, v))
