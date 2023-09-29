#!/usr/bin/env python3
"""This module contains a function `safely_get_value`
"""
from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Optional[T] = None) -> Union[Any, T]:
    """Safely get a value from a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
