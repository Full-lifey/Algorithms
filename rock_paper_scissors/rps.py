#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # initialize an array with possible options
    rps = ['rock', 'paper', 'scissors']
    # for play in rps:
    #   for play2 in rps:
    #     result.append([play, play2])

    '''
  For n=2
  loop over rps
    for every item in rps
      [rps[0], rps2[0]], [rps[0], [rps[1]]]
  '''
    results = []

    def loop(n, previous_plays=[]):
        # base case
        if n == 0:
            return results.append(previous_plays)
        else:
            for play in rps:
                loop(n-1, [*previous_plays, play])
    loop(n)
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
