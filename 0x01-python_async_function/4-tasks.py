#!/usr/bin/env python3
"""
Curriculum
Short Specializations
Average: 118.3%
0x01. Python - Async """
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Let's execute multiple coroutines at the same time with async"""
    arr: List[float] = []
    for i in range(n):
        arr.append(await task_wait_random(max_delay))
    for i in range(len(arr)):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
