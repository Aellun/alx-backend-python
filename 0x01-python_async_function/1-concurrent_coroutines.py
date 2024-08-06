#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehension
over async_generator, then return the 10 random numbers.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

# Import async_generator from the module 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Collect 10 random numbers from async_generator and return them.

    This coroutine uses an asynchronous comprehension to gather values
    yielded by async_generator into a list and returns this list.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Await all tasks and collect results
    delays = await asyncio.gather(*tasks)

    # Sort the delays without using sort()
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
