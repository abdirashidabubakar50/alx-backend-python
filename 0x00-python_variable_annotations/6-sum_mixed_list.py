#!/usr/bin/env python3
"""
This script defines type-annotated function sum_mixed_list
which takes a list mxd_list of integers and floats and returns
their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ This function returns the sum of mxd_list as float"""
    return float(sum(mxd_lst))
