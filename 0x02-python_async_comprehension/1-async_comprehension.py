#!/usr/bin/env python3
'''Import async_generator from the previous task
    and then write a coroutine called async_comprehension
    that takes no arguments.
'''
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collects 10 random numbers from async_generator using asynchronous
    comprehension.

    This coroutine will use asynchronous comprehension to gather 10 numbers
    from the async_generator coroutine and return them as a list.

    Returns:
        list: A list containing 10 random numbers between 0 and 10.
    """
    # Use asynchronous comprehension to collect 10 numbers from async_generator
    numbers = [number async for number in async_generator()]
    return numbers
