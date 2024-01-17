#!/usr/bin/env python3
"""0x02. Python - Async Comprehension"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Import async_generator from the previous task and then write
    a coroutine called async_comprehension that takes no arguments."""
    arr = []
    async for i in async_generator():
        arr.append(i)

    return arr
