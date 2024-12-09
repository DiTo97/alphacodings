from alphacodings import base26_decode, base26_encode


def test_base26_empty():
    string = ""
    assert base26_decode(base26_encode(string)) == string


def test_base26_benchmark(benchmark: str):
    string = benchmark
    assert base26_decode(base26_encode(string)) == string
