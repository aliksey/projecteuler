from problems.utils import get_n_primes, get_primes_smaller, PrimeFactorChain


def test_get_n_primes():
    primes = get_n_primes(5)
    assert primes == [2, 3, 5, 7, 11]


def test_get_primes_smaller():
    primes = get_primes_smaller(20)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19]
