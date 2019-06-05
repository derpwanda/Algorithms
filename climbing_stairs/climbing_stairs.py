#!/usr/bin/python

import sys

'''
Polya
Understand the problem: 
  There is a staircase with N number of stairs.
  I can only move 1, 2 or 3 stairs at a time, no matter how many
    stairs N is (unless is less than possible num of stair I can move)
  
  I need to return the number of DIFFERENT WAYS I can ascend the stairs.
  For example:
    # num of stairs: 3
    # 1 + 1 + 1 - take 1 stair at a time for a total of 3
    # 2 + 1 - take 2 stair, then 1 stair for a total of 3
    # 1 + 2 - take 1 stair, then 2 stair for a total of 3
    # 3 - take 3 stairs once for a total of 3
    
    means that there are FOUR ways to ascend the stairs

    # num of stairs: 4
    # 3 + 1
    # 2 + 1 + 1
    # 2 + 2
    # 1 + 3
    # 1 + 2 + 1
    # 1 + 1 + 2
    # 1 + 1 + 1 + 1

    there are 7 ways to ascend the stairs

    Questions:
    - What is the purpose of `cache`?
    - if recursive, what is the base case?
        - if stairs = 0, return 1
        - if stairs < 0, return 0
'''

def climbing_stairs(n, cache=None):
  if n < 2:
    return n
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    cache[n] = climbing_stairs(n - 1, cache) + climbing_stairs(n - 2, cache)

    return cache[n]

print(climbing_stairs(3))

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
