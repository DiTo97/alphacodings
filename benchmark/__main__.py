import pathlib

from plotting import plot_measure_efficiency
from profiling import measure
from tqdm.auto import tqdm

from alphacodings import base26_decode, base26_encode, base52_decode, base52_encode
from alphacodings.base26 import _base26_single_decode, _base26_single_encode
from alphacodings.base52 import _base52_single_decode, _base52_single_encode


def b26_encode(input_string):
    # Convert input string to a base-256 integer
    base256_int = 0
    for char in input_string:
        base256_int = base256_int * 256 + ord(char)

    # Convert base-256 integer to base26 string
    if base256_int == 0:
        return "A"  # Special case for empty input or input that equals zero

    base26_str = ""
    while base256_int > 0:
        base26_str = chr(base256_int % 26 + 65) + base26_str
        base256_int //= 26

    return base26_str


def b26_decode(input_string):
    # Convert base26 string to a base-256 integer
    base26_int = 0
    for char in input_string:
        base26_int = base26_int * 26 + (ord(char) - 65)

    # Convert base-256 integer to string
    bytes_list = []
    while base26_int > 0:
        bytes_list.insert(0, base26_int % 256)
        base26_int //= 256

    return "".join(chr(byte) for byte in bytes_list)


test1 = lambda x: base26_decode(base26_encode(x))
test2 = lambda x: base52_decode(base52_encode(x))
test3 = lambda x: _base26_single_decode(_base26_single_encode(x))
test4 = lambda x: _base52_single_decode(_base52_single_encode(x))
test5 = lambda x: b26_decode(b26_encode(x))

ROOT = pathlib.Path(__file__).resolve().parents[1]
examples_dir = ROOT / "examples"
benchmark = examples_dir / "benchmark.html"

with benchmark.open("rt", encoding="utf-8") as f:
    string = f.read()


def main():
    L = [
        "base26",
        "base52",
        "base26 w/o chunking",
        "base52 w/o chunking",
        "Heaton's base26",
    ]
    M = [test1, test2, test3, test4, test5]  # functions
    K = [10**x for x in range(1, 7)]  # arguments
    N = [string[:k] for k in K]  # arguments

    # Warmup for each function on dummy input
    dummy_input = "warmup"
    for func in M:
        func(dummy_input)

    timeout = 60

    efficiency = {L[j]: {"elapsed": [], "space": []} for j, closure in enumerate(M)}

    for i, k in enumerate(tqdm(K, desc="alphacodings")):
        for j, closure in enumerate(M):
            elapsed_trials = []
            space_trials = []

            n = 5

            for _ in range(n):
                elapsed, space = measure(closure, timeout, N[i])

                if elapsed is None:
                    elapsed_trials = []
                    space_trials = []
                    break

                elapsed_trials.append(elapsed)
                space_trials.append(space)

            if not elapsed_trials:
                elapsed = None
                space = None
            else:
                elapsed = sum(elapsed_trials) / n
                space = sum(space_trials) / n

            print(
                f"{L[j]}({k}) -> elapsed: {(elapsed or float('NaN')):.6f}s, space: {(space or float('NaN')):.6f}MiB"
            )

            efficiency[L[j]]["elapsed"].append(elapsed)
            efficiency[L[j]]["space"].append(space)

    plot_measure_efficiency(K, efficiency, 30)


if __name__ == "__main__":
    main()
