#!/usr/bin/env python3
"""0x02. Python - Async Comprehension"""
import asyncio
from time import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Import async_comprehension from the previous
    file and write a measure_runtime
    coroutine that will execute async_comprehension four
    times in parallel using asyncio.gather."""
    start = time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time()
    return end - start
