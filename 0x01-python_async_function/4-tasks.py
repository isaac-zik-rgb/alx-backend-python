#!/usr/bin/env python3
"""Tasks"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> asyncio.Task:
    """returns a asyncio.Task"""
    list_float = []
    for i in range(n):
        list_float.append(asyncio.create_task(wait_random(max_delay)))
    return [await task for task in asyncio.as_completed(list_float)]
