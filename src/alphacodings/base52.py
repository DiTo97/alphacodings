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


_encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_decoding = {value: key for key, value in enumerate(_encoding)}


def _base52_single_encode(string: str) -> str:
    """encodes a string to base52"""
    number = string_to_base256_int(string)

    if number == 0:
        return _encoding[0]  # empty string or string that equals 0

    coding = deque()

    while number > 0:
        number, modulo = divmod(number, 52)
        coding.appendleft(_encoding[int(modulo)])

    return "".join(coding)


def _base52_single_decode(string: str) -> str:
    """decodes a base52 string"""
    number = gmpy2.mpz(0)

    for character in string:
        number = number * 52 + _decoding[character]

    return base256_int_to_string(number)


_SIMD_base52_single_encode = SIMD(_base52_single_encode)
_SIMD_base52_single_decode = SIMD(_base52_single_decode)


def base52_encode(string: str) -> Encoding:
    """encodes a string to base52 with chunking"""
    if len(string) < max_string_len + 1:
        return [_base52_single_encode(string)]

    output = _SIMD_base52_single_encode(chunking(string))
    return output


def base52_decode(encoding: Encoding) -> str:
    """decodes a base52 encoding"""
    if len(encoding) == 1:
        return _base52_single_decode(encoding[0])

    output = _SIMD_base52_single_decode(encoding)
    output = "".join(output)

    return output
