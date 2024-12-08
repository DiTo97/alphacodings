import typing

import matplotlib.pyplot as plt


class Tracker(typing.TypedDict):
    """elapsed and space efficiency tracker for single configuration"""
    elapsed: list[float]
    space: list[float]


def plot_measure_efficiency(N: list[int], efficiency: dict[str, Tracker]):
    """plots the elapsed and space efficiency of multiple configurations"""
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)

    for config in efficiency:
        plt.plot(N, efficiency[config]["elapsed"], label=config)

    plt.xlabel("upper limit")
    plt.ylabel("elapsed (s)")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.title("elapsed efficiency")

    plt.subplot(1, 2, 2)

    for config in efficiency:
        plt.plot(N, efficiency[config]["space"], label=config)

    plt.xlabel("upper limit")
    plt.ylabel("space (MiB)")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.title("space efficiency")

    plt.tight_layout()
    plt.show()
