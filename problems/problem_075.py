# -------------------------------------------------------------------------------
# Name:        Problem 75
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Solved:      25.12.2017
# Copyright:   (c) aliksey 2015
# Licence:     <your licence>
# -------------------------------------------------------------------------------
from math import *
import mylib
import time

L = 1500000


def solve():
    A = int(floor(L/(2 + sqrt(2))))
    result = dict()

    chain = mylib.PrimeFactorChain(A)
    for i in range(A):
        a = chain.get_next_number()
        factors = chain.get_factor_list()
        prime_factors, powers = factors_to_powers(factors)
        max_powers = [2*p+1 for p in powers]
        x_powers = mylib.all_samples(max_powers)

        for x_power in x_powers:
            y_power = [2*powers[i] - x_power[i] for i in range(len(powers))]
            x = powers_to_value(prime_factors, x_power)
            y = powers_to_value(prime_factors, y_power)
            if x >= y:
                continue
            if (x + y) % 2 == 1:
                continue
            b = (y - x) // 2
            if a > b:
                continue

            P = a + y
            if P > L:
                continue

            if P in result.keys():
                result[P] += 1
            else:
                result[P] = 1

            # print("P =", P,
            #       "\ta =", a,
            #       # factors,
            #       # prime_factors,
            #       # powers,
            #       "\tb =", b,
            #       "\tc =", c,
            #       # "\ty =", y,
            #       # y_power,
            #       # "\tx =", x,
            #       # x_power,
            #       # "\t", a**2 + b**2 == c**2,
            #       # P,
            #       "\t->", result[P])

    return sum([1 for key in result.keys() if result[key] == 1])


def factors_to_powers(factors):
    bases = [factors[0]]
    powers = [1]
    for i in range(1, len(factors)):
        p = factors[i]
        if p != factors[i-1]:
            powers.append(1)
            bases.append(factors[i])
        else:
            powers[-1] += 1
    return bases, powers


def powers_to_value(bases, powers):
    result = 1
    for p, n in zip(bases, powers):
        result *= p**n
    return result


if __name__ == '__main__':
    print("Problem 75")
    start = time.time()
    print("Result:", solve())
    print("Solved in", time.time() - start, "sec")
