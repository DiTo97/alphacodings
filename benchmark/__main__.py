from tqdm.auto import tqdm

from plotting import plot_measure_efficiency
from profiling import measure


def main():
    M = []  # functions
    N = []  # arguments
    
    efficiency = {closure.__name__: {"elapsed": [], "space": []} for closure in M}
    
    for arg in tqdm(N, desc="alphacodings"):
        for closure in M:
            elapsed, space = measure(closure, arg)

            efficiency[closure.__name__]["elapsed"].append(elapsed)
            efficiency[closure.__name__]["space"].append(space)
            
    plot_measure_efficiency(N, efficiency)


if __name__ == "__main__":
    main()
