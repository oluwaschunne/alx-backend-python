#!/usr/bin/env python3
"""0x02. Python - Async Comprehension"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Write a coroutine called async_generator that takes no arguments."""

    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
