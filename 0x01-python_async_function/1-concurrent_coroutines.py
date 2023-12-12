#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """spawn wait_random n times with the specified max_delay."""
    list_float = []
    for i in range(n):
        list_float.append(asyncio.create_task(wait_random(max_delay)))
    return [await task for task in asyncio.as_completed(list_float)]
