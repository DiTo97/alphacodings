from collections import deque

import gmpy2

from alphacodings.common import (
    SIMD,
    Encoding,
    base256_int_to_string,
    chunking,
    max_string_len,
    string_to_base256_int,
)


_encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_decoding = {value: key for key, value in enumerate(_encoding)}


def _base26_encode(string: str) -> str:
    """encodes a string to base26"""
    number = string_to_base256_int(string)

    if number == 0:
        return _encoding[0]  # empty string or string that equals 0

    coding = deque()

    while number > 0:
        number, modulo = divmod(number, 26)
        coding.appendleft(_encoding[int(modulo)])

    return "".join(coding)


def _base26_decode(string: str) -> str:
    """decodes a base26 string"""
    number = gmpy2.mpz(0)

    for character in string:
        number = number * 26 + _decoding[character]

    return base256_int_to_string(number)


_SIMD_base26_encode = SIMD(_base26_encode)
_SIMD_base26_decode = SIMD(_base26_decode)


def base26_encode(string: str) -> Encoding:
    """encodes a string to base26 with chunking"""
    if len(string) < max_string_len:
        return [_base26_encode(string)]

    output = _SIMD_base26_encode(chunking(string))
    return output


def base26_decode(encoding: Encoding) -> str:
    """decodes a base26 encoding"""
    if len(encoding) == 1:
        return _base26_decode(encoding[0])

    output = _SIMD_base26_decode(encoding)
    output = "".join(output)

    return output
