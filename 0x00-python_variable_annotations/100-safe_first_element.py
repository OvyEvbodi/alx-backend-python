#!/usr/bin/env python3
"""This module duck-types a function
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """This function returns the first element of a sequence, or None if none
    """
    if lst:
        return lst[0]
    else:
        return None
