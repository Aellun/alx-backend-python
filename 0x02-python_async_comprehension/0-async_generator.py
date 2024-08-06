#!/usr/bin/env python3

'''coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    Use the random module
'''

import asyncio
import random
from typing import Generator


async def async_generator():
    """
    Asynchronously generates 10 random numbers between 0 and 10.

    returns:
        float: A random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
