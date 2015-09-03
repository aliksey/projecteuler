# -------------------------------------------------------------------------------
# Name:        Problem 71
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


from math import *


def relativePrime(p, q):
    while p != q:
        if p > q:
            p -= q
        else:
            q -= p

    return p == 1


def main():
    maxRatio = 0

    for d in range(8, 1000001):
        for n in range(int(floor(d * 3. / 7.)), 1, -1):
            if relativePrime(n, d):
                if float(n) / float(d) > maxRatio:
                    maxN = n
                    maxD = d
                    maxRatio = float(n) / float(d)
                break

    print "Solution:", str(maxN) + "/" + str(maxD)


if __name__ == '__main__':
    main()