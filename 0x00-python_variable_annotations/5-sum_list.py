#!/usr/bin/env python3
"""Type annotation function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list: takes a list of floats as argument and returns their sum"""
    return sum(input_list)
