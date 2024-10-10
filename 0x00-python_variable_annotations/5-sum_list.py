#!/usr/bin/env python3
"""
This script defines a type-annotated fucntion sum_list
which takes a list  input_list of floats as argument and returns their sum
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function that returns sum of list input_list
    """
    return sum(input_list)
