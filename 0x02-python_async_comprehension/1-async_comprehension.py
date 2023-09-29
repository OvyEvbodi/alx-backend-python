#!/usr/bin/env python3
"""This module contains the coroutine `async_comprehension`.
"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    This function gets a list of floats from `async_generator` using
    async comprehension.
    """
    return [n async for n in async_generator()]
