#!/usr/bin/python

import sys
import itertools

def rock_paper_scissors(n):
  options = ["rock", "paper", "scissors"]

  def rps_recursive(n):
    nonlocal options
    permutations = list()
    if n == 0:
      permutations.append([])
    elif n <= 1:
      for option in options:
        permutations.append([option])
    else:
      for option in options:
        for newPermutation in rps_recursive(n-1):
          newPermutation.insert(0, option)
          permutations.append(newPermutation)
    return permutations
  return rps_recursive(n)


# def rock_paper_scissors(n):
#   if n==0:
#     return [[]]
#   return list(itertools.permutations([["rock"], ["paper"], ["scissors"]],n))
#   # for i in range(len(optionArr)):


# print(rock_paper_scissor(2))



# print(rock_paper_scissors(0))
# print(rock_paper_scissors(1))

# print(rock_paper_scissors(2))
# options = [['rock'], ['paper'], ['scissors']]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')