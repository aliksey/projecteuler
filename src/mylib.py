# -------------------------------------------------------------------------------
# Name:        Library of useful utilities for projecteuler.net problems.
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     2015
# Copyright:   (c) aliksey 2015
# Licence:     <your licence>
# -------------------------------------------------------------------------------


primes = []


def get_n_primes(n):
    global primes
    primes = []
    x = 2

    while len(primes) < n:
        ok = True
        for y in primes:
            if x % y == 0:
                ok = False
                break
            if y * y > x:
                break
        if ok:
            primes.append(x)
        x += 1
    return primes


def get_primes_smaller(n):
    global primes
    primes = []
    x = 2

    while True:
        ok = True
        for y in primes:
            if x % y == 0:
                ok = False
                break
            if y * y > x:
                break
        if ok:
            primes.append(x)
        x += 1
        if x > n:
            return primes


def is_prime(n):
    global primes
    primes = []

    for i in range(len(primes)):
        if n % primes[i] == 0:
            return False
        if primes[i] * primes[i] > n:
            break

    if primes[-1] * primes[-1] < n:
        print('Too few primes')
        return False

    return True


def nod(a, b):
    while not a == b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
