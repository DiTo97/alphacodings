import time
import typing
from typing import Any

import multiprocess
from memory_profiler import memory_usage


def execution(
    closure: typing.Callable[..., Any],
    args: tuple[Any],
    kwargs: dict[str, Any],
    queue: multiprocess.Queue,
) -> None:
    space = memory_usage((closure, args, kwargs), interval=0.1, max_usage=True)
    queue.put(space)


def measure(
    closure: typing.Callable[..., Any], timeout: float, *args: Any, **kwargs: Any
) -> tuple[float | None, float | None]:
    """measures the runtime and space efficiency of a closure"""
    queue = multiprocess.Queue()
    # Use dill to serialize the closure function
    process = multiprocess.Process(
        target=execution, args=(closure, args, kwargs, queue)
    )
    start = time.perf_counter()

    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()

        return None, None

    elapsed = time.perf_counter() - start
    space = queue.get()

    return elapsed, space
