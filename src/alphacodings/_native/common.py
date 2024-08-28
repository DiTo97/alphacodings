def int_to_string(number: int) -> str:
    """converts a base256 int to a string"""
    B = (number.bit_length() + 7) >> 3
    
    string = number.to_bytes(B, "big")
    return string.decode("utf-8")


def string_to_int(string: str) -> int:
    """converts a string to a base256 int"""
    return int.from_bytes(string.encode(), "big")
