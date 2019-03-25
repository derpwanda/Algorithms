#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):


print(climbing_stairs(3))


# 3
# 1 + 1 + 1
# 2 + 1
# 1 + 2
# 3


# 4
# 1 + 1 + 1 + 1
# 3 + 1
# 1 + 3
# 2 + 1 + 1
# 2 + 2
# 1 + 2 + 1
# 1 + 1 + 2


# 5
# 2 + 2 + 1
# 1 + 2 + 2
# 1 + 1 + 1 + 1 + 1
# 2 + 1 + 2
# 1 + 2 + 1 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 2 + 1
# 1 + 1 + 1 + 2
# 3 + 2
# 2 + 3
# 3 + 1 + 1
# 1 + 3 + 1
# 1 + 1 + 3



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
