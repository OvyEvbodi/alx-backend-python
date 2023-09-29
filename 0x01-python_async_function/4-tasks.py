#!/usr/bin/env python3
"""This module contains the multiple coroutines
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function returns the wait times in sorted order of each call to
    `task_wait_random` in seconds.
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*coroutines)
    return sorted(wait_times)
