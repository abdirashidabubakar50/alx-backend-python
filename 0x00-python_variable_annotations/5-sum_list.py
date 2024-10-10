#!/usr/bin/env python3
from typing import List
"""
This script defines a type-annotated fucntion sum_list
which takes a list  input_list of floats as argument and returns their sum
"""


def sum_list(input_list: List[float]) -> float:
    """
    function that returns sum of list input_list
    """
    return sum(input_list)
