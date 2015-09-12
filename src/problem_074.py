# -------------------------------------------------------------------------------
# Name:        Problem 74
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Solved:      12.09.2015
# Copyright:   (c) aliksey 2015
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import time

N = 1000000
periods = [0]*(N+1)
print len(periods)


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return reduce(lambda x, y: x*y, range(2, n+1), 1)


def digits(n):
    d = []
    while n > 0:
        d.append(n % 10)
        n //= 10
    d.reverse()
    return d


def f(n):
    return sum([factorial(x) for x in digits(n)])


def find_length(n):
    global periods

    n_set = set()
    n_arr = []
    while n not in n_set:
        n_arr.append(n)
        n_set.add(n)
        n = f(n)
    period = len(n_arr)

    for i in range(period):
        if n_arr[i] <= N:
            periods[n_arr[i]] = period - i

    return


def solve():
    for n in range(1, N+1):
        if periods[n] > 0:
            continue
        find_length(n)
    return sum([1 for p in periods if p == 60])


if __name__ == '__main__':
    print "Problem 74"
    start = time.time()
    print "Result:", solve()
    print "Solved in", time.time() - start, "sec"