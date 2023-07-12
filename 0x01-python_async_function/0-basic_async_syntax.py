#!/usr/bin/env python3

"""async function to delay display of random number
   between 0 and the integer passed in as an argument
   """

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Returns a random number between 0 and max_delay, after random period

    Args:
        max_delay - The maximum delay time in seconds, defaults to 10
    """

    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
