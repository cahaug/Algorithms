#!/usr/bin/python
# prices = [100, 90, 80, 50, 20, 10]

import argparse
# prices = [int, int, int]
def find_max_profit(prices):
  current_min_price_so_far = min(prices)
  current_max_price_so_far = max(prices)
  # if the minimum price in the whole array precedes the maximum value in the array, easy to find the max profit
  if prices.index(current_min_price_so_far) < prices.index(current_max_price_so_far):
    return current_max_price_so_far - current_min_price_so_far
  else:
    #indices of comparison, i = buy, j=sell
    i = 0
    j = 1
    cycled = False
    # look at each price, save the highest & lowest prices
    max_profit_so_far = prices[j]-prices[i]
    # current_min_price_so_far = prices[i]
    while cycled != True:
      if i == len(prices):
        # print(max_profit_so_far)
        cycled = True
      elif j == len(prices):
        i+=1
        j=i+1
      elif (prices[j] - prices[i]) >= max_profit_so_far:
        max_profit_so_far = prices[j] - prices[i]
        # print(max_profit_so_far)
        j+=1
      else:
        # print(max_profit_so_far)
        # print(j)
        j+=1

    return max_profit_so_far

    # the index of the lowest price must be less than the index of the highest price
    # find the difference between each value and the values after it, saving the greatest difference (most profit)
    # loop through all values until the last two in the array are the only available
    # -> make every combination of possible buy and see which has the greatest profit making potential

# print(find_max_profit(prices))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))