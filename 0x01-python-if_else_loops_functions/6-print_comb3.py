#!/usr/bin/python3
for first in range(0, 10):
    for last in range((first + 1) , 10):
        if first != last:
            print(str(first) + str(last), end=', ')
