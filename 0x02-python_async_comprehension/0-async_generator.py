#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import Generator
import secrets


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10. Use the random module.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield secrets.SystemRandom().uniform(0, 10)
