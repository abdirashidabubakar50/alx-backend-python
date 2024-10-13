#!/usr/bin/env python3
"""
This script defines a function that safely retrieve a value
from a mapping object
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None]
        ) -> Union[Any, T]:
    """
    Safely retrieve a value from a mapping object.

    This function attempts to retrieve a value from the given mapping
    using the provided key. If the key exists in the mapping, It returns
    the corresponding value. If the key does not exits, it returns the
    specified default value.

    Args:
        dct(Mapping): The mapping object (e.g, dictionary) to retrieve
                      the value from.
        Key (Any): The key to look up in the mapping.
        default(Union[T, None]): The default value to return if the  key
                                 is not found. It can be of any type T or None
    Returns:
        Union[Any, T]: The value associated with the key in the mapping
            if the key exists, Otherwise the defaultt value.

    Type variables:
            T: Represents the type of the default value and part of the return
            type.
    Examples:
        >>> d = {'a': 1, 'b': 2}
        >>> safely_get_value(d, 'a', 0)
        1
        >>> safely_get_value(d, 'c', 3)
        3
        >>> safely_get_value(d, 'd', None)
        None

    """
    if key in dct:
        return dct[key]
    else:
        return default
