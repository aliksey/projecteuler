from collections import defaultdict
from typing import List

from problems.utils import Primes


class Problem77:
    def __init__(self):
        self.primes = Primes()
        self.term_count = {}

    def count_sums(self, target_sum: int, max_prime: int) -> int:
        # if (target_sum, max_prime) not in term_count.keys():
        #     return 0
        counter = 0
        for p in self.primes.series:
            if p > max_prime:
                # print("count_sums({}, {}) = {}".format(target_sum, max_prime, counter))
                return counter
            if (target_sum, p) in self.term_count.keys():
                counter += self.term_count[(target_sum, p)]

    def _get_terms(self, n: int, max_prime: int, terms: List[int]) -> None:
        # print("n = {}\tm = {}\tterms = {}".format(n, max_prime, terms))
        if self.primes.is_prime(n) and n <= max_prime and len(terms) > 0:
            print(" + ".join([str(x) for x in terms + [n]]))
        for p in self.primes.series:
            if p >= min(n - 1, max_prime + 1):
                return
            else:
                self._get_terms(n - p, p, terms + [p])

    def solve(self, variant_count: int) -> int:
        n = 2
        while True:
            count = 0

            if self.primes.is_prime(n):
                self.term_count[(n, n)] = 1
                # count += 1

            for prime in self.primes.series:
                if prime >= n:
                    break
                res = n - prime
                partial_sum_count = self.count_sums(res, prime)
                if partial_sum_count > 0:
                    self.term_count[(n, prime)] = partial_sum_count
                    # print("term_count[{}, {}] = {}".format(n, prime, term_count[(n, prime)]))
                    count += partial_sum_count
                else:
                    self.term_count[(n, prime)] = 0
                    # print("term_count[{}, {}] = {}".format(n, prime, term_count[(n, prime)]))

            # if primes.is_prime(n):
                # print("term_count[{}, {}] = {}".format(n, n, term_count[(n, n)]))

            print("{} -> {} sums".format(n, count))

            if count >= variant_count:
                self._get_terms(n, n, [])
                return n
            else:
                n += 1


if __name__ == "__main__":
    print("Answer: {}".format(Problem77().solve(5000)))
