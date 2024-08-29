def base256_int_to_string(number: int) -> str:
    B = (number.bit_length() + 7) >> 3
    
    string = number.to_bytes(B, "big")
    return string.decode("utf-8")


def string_to_base256_int(string: str) -> int:
    return int.from_bytes(string.encode(), "big")
