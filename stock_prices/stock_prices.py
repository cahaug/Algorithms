#!/usr/bin/python

import argparse
# prices = [int, int, int]
def find_max_profit(prices):
  # duplicate the array for manipulation
  # look at each price, save the highest & lowest prices
  # the index of the lowest price must be less than the index of the highest price
  # find the difference between each value and the values after it, saving the greatest difference (most profit)
  # loop through all values until the last two in the array are the only available
  # -> make every combination of possible buy and see which has the greatest profit making potential


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))