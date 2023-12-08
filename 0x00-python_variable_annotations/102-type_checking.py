#!/usr/bin/env python3
"""Type Checking"""
from typing import Tuple, List, Union


def zoom_array(lst: Tuple,factor: int = 2) -> List:
    """zoom_array: takes a tuple and return a tuple"""
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)  # Use a tuple instead of a list

zoom_2x = zoom_array(array)  # No issues here

zoom_3x = zoom_array(array, 3)
