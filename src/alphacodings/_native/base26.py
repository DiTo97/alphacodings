from collections import deque

from .common import int_to_string, string_to_int


_encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_decoding = {value: key for key, value in enumerate(_encoding)}


def base26_encode(string: str) -> str:
    number = string_to_int(string)

    if number == 0:
        return _encoding[0]  # empty string or string that equals 0

    coding = deque()

    while number > 0:
        number, modulo = divmod(number, 26)
        coding.appendleft(_encoding[modulo])
    
    return "".join(coding)


def base26_decode(string: str) -> str:
    number = 0

    for character in string:
        number = number * 26 + _decoding[character]

    return int_to_string(number)
