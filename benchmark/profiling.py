import time
import typing
from typing import Any

from memory_profiler import memory_usage


def measure(closure: typing.Callable[..., Any], *args: Any, **kwargs: Any) -> tuple[float, float]:
    """measures the elapsed and space efficiency of a closure"""
    start = time.perf_counter()
    space = memory_usage((closure, args, kwargs), interval=0.1, max_usage=True)
    
    elapsed = time.perf_counter() - start

    return elapsed, space
