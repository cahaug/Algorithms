#!/usr/bin/python

import sys
cache={}
def making_change(amount, denominations, cache=cache):
  #check if the n has already been calculated
  if cache!=None and amount in cache:
    return cache[amount]
  #base case, cannot split up zero cents
  if amount == 0:
    return 1
  # if amount == 1:
  #   return 1

  way_counter = 0
  # for value in denominations:
  #   #for the value in the denominations
  #   if amount >= value:
  #     #if the amt is greater than the value, subtract that value then recurse
  #     way_counter += making_change(amount-value, denominations, cache=cache)
  if amount >= 50:
    #use a half dollar
    way_counter += making_change(amount-50, denominations, cache=cache)
  if amount >= 25:
    #use a quarter
    way_counter += making_change(amount-25, denominations, cache=cache)
  if amount >= 10:
    #use a dime
    way_counter += making_change(amount-10, denominations, cache=cache)
  if amount >= 5:
    #use a nickel
    way_counter += making_change(amount-5, denominations, cache=cache)
  if amount >= 1:
    #use a penny
    way_counter += making_change(amount-1, denominations, cache=cache)
  cache[amount] = way_counter
  return way_counter


# print(making_change(15, [1, 5, 10, 25, 50], cache))


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")