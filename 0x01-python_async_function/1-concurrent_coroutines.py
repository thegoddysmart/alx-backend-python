#!/usr/bin/env python3
"""
Spawn wait_random n times with the specified max_delay
Args:
    n (int): Number of times to spawn wait_random
    max_delay (int): Maximum delay value to pass to wait_random

Returns:
    List[float]: List of delays in ascending order
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks = []
    delays = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
