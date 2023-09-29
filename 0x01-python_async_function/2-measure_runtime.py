#!/usr/bin/env python3
"""This module contains the benchmark function `measure_time`
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 0) -> float:
    """
    Returns the average execution time of each call of `wait_random`
    in `wait_n`.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start) / n
