#!/usr/bin/python

import argparse

# buy low, sell high
# the biggist positive difference left to right
# you have to buy before you sell
# the array is a list of prices throughout the day
# buy at 270, sell at 3800


def find_max_profit(prices):
	# find the lowest price that is not the final number in the array
	# compare that num to every subsequent number in the array
	# log the highest, if another high comes along replace it

	lowest_num=[]
	for index in range(0, len(prices) - 1):
		print(f"forloop", prices[index]) # prints value at index
		print(index) # prints actual index

		current_price = prices[index]
		next_price = prices[index + 1]

		if current_price < next_price:
			lowest_num = current_price
			print(f"if statement: ", lowest_num)
	
	return lowest_num
# currently returns 1540 as lowest_num
# print(prices[index])


print(find_max_profit([1050, 270, 1540, 3800, 2])) # should return 3530

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
