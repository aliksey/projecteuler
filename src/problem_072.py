# -------------------------------------------------------------------------------
# Name:        Problem 72
# Purpose:     projecteuler.net
#
# Author:      aliksey
#
# Created:     06.04.2012
# Copyright:   (c) aliksey 2012
# Licence:     <your licence>
# -------------------------------------------------------------------------------


import mylib
import time


d = 1000000
chain = [1]
value = 1
prime_index = [0]


def increase_chain():
    global chain
    global value

    x = value * mylib.primes[prime_index[-1]]

    if x <= d:
        value = x
        chain.append(mylib.primes[prime_index[-1]])
        prime_index.append(prime_index[-1])
        return True
    else:
        return False


def cut_chain():
    global chain
    global prime_index
    global value

    if len(chain) == 1:
        return False
    else:
        value /= chain[-1]
        chain = chain[:-1]
        prime_index = prime_index[:len(chain) + 1]
        return True


def append_chain():
    global chain
    global prime_index
    global value

    if prime_index[-1] + 1 == len(mylib.primes):
        return False

    x = mylib.primes[prime_index[-1] + 1]

    if x * value <= d:
        prime_index[-1] += 1
        chain.append(x)
        value *= x
        return True
    else:
        return False


def get_prime_set():
    return set(chain[1:])


def n_of_mx(m, x, n=d):
    return (n - m) / x


def all_combinations(series):
    result = []

    for i in range(1, 2**len(series)):
        n = i
        on = [0]*len(series)
        for j in range(len(on)):
            if n % 2 == 1:
                on[j] = 1
            n /= 2
        result.append([series[k] for k in range(len(series)) if on[k] == 1])
    return result


def add_count(m, series):
    z = d - m
    coms = all_combinations(series)
    for com in coms:
        x = reduce(lambda z, y: z*y, com, 1)
        if len(com) % 2 == 1:
            z -= n_of_mx(m, x)
        else:
            z += n_of_mx(m, x)
    return z


def solve():
    mylib.get_primes_smaller(d)
    count = d-1   # start with the number of fractions 1/x

    start = time.time()

    while True:
        if increase_chain():
            count += add_count(value, list(get_prime_set()))
        else:
            while cut_chain():
                if append_chain():
                    count += add_count(value, list(get_prime_set()))
                    break
            else:
                break

    print "Solved in", time.time() - start, "sec"
    return count


if __name__ == '__main__':
    print "Problem 72"
    print solve()
