#!/usr/bin/env python3
"""
This script returns a type-annotated function that returns values with
appropriate types
"""
from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains a sequence
    from the input iterable
    and the length of that sequence.

    Parameters:
    -----------
    lst : Iterable[Sequence]
        An iterable containing sequences (e.g., strings, lists, or tuples).

    Returns:
    --------
    List[Tuple[Sequence, int]]
        A list of tuples. Each tuple contains:
            - A sequence (e.g., string, list, or tuple)
              from the input iterable.
            - An integer representing the length of that sequence.

    Example:
    --------
    >>> element_length(["hello", (1, 2, 3), [4, 5]])
    [('hello', 5), ((1, 2, 3), 3), ([4, 5], 2)]
    """
    return [(i, len(i)) for i in lst]
