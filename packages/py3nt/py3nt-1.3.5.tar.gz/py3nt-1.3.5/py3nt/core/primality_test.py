"""Define primality tests"""

import numpy as np


def is_prime_naive(n: int) -> bool:
    """Check if ``n`` is prime using square root method.

    :param n: Integer to check.
    :type n: ``int``
    :raises ValueError: If ``n`` is negative.
    :return: ``True`` if ``n`` is a prime. Otherwise, ``False``.
    :rtype: ``bool``
    """

    if n < 0:
        raise ValueError("n cannot be negative")

    if n < 2:
        return False
    if n < 4:
        return True

    if (n & 1) == 0:
        return False

    root = int(np.floor(np.sqrt(n)))

    for i in np.arange(start=3, stop=root + 1, step=2):
        if (n % i) == 0:
            return False

    return True
