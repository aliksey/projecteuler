# -------------------------------------------------------------------------------
# Name:        Problem 74
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Solved:      20.09.2015
# Copyright:   (c) aliksey 2015
# Licence:     <your licence>
# -------------------------------------------------------------------------------
from math import *

import time


d = 10000
z = 1./((2.+sqrt(2))*(1.+sqrt(2)))


def valid_triangle(p, k):
    x = k**2 + 4*p*k
    y = sqrt(x)
    if (int(floor(y+0.1)))**2 == x:
        a = int(y) - k
        if a % 2 == 0:
            a /= 2
            c = (p - a + k)
            if c % 2 == 0:
                c /= 2
                # print "Triangle:", p, a, p-a-c, c
                return True
    return False


def number_of_triangles(p):
    count = 0
    print
    print p, ":"
    for k in range(1, int(floor(p*z))+1):
        if valid_triangle(p, k):
            count += 1
            print k,
            # if count > 1:
            #     return count
    return count


def solve():
    count = 0

    for p in range(12, d+1):
        if number_of_triangles(p) == 1:
            # print p
            count += 1

    return count


if __name__ == '__main__':
    print "Problem 75"
    start = time.time()
    # print valid_triangle(12, 1)
    # print number_of_triangles(12)
    # print number_of_triangles(24)
    # print number_of_triangles(30)
    # print number_of_triangles(36)
    # print number_of_triangles(40)
    # print number_of_triangles(48)
    # print number_of_triangles(120)
    print "Result:", solve()
    print "Solved in", time.time() - start, "sec"
