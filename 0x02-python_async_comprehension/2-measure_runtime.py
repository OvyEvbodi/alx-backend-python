#!/usr/bin/env python3
"""This module contains the coroutine `measure_runtime`.
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension
NO_OF_COROUTINES: int = 4


async def measure_runtime() -> float:
    """
    This function runs `async_comprehension` 4 times in parallel, and returns
    the total time taken.
    """
    start = time.perf_counter()
    await asyncio.gather(*(
        async_comprehension() for _ in range(NO_OF_COROUTINES)))

    return time.perf_counter() - start
