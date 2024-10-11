#!/usr/bin/env python3
"""
This script defines a type-annotated function to_kv that
takes a string k and an int OR floatt v as arguments and returns
a tuple. The first element of the tupleis the string k. The second
element is the square of the int/float v and is annotated as a float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    this function returns a tuple. The first element of the tuple is
    the string k and the seceond is the square of the int/float v and
    is annotated as a float
    """
    squared_value = v ** 2
    return (k, squared_value)
