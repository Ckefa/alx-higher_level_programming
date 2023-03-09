#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    for i in filter(lambda x: not x.startswith('_'), dir(hidden_4)):
       print(i)
