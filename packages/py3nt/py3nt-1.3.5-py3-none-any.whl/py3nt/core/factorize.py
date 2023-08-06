"""Factorize integers"""


from dataclasses import dataclass, field

import numpy as np

from py3nt.core.base import BaseFactorization, BaseSieveFactorization
from py3nt.core.sieve import SieveOfEratosthenes, SieveOfEratosthenesOptimized
from py3nt.defaults import (
    BIGGEST_NUMBER,
    LARGEST_SMALL_NUMBER,
    LOGN_PRIME_FACTOR_FIELD,
    MAX_LOGN_FACTORIZATION_LIMIT,
)


@dataclass
class NaiveSqrtFactorization(BaseFactorization):
    """Factorize small numbers in sqrt(n) complexity"""

    def factorize(self, n: int) -> dict[int, int]:
        root = int(np.floor(np.sqrt(1.0 * n)))

        factorization = {}

        for i in np.arange(start=2, step=1, stop=root + 1):
            if (n % i) == 0:
                prime_factor = i
                multiplicity = 0

                while (n % prime_factor) == 0:
                    n //= prime_factor
                    multiplicity += 1
                factorization[prime_factor] = multiplicity

        if n > 1:
            factorization[n] = 1

        return factorization


@dataclass
class SieveSqrtFactorization(BaseSieveFactorization):
    """Factorize positive integers"""

    def __post_init__(self) -> None:
        if self.sieve.primes_.shape[0] < 1:
            self.sieve.generate_primes()

    def factorize(self, n: int) -> dict[int, int]:
        print("sieve sqrt")
        primes = self.sieve.primes_
        root = int(np.floor(np.sqrt(1.0 * n)))

        factorization = {}

        for prime in primes:
            if prime > root:
                break

            if (n % prime) == 0:
                multiplicity = 0
                while (n % prime) == 0:
                    n //= prime
                    multiplicity += 1

                factorization[prime] = multiplicity

        if n > 1:
            factorization[n] = 1

        return factorization


@dataclass
class LognSieveFactorization(BaseSieveFactorization):
    """Factorize small numbers in logn complexity"""

    def __post_init__(self) -> None:
        prime_factors = getattr(self.sieve, LOGN_PRIME_FACTOR_FIELD)

        if prime_factors.shape[0] < self.sieve.limit:
            self.sieve.generate_primes()

    def factorize(self, n: int) -> dict[int, int]:
        """Factorize a positive integer in logn complexity.

        :param n: Positive integer to factorize.
        :type n: ```int```
        :raises ValueError: If sieve is ``None``.
        :return: Dictionary of prime factor, multiplicity as key-value pairs.
        :rtype: ``dict``
        """

        factorization: dict[int, int] = {}
        prime_factors = getattr(self.sieve, LOGN_PRIME_FACTOR_FIELD)

        while n > 1:
            prime_factor = prime_factors[n]

            multiplcity = 0
            while (n % prime_factor) == 0:
                n //= prime_factor
                multiplcity += 1

            factorization[prime_factor] = multiplcity

        return factorization


@dataclass
class BigIntFactorization(BaseFactorization):
    """Factorize large positive integers not exceeding a default biggest number."""

    def factorize(self, n) -> dict[int, int]:
        if np.greater(n, BIGGEST_NUMBER):
            raise ValueError(
                f"{n} is greater than the current default biggest number: {BIGGEST_NUMBER}"
            )

        return {}


@dataclass
class FactorizationFactory:
    """Factorize positive integers not exceeding the default biggest number.

    :raises ValueError: If n is negative or exceeds the default biggest number.
    :param N: Maximum value of positive integer to factorize.
    :type N: ``int``:
    :param with_sieve: True if sieve is used to factorize. Otherwise False.
    :type with_sieve: ``bool``
    """

    N: int
    with_sieve: bool = field(default=True)

    def _get_factorizer_class(self) -> BaseFactorization:
        if not self.with_sieve:
            return NaiveSqrtFactorization()
        if np.less_equal(self.N, MAX_LOGN_FACTORIZATION_LIMIT):
            return LognSieveFactorization(sieve=SieveOfEratosthenesOptimized(limit=self.N))
        if np.less_equal(self.N, LARGEST_SMALL_NUMBER):
            return SieveSqrtFactorization(
                sieve=SieveOfEratosthenes(limit=int(np.sqrt(self.N)))
            )
        return BigIntFactorization()

    def factorize(self, n: int) -> dict[int, int]:
        """Factorize positive integers"""

        if n < 1:
            raise ValueError("n must be a positive integer")

        if n == 1:
            return {1: 1}

        factorizer = self._get_factorizer_class()

        return factorizer.factorize(n=n)
