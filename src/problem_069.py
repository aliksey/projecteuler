# -------------------------------------------------------------------------------
# Name:        Problem 69
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


def getPrimes(n=None):
    prime = []

    for k in range(2, n + 1):
        ok = True
        for m in prime:
            if k % m == 0:
                ok = False
                break
        if ok:
            prime.append(k)

    return prime


def getCombinations(n, k):
    N = len(n)
    mult = list(n)
    factors = []

    a = [mult[i] for i in range(k)]
    factors.append(reduce(lambda x, y: x * y, a))

    while True:
        for j in range(k):
            if a[j] == mult[N - 1] and j == k - 1:
                return factors
            if j < k - 1 and mult.index(a[j]) + 1 == mult.index(a[j + 1]):
                continue
            a[j] = mult[mult.index(a[j]) + 1]
            for i in range(j):
                a[i] = mult[i]

            #             print a
            factors.append(reduce(lambda x, y: x * y, a))


def main():
    prime = getPrimes(1000)
    Q = 0
    P = 0

    for n in range(2, 1000000):
        N = n - 1

        divs = set([])

        # find all prime divisors
        for p in prime:
            if p >= n:
                break
            if n % p == 0:
                divs.add(p)

        for d in divs:
            N -= (N / d - 1)
            if n % d == 0:
                N -= 1

        if len(divs) > 1:
            for m in range(2, len(divs) + 1):
                factors = getCombinations(divs, m)
                #                 print factors
                for f in factors:
                    if m % 2 == 0:
                        N -= N / f
                    else:
                        N += N / f

        q = float(n) / float(N)

        if q > Q:
            Q = q
            P = n

    print "Solution:", P


if __name__ == '__main__':
    main()
