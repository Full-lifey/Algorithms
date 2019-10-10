#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
count = 0


def eating_cookies(n, cache=None):
    print(n)
    global count
    # Base case
    if n <= 0:
        return n
    elif n == 1:
        return n
    count += 1
    # Start by cookie monster taking three cookies if n > 3
    if n-3 > 0:
        return eating_cookies(n-3)
    if n-2 > 0:
        return eating_cookies(n-2)
    if n-1 > 0:
        return eating_cookies(n-1)
    return count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')


cache = {}


def dynamic_fib(n):
    global cache
    if n < 2:
        return n
    elif n in cache:
        return cache[n]
    else:
        cache[n] = dynamic_fib(n - 1) + dynamic_fib(n - 2)
        return cache[n]
