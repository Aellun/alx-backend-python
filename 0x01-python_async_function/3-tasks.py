#!/usr/bin/env python3

'''function (do not create an async function,
    use the regular function syntax to do this)
    task_wait_random that takes an integer max_delay
    and returns a asyncio.Task'''

import asyncio
from typing import Any

# Import wait_random from 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random
    with the given max_delay.

    Args:
        max_delay (int): Maximum delay for the wait_random call.

    Returns:
        asyncio.Task: The asyncio task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
