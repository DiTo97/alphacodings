from collections import deque

import gmpy2

from alphacodings.common import base256_int_to_string, string_to_base256_int


_encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_decoding = {value: key for key, value in enumerate(_encoding)}


def base52_encode(string: str) -> str:
    """encodes a string to base52"""
    number = string_to_base256_int(string)

    if number == 0:
        return _encoding[0]  # empty string or string that equals 0

    coding = deque()

    while number > 0:
        number, modulo = divmod(number, 52)
        coding.appendleft(_encoding[int(modulo)])

    return "".join(coding)


def base52_decode(string: str) -> str:
    """decodes a base52 string"""
    number = gmpy2.mpz(0)

    for character in string:
        number = number * 52 + _decoding[character]

    return base256_int_to_string(number)
