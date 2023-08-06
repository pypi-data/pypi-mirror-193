"""Generate primes using sieve"""


from dataclasses import dataclass, field

import numpy as np

from py3nt.core.base import BaseSieve


@dataclass
class SieveOfEratosthenes(BaseSieve):
    """Sieve of Eratosthenes for generating primes"""

    def generate_primes(self) -> None:
        """Generate primes and set it in ``self.primes_``"""

        flags = np.zeros(shape=(self.limit + 1,), dtype=np.byte)

        if (not self.limit) or self.limit < 2:
            return

        self.primes_ = np.empty(shape=(self.max_prime_count,), dtype=int)

        prime_count = 1
        self.primes_[0] = 2
        for i in np.arange(start=3, stop=self.limit + 1, step=2):
            if flags[i] == 0:
                self.primes_[prime_count] = i
                prime_count += 1
                flags[i * i : self.limit + 1 : i * 2] = 1

        self.num_primes = prime_count
        self.primes_ = self.primes_[:prime_count]


@dataclass
class SieveOfEratosthenesOptimized(BaseSieve):
    """We can store smallest prime factors for logn factorization"""

    largest_prime_factors_: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        self.largest_prime_factors_ = np.empty(shape=(0), dtype=int)

    def generate_primes(self) -> None:
        """Generate primes using largest prime factors"""

        if self.limit < 2:
            return

        self.largest_prime_factors_ = np.empty(shape=(self.limit + 1,), dtype=int)

        self.primes_ = np.empty(shape=(self.max_prime_count,))
        self.primes_[0] = 2

        prime_count = 1

        for i in np.arange(start=0, stop=self.limit + 1):
            self.largest_prime_factors_[i] = i

        for i in np.arange(start=2, stop=self.limit + 1, step=2):
            self.largest_prime_factors_[i] = 2

        for i in np.arange(start=3, stop=self.limit + 1, step=2):
            if self.largest_prime_factors_[i] == i:
                self.primes_[prime_count] = i
                prime_count += 1
                self.largest_prime_factors_[i * i : self.limit + 1 : 2 * i] = i

        self.num_primes = prime_count


class NumberOfPrimeFactorSieve(BaseSieve):
    """Sieve to get number of prime factors as well"""

    omega_: np.ndarray

    def generate_primes(self) -> None:
        flags = np.zeros(shape=(self.limit + 1,), dtype=np.byte)

        self.num_primes = 0
        self.primes_ = np.zeros(shape=(self.max_prime_count,), dtype=int)
        self.omega_ = np.zeros(shape=(self.limit + 1,), dtype=int)

        for i in np.arange(2, self.limit + 1):
            if flags[i] == 0:
                self.primes_[self.num_primes] = i
                self.num_primes += 1
                self.omega_[i] = 1

                flags[2 * i : self.limit + 1 : i] = 1
                self.omega_[2 * i : self.limit + 1 : i] += 1

        self.primes_ = self.primes_[: self.num_primes]
