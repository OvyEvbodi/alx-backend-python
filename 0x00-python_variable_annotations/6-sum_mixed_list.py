#!/usr/bin/env python3
"""This module defines the type-annotated function `sum_mixed_list`
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of floats and/or integers in a list"""
    return sum(mxd_list)
