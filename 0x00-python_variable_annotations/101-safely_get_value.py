#!/usr/bin/env python3
"""Typing Variable annotation"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """TypeVar that takes in dict, key and return the key"""
    if key in dct:
        return dct[key]
    else:
        return default
