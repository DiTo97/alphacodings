import gmpy2


def base256_int_to_string(number: gmpy2.mpz) -> str:
    B = (number.bit_length() + 7) >> 3
    string = bytearray(B)

    i = 0

    while number > 0:
        i = i + 1

        string[B - i] = number & 0xFF
        number = number >> 8

    return string.decode("utf-8")


def string_to_base256_int(string: str) -> gmpy2.mpz:
    string = string.encode()
    number = gmpy2.mpz(0)

    for character in string:
        number = (number << 8) | character

    return number
