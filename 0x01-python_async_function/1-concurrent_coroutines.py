#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""

from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Let's execute multiple coroutines at the same time with async"""
    arr = []
    for i in range(n):
        random_number = await wait_random(max_delay)
        arr.append(random_number)
    for i in range(len(arr)):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
