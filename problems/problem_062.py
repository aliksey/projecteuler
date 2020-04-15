# -------------------------------------------------------------------------------
# Name:        Problem 62
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


import sys


def getID(n):
    arr = []
    number = 0
    while n > 0:
        arr.append(n % 10)
        n //= 10
    arr = sorted(arr)
    for i in range(len(arr)):
        number += arr[i] * 10 ** i
    return number


def main():
    amount = dict()
    number = dict()
    for i in range(1, 10000):
        n = i ** 3
        m = getID(n)
        if m in amount.keys():
            amount[m] += 1
            if n < number[m]:
                number[m] = n
        else:
            amount[m] = 1
            number[m] = n
        if amount[m] == 5:
            print "Found 5er:", number[m]
            sys.exit()


if __name__ == '__main__':
    main()
