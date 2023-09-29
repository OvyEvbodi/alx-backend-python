#!/usr/bin/env python3
"""This module contains a type-annotated function `make_multiplier`
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """create a function that returns a function
    """
    return lambda x: x * multiplier
