#!/usr/bin/env python3

'''function task_wait_n. The code is nearly identical to wait_n except
    task_wait_random is being called.'''

import asyncio
from typing import List

# Import task_wait_random from task_wait_random.py
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay and
    return a list of all delays in ascending order.

    Args:
        n (int): Number of times to spawn the task_wait_random coroutine.
        max_delay (int): Maximum delay for each task_wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Await all tasks and collect results
    delays = await asyncio.gather(*tasks)

    # Sort the delays without using sort()
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
