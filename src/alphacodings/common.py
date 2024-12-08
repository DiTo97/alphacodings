from gmpy2 import mpz


def base256_int_to_string(number: mpz) -> str:
    B = (number.bit_length() + 7) >> 3

    string = number.to_bytes(B, "big")
    return string.decode("utf-8")


def string_to_base256_int(string: str) -> mpz:
    return mpz.from_bytes(string.encode(), "big")
