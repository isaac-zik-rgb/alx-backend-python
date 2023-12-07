#!/usr/bin/env python3
"""Type annotation function"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list: takes a list mxd_lst of floats and integers
    and returns their sum as a float."""
    return sum(mxd_lst)
