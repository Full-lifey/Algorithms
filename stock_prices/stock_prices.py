#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price_index = 0
    current_max_profit = 0
    for index, price in enumerate(prices):
        if index > 0:
            if price <= prices[current_min_price_index]:
                current_min_price_index = index
                if index != len(prices)-1:
                    for i in range(current_min_price_index+1, len(prices)-1):
                        if prices[i]-prices[current_min_price_index] > current_max_profit:
                            current_max_profit = prices[i] - \
                                prices[current_min_price_index]
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
