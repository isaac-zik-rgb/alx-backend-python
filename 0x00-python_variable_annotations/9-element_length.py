#!/usr/bin/env python3
"""Typing Annotation"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length: takes an iterable as an argument and return the list"""
    return [(i, len(i)) for i in lst]
