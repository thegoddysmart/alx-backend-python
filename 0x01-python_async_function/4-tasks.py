#!/usr/bin/env python3
"""
Spawn n tasks with the task_wait_random coroutine and
return a list of delays.

Args:
    n (int): The number of tasks to create.
    max_delay (int): The maximum delay for each task.

Returns:
    List[float]: A list of delays in ascending order.
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks = []
    delays = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
