from collections import deque

import gmpy2
from .common import base256_int_to_string, string_to_base256_int


_encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_decoding = {value: key for key, value in enumerate(_encoding)}


def base26_encode(string: str) -> str:
    """encodes a string to base26"""
    number = string_to_base256_int(string)

    if number == 0:
        return _encoding[0]  # empty string or string that equals 0

    coding = deque()

    while number > 0:
        number, modulo = divmod(number, 26)
        coding.appendleft(_encoding[int(modulo)])
    
    return "".join(coding)


def base26_decode(string: str) -> str:
    """decodes a base26 string"""
    number = gmpy2.mpz(0)

    for character in string:
        number = number * 26 + _decoding[character]

    return base256_int_to_string(number)
