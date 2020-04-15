# -------------------------------------------------------------------------------
# Name:        Problem 76
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Solved:      25.12.2017
# Copyright:   (c) aliksey 2015
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import time

cash = dict()


def splits(n, m, depth=0):
    key = n*100 + min(m, n)
    if key in cash.keys():
        return cash[key]

    s = 0

    # if depth == 1:
    #     print(m)

    if n == 0:
        # print(" " * depth, "terminate")
        return 1
    else:
        for a in range(max(0, n-m), n):
            # print(" "*depth, n-a)
            s += splits(a, n-a, depth+1)
        cash[key] = s
        return s


def solve(N):
    return splits(N, N) - 1


if __name__ == '__main__':
    print("Problem 76")
    start = time.time()
    print("Result:", solve(100))
    print("Solved in", time.time() - start, "sec")
