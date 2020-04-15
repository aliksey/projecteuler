from collections import defaultdict

from problems.utils import Primes


def solve(variant_count: int) -> int:
    primes = Primes()
    term_count = {}

    def count_sums(target_sum: int, max_prime: int) -> int:
        # if (target_sum, max_prime) not in term_count.keys():
        #     return 0
        counter = 0
        for p in primes.series:
            if p > max_prime:
                # print("count_sums({}, {}) = {}".format(target_sum, max_prime, counter))
                return counter
            if (target_sum, p) in term_count.keys():
                counter += term_count[(target_sum, p)]

    n = 2
    while True:
        count = 0

        if primes.is_prime(n):
            term_count[(n, n)] = 1
            # count += 1

        for prime in primes.series:
            if prime >= n:
                break
            res = n - prime
            partial_sum_count = count_sums(res, prime)
            if partial_sum_count > 0:
                term_count[(n, prime)] = partial_sum_count
                # print("term_count[{}, {}] = {}".format(n, prime, term_count[(n, prime)]))
                count += partial_sum_count
            else:
                term_count[(n, prime)] = 0
                # print("term_count[{}, {}] = {}".format(n, prime, term_count[(n, prime)]))

        # if primes.is_prime(n):
            # print("term_count[{}, {}] = {}".format(n, n, term_count[(n, n)]))

        print("{} -> {} sums".format(n, count))

        if count >= variant_count:
            return n
        else:
            n += 1


if __name__ == "__main__":
    print(solve(16))
