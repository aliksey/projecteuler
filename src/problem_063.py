#-------------------------------------------------------------------------------
# Name:        Problem 63
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import math

def countDigits(N):
    return int(math.floor(math.log10(N)))+1


def main():
    n = 0
    k = 1
    while countDigits(9**k) == k:
        for m in range(1, 10):
            if countDigits(m**k) == k:
                n += 1
        k += 1
    print 'Total number:', n


if __name__ == '__main__':
    main()
