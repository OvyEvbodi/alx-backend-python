#!/usr/bin/env python3
"""This module contains the async coroutine `wait_random`
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function waits for a random delay between 0 and `max_delay` seconds
    and eventually returns it.
    """
    res = random.uniform(0, max_delay)
    await asyncio.sleep(res)
    return res
