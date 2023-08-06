"""Integers"""


class Integer(int):
    """Integer class"""

    def multiply_modular(self, other: int, modulus: int) -> int:
        """Calculate ``self*other%modulus``
        This remainder will always be non-negative.
        If negative integers are provided, they will be converted to positive first.

        :param other: Multiplier.
        :type other: ``int``
        :param modulus: Modulo used for multiplcation.
        :type modulus: ``int``
        :return: Multiplication of ``self`` and ``other`` modulo ``modulus``.
        :rtype: ``int``
        """

        remainder = 0

        cur = self % modulus
        other %= modulus

        while other > 0:
            if (other & 1) == 1:
                remainder += cur
                if remainder > modulus:
                    remainder -= modulus

            other >>= 1
            cur <<= 1
            if cur > modulus:
                cur -= modulus

        remainder %= modulus

        return remainder

    def __pow__(self, exponent: int, modulus=None):
        if not modulus:
            return pow(int(self), int(exponent))

        return pow(int(self), int(exponent), int(modulus))
