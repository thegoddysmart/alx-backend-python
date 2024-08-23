#!/usr/bin/env python3
"""
Measure the total execution time for wait_n(n, max_delay),
and return the average time per coroutine.

Args:
    n (int): Number of times to spawn wait_random.
    max_delay (int): Maximum delay value to pass to wait_random.

Returns:
    float: Average time per coroutine.
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total execution time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time/n)
