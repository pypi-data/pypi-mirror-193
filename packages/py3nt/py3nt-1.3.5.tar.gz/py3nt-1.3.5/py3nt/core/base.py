"""Base classes"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import numpy as np

from py3nt.defaults import LARGEST_SMALL_NUMBER


@dataclass
class BaseSieve(ABC):
    """Abstract base class for sieve"""

    limit: int
    primes_: np.ndarray = field(default=np.empty(shape=(0,)))
    num_primes: int = field(default=0)

    @abstractmethod
    def generate_primes(self) -> None:
        """Generate primes when size is small"""

    @property
    def max_prime_count(self) -> int:
        """Maximum number of primes possible up to n.

        :param n: Upper bound for primes.
        :type n: ``int``
        :return: An upper bound on number of primes not exceeding ``n``.
        :rtype: int
        """

        if self.limit < 2:
            return 0

        tmp = np.log(self.limit)
        res = 1.0 + (1.28 / tmp)
        res *= self.limit / tmp
        res = int(np.floor(res))

        return res


@dataclass
class BaseFactorization(ABC):
    """Abstract base class for factorization"""

    @abstractmethod
    def factorize(self, n) -> dict[int, int]:
        """Factorize positive integers not exceeding 10^70.

        :param n: Positive integer to be factorized.
        :type n: ``int``
        :return: Dictionary of canonical prime factorization.
            Keys correspond to prime factors and values correspond to their multiplicity.
        :rtype: ``dict``
        """


@dataclass
class BaseSieveFactorization(BaseFactorization):
    """Base Factorization class with sieve"""

    sieve: BaseSieve
    largest_small_number: int = field(default=LARGEST_SMALL_NUMBER)
