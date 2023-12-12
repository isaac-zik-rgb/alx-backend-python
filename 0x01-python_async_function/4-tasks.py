#!/usr/bin/env python3
"""Tasks"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of all the delays"""
    list_float = []
    for i in range(n):
        list_float.append(task_wait_random(max_delay))
    return [await task for task in asyncio.as_completed(list_float)]
