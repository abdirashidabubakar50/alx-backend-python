#!/usr/bin/env python3
"""
This script defines an asynchronous coroutine that takes in
an integer argument(max_delay) with a default value of 10
with the name wait_random that waits for a raondom delay between
0 and max_delay and returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and max_delay seconds
    and returns the delay"""

    # random float between 0 and max_delay
    delay = random.uniform(0, max_delay)

    # Asynchronous sleep for the delay function
    await asyncio.sleep(delay)
    return delay
