#!/usr/bin/env python3
"""This module contains the multiple coroutines
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function returns the wait times in sorted order of each call to
    `wait_random` in seconds.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*coroutines)
    return sorted(wait_times)
