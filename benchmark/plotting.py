import typing

import matplotlib.pyplot as plt


class Tracker(typing.TypedDict):
    """elapsed and space efficiency tracker for single configuration"""

    elapsed: list[float]
    space: list[float]


def plot_measure_efficiency(N: list[int], efficiency: dict[str, Tracker], timeout):
    """plots the elapsed and space efficiency of multiple configurations"""
    plt.figure(figsize=(12, 6), dpi=100)

    plt.subplot(1, 2, 1)

    for config in efficiency:
        elapsed = efficiency[config]["elapsed"]
        valid_elapsed = []
        valid_N = []
        for i, e in enumerate(elapsed):
            if e is None:
                plt.scatter(N[i-1], valid_elapsed[-1], color="red", marker="x", s=100)
                break
            valid_elapsed.append(e)
            valid_N.append(N[i])
        plt.plot(valid_N, valid_elapsed, label=config)

    plt.xlabel("characters")
    plt.ylabel("runtime (s)")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    # plt.title("elapsed efficiency")

    plt.subplot(1, 2, 2)

    for config in efficiency:
        space = efficiency[config]["space"]
        valid_space = []
        valid_N = []
        for i, s in enumerate(space):
            if s is None:
                plt.scatter(N[i-1], valid_space[-1], color="red", marker="x", s=100)
                break
            valid_space.append(s)
            valid_N.append(N[i])
        plt.plot(valid_N, valid_space, label=config)

    plt.xlabel("characters")
    plt.ylabel("memory (MiB)")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    # plt.title("space efficiency")

    plt.tight_layout()
    plt.show()