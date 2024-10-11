#!/usr/bin/env python3
"""

This script defines a type-annotated functin make_multiplier
that takes a float multiplier as arguments and returns
a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    functin make_multiplier
    that takes a float multiplier as arguments and returns
    a function that multiplies a float by multiplier
    """
    def multiplier_function(x: float) -> float:
        """
        function that multiplies a float by multiplier
        """
        return x * multiplier
    return multiplier_function
