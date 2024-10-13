#!/usr/bin/env python3

"""
This scirpt defines an Augmented type-annotated function with
duck typed annotations
"""
from typing import Any,  Sequence, Union, Optional


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieve the first element of a sequence.

    This function takes a sequence as input and returns its first element.
    If the sequence is empty, it returns None instead of raising an IndexError.

    Args:
        lst (Sequence[Any]): The input sequence. Can be any sequence type
                             (list, tuple, etc.) containing elements of any
                             type.

    Returns:
        Union[Any, None]: The first element of the sequence if it's non-empty,
                          or None if the sequence is empty.

    Examples:
        >>> safe_first_element([1, 2, 3])
        1
        >>> safe_first_element(["a", "b", "c"])
        'a'
        >>> safe_first_element([])
        None
        >>> safe_first_element(())
        None
    """
    if lst:
        return lst[0]
    else:
        return None
