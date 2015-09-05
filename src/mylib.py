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


def all_subsets(series):
    result = []

    for i in range(2**len(series)):
        n = i
        on = [0]*len(series)
        for j in range(len(on)):
            if n % 2 == 1:
                on[j] = 1
            n /= 2
        result.append([series[k] for k in range(len(series)) if on[k] == 1])
    return result


class PrimeFactorChain:
    def __init__(self, N, series=None):
        self.N = N
        self.value = 1
        self.chain = [1]
        self.prime_index = [0]
        if series is None:
            self.primes = get_primes_smaller(N)
        else:
            self.primes = series

    def increase_chain(self):
        x = self.value * self.primes[self.prime_index[-1]]
        if x <= self.N:
            self.value = x
            self.chain.append(self.primes[self.prime_index[-1]])
            self.prime_index.append(self.prime_index[-1])
            return True
        else:
            return False

    def cut_chain(self):
        if len(self.chain) == 1:
            return False
        else:
            self.value /= self.chain[-1]
            self.chain = self.chain[:-1]
            self.prime_index = self.prime_index[:len(self.chain) + 1]
            return True

    def append_chain(self):
        if self.prime_index[-1] + 1 == len(self.primes):
            return False

        x = self.primes[self.prime_index[-1] + 1]

        if x * self.value <= self.N:
            self.prime_index[-1] += 1
            self.chain.append(x)
            self.value *= x
            return True
        else:
            return False

    def get_next_number(self):
        if not self.increase_chain():
            while self.cut_chain():
                if self.append_chain():
                    break
            else:
                return 0
        return self.value

    def get_factor_list(self):
        return self.chain[1:]

    def get_factor_set(self):
        return set(self.chain[1:])


if __name__ == '__main__':
    print "mylib"