#!/usr/bin/env python3
"""
This script defines a function `zoom_array` that takes a tuple
of elements and a repetition factor,
and returns a list where each element from the tuple is repeated
a specified number of times.

Usage:
1. Define an input tuple with elements.
2. Call the `zoom_array` function with the tuple and desired factor.
3. The function returns a list with the zoomed-in elements.

Example:
- Input: (12, 72, 91) with a factor of 2 will produce:
  [12, 12, 72, 72, 91, 91]
- Input: (12, 72, 91) with a factor of 3 will produce:
  [12, 12, 12, 72, 72, 72, 91, 91, 91]
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a zoomed-in version of the input tuple by
    repeating each item a specified number of times.

    Parameters:
    lst (Tuple): A tuple containing the elements to be zoomed in.
    factor (int): The number of times to repeat each item in the
    tuple. Default is 2.

    Returns:
    List: A list containing the zoomed-in elements.

    Example:
    >>> zoom_array((1, 2, 3), 3)
    [1, 1, 1, 2, 2, 2, 3, 3, 3]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
