#!/usr/bin/env python3
"""This module contains a type-annotated function `element_length`
"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function implements duck-typing"""
    return [(i, len(i)) for i in lst]
