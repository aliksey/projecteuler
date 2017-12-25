from unittest import TestCase
import mylib


class TestAllSamples(TestCase):

    def test_all_samples(self):
        series = [2, 3, 4]
        samples = mylib.all_samples(series)
        print(samples)
        self.assertEqual(len(samples), 24)

    def test_prime_factor_chain(self):
        a = mylib.PrimeFactorChain(70)
        for i in range(70):
            print(i, a.get_next_number())
