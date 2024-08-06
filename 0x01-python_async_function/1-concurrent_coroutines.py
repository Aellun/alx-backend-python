#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehension
over async_generator, then return the 10 random numbers.
"""

from typing import List

# Import async_generator from the module
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from async_generator and return them.

    This coroutine uses an asynchronous comprehension to gather values
    yielded by async_generator into a list and returns this list.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    # Collect random numbers using async comprehension
    results = [i async for i in async_generator()]
    return results
