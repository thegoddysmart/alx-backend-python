#!/usr/bin/env python3
"""
Create an asyncio.Task for the wait_random coroutine.

Args:
    max_delay (int): The maximum delay for the wait_random coroutine.

Returns:
    asyncio.Task: The created asyncio Task.
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
