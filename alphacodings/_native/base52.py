from collections import deque

from .common import base256_int_to_string, string_to_base256_int


_encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_decoding = {value: key for key, value in enumerate(_encoding)}


def base52_encode(string: str) -> str:
    number = string_to_base256_int(string)

    if number == 0:
        return _encoding[0]  # empty string or string that equals 0

    coding = deque()

    while number > 0:
        number, modulo = divmod(number, 52)
        coding.appendleft(_encoding[modulo])
    
    return "".join(coding)


def base52_decode(string: str) -> str:
    number = 0

    for character in string:
        number = number * 52 + _decoding[character]

    return base256_int_to_string(number)
