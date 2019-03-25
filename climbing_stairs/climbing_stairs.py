#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):

    # if stairs = 0, then return 1
    # if the num of stairs is < 0, return 0
    if n < 0:
        return 0

    if n % 3 == 0:
        return 0

    else:
        climbing_stairs(n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
