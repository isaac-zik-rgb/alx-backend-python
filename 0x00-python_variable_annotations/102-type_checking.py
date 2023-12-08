#!/usr/bin/env python3
"""Type Checking"""
from typing import List, Union, Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List:
    """zoom_array: takes a tuple and return a list"""
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)  # Returns a List[Union[int, float]]

zoom_3x = zoom_array(array, 3)
