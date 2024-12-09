from alphacodings import base52_decode, base52_encode


def test_base52_empty():
    string = ""
    assert base52_decode(base52_encode(string)) == string


def test_base52_benchmark(benchmark: str):
    string = benchmark
    assert base52_decode(base52_encode(string)) == string
