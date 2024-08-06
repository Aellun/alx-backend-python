#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10)
named wait_random that waits for a random
delay between 0 and max_delay.

This script defines an asynchronous generator coroutine called
`async_generator`.

The `async_generator` coroutine:
1. Loops 10 times.
2. Asynchronously waits for 1 second in each iteration.
3. Yields a random float number between 0 and 10 in each iteration.

Dependencies:
- asyncio: For asynchronous operations and sleep functionality.
- random: For generating random float numbers.
"""

import asyncio
import random
from typing import AsyncGenerator


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously wait for a random delay between 0 and max_delay
        seconds and return the delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronous generator that yields 10 random float
        numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
