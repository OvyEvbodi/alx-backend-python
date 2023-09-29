#!/usr/bin/env python3
"""This module contains the type-annotated function `to_kv`
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns the tuple of the kv pair of a as k and square of v"""
    return tuple((k, v ** 2))
