# -------------------------------------------------------------------------------
# Name:        Problem 72
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Solved:      05.09.2015
# Copyright:   (c) aliksey 2015
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import time
import mylib

d = 12000


def solve():
    count = 0
    chain = mylib.PrimeFactorChain(d)

    primes = set(mylib.get_primes_smaller(d))

    while True:
        n = chain.get_next_number()
        if n == 0:
            break

        nom_min = n / 3
        nom_max = n / 2

        nom_series = []
        for x in primes.difference(chain.get_factor_set()):
            if x <= nom_max:
                nom_series.append(x)

        if len(nom_series) == 0:
            continue

        nom_chain = mylib.PrimeFactorChain(nom_max, nom_series)
        nom_values = []
        while True:
            v = nom_chain.get_next_number()
            if v > 0:
                if nom_min < v <= nom_max:
                    nom_values.append(v)
                else:
                    continue
            else:
                break
        count += sum([1 for v in nom_values], 0)

    return count


if __name__ == '__main__':
    print "Problem 73"
    start = time.time()
    print "Result:", solve()
    print "Solved in", time.time() - start, "sec"
