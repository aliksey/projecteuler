# -------------------------------------------------------------------------------
# Name:        Problem 60
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


def getPrimes(N):
    n = 0
    x = 2
    primes = []

    while len(primes) < N:
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


def check(num):
    for i in range(len(num)):
        for j in range(len(num)):
            if i == j:
                continue
            number = int(str(num[i]) + str(num[j]))
            if not isPrime(number):
                return False
    return True


def isPrime(n):
    for i in range(len(primes)):
        if n % primes[i] == 0:
            return False
        if primes[i] * primes[i] > n:
            break

    if primes[-1] * primes[-1] < n:
        print('Too few primes')
        return False

    return True


primes = getPrimes(6000)


def solve():
    print('Max prime: ' + str(primes[-1]))

    aseries = primes[1:1100]

    for a in aseries:
        bseries = []
        for b in aseries:
            if b <= a:
                continue
            if check([a, b]):
                bseries.append(b)

        for b in bseries:
            cseries = []
            for c in bseries:
                if c <= b:
                    continue
                if check([a, c]) and check([b, c]):
                    cseries.append(c)

            for c in cseries:
                dseries = []
                for d in cseries:
                    if d <= c:
                        continue
                    if check([a, d]) and check([b, d]) and check([c, d]):
                        dseries.append(d)

                for d in dseries:
                    for e in dseries:
                        if e <= d:
                            continue
                        if check([a, e]) and check([b, e]) and check([c, e]) and check([d, e]):
                            print(
                            'Found: ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + ' ' + str(e) + ': ' + str(
                                a + b + c + d + e))
                            return

    print('Not found')


def main():
    solve()


if __name__ == '__main__':
    main()
