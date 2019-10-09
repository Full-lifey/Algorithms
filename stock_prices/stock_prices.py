#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price_index = 0
    current_max_profit = 0
    # For loop to find index of lowest price
    for index, price in enumerate(prices):
        # Index is initialized at 0
        if index > 0:
            # If the price is less than the price at index 0
            if price <= prices[current_min_price_index]:
                # Update current_min_price_index
                current_min_price_index = index
                # Resolves edge case of lowest number at the end of prices
                if index != len(prices)-1:
                    # Loop through everything after current_min_price_index and find new current_max_profit
                    for i in range(current_min_price_index+1, len(prices)-1):
                        if prices[i]-prices[current_min_price_index] > current_max_profit:
                            current_max_profit = prices[i] - \
                                prices[current_min_price_index]
        else:
          # initialize current_max_profit based on the difference between first and second prices
          # Resolves negative profit issues relating to initializing current_max_profit at 0
            current_max_profit = prices[1] - prices[0]
    return current_max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
