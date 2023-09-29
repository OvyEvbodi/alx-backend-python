#!/usr/bin/env python3
"""This module contains the type-annotated function `sum_list`
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function sums the floats in `input_list` and returns the result
    """
    return sum(input_list)
