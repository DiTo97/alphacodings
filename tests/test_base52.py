from alphacodings import base52_decode, base52_encode


def test_base52_empty():
    string = ""
    assert base52_decode(base52_encode(string)) == string


def test_base52_benchmark(benchmark: str):
    string = benchmark[:8]  # uint64_t
    assert base52_decode(base52_encode(string)) == string
