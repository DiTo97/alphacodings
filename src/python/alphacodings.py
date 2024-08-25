def base26_encode(string: str) -> str:
    base256_int = 0

    for character in string:
        base256_int = base256_int * 256 + ord(character)

    if base256_int == 0:
        return "A"  # empty input or input that equals 0

    base26_str = ""

    while base256_int > 0:
        base26_str = chr(base256_int % 26 + 65) + base26_str
        base256_int //= 26

    return base26_str


def base26_decode(string: str) -> str:
    base26_int = 0

    for character in string:
        base26_int = base26_int * 26 + (ord(character) - 65)

    bytestring = []

    while base26_int > 0:
        bytestring.insert(0, base26_int % 256)
        base26_int //= 256

    return "".join(chr(byte) for byte in bytestring)
