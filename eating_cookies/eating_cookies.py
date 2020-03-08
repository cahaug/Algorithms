#!/usr/bin/python

import sys
import math


# 4 ways to eat 3 cookies 
# 1+1+1
# 1+2
# 2+1
# 3
# 7 ways to eat 4 Cookies
# 1+1+1+1
# 1+1+2
# 1+2+1
# 1+3
# 2+1+1
# 2+2
# 3+1
# 13 ways to eat 5 cookies
# 1+1+1+1+1
# 1+1+1+2
# 1+1+2+1
# 1+2+1+1
# 2+1+1+1
# 1+1+3
# 1+3+1
# 3+1+1
# 2+2+1
# 2+1+2
# 1+2+2
# 2+3
# 3+2
# #







# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=dict()):
  # check if the n has already been calculate
  if n in cache:
    return cache[n]
  # base case, he cannot eat anymore cookies
  if n <= 0:
    return 1
  way_counter = 0
  for i in range(1, 4):
    if i < n:
      way_counter += eating_cookies(n - i)
    elif i == n:
      way_counter += 1
  # save the result of n into cache for reuse
  cache[n] = way_counter
  return way_counter
  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')