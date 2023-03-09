#!/usr/bin/python3

if __name__ == '__main__':  
    from sys import argv

    print(sum(map(lambda x: int(x), argv[1:])))
