# -------------------------------------------------------------------------------
# Name:        Problem 64
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


import math


def getA0(n):
    a0 = int(math.floor(math.sqrt(n)))
    a1 = a0
    a2 = 1
    return n, a0, a1, a2


def getAn(t):
    (n, a0, a1, a2) = t
    b2 = int((n - a1 ** 2) / a2)
    b0 = int(math.floor((a1 + math.sqrt(n)) / b2))
    b1 = b0 * b2 - a1
    return n, b0, b1, b2


def computePeriod(n):
    t = getA0(n)
    pSet = set()
    while True:
        t = getAn(t)
        if t in pSet:
            return len(pSet)
        else:
            pSet.add(t)


def main():
    N = 0
    for n in range(2, 10000):
        m = int(math.floor(math.sqrt(n)))
        if (not m * m == n) and computePeriod(n) % 2 == 1:
            N += 1
    print 'Total:', N


if __name__ == '__main__':
    main()
