#!/usr/bin/env python3
'''Import async_comprehension from the previous file
    and write a measure_runtime coroutine that will
    execute async_comprehension four times in parallel
    using asyncio.gather.
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for executing async_comprehension
    four times in parallel.

    This coroutine will execute async_comprehension
    four times concurrentlyusing
    asyncio.gather and measure the total runtime of these executions.

    Returns:
        float: The total runtime of executing async_comprehension four times.
    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
