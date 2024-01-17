#!/usr/bin/env python3
"""0x02. Python - Async Comprehension"""
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Write a coroutine called async_generator that takes no arguments."""

    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
