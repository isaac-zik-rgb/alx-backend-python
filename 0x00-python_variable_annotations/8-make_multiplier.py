#!/usr/bin/env python3
"""Type annotation function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier: takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier."""
    def multiplies(n: float) -> float:
        """multiplies: takes a float n as argument and
        returns the multiplication of n and multiplier."""
        return n * multiplier
    return multiplies
