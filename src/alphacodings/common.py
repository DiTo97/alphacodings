import typing
from concurrent import futures
from functools import wraps

from gmpy2 import mpz


I = typing.TypeVar("I")
O = typing.TypeVar("O")


Encoding = list[str]
max_string_len = int(1e4)  # empirical


def base256_int_to_string(number: mpz) -> str:
    B = (number.bit_length() + 7) >> 3

    string = number.to_bytes(B, "big")
    return string.decode("utf-8")


def string_to_base256_int(string: str) -> mpz:
    return mpz.from_bytes(string.encode(), "big")


def chunking(string: str) -> list[str]:
    config = (0, len(string), max_string_len)
    return [string[i : i + max_string_len] for i in range(*config)]


def SIMD(closure: typing.Callable[[I], O]) -> typing.Callable[[list[I]], list[O]]:
    """decorator for function vectorization in SIMD mode.

    should significantly speed up the execution of CPU-bound tasks.
    """

    @wraps(closure)
    def wrapper(args: list[I]) -> list[O]:
        with futures.ProcessPoolExecutor() as executor:
            return list(executor.map(closure, args))

    return wrapper
