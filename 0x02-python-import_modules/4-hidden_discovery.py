#!/usr/bin/python3

import hidden_4

for i in filter(lambda x: not x.startswith('_'), dir(hidden_4)):
    print(i)
