#!/usr/bin/env python3

wait_random = __import__('0-basic_async_syntax').wait_random
"""
This script defines a function that executes multiple coroutines
at the same time with async
"""

import asyncio
from typing  import List


async def wait_n(n: int, max_delay: int) -> List:
    """
    Run n coroutines concurrently, each waiting for a random delay
    up to 'max_delay' seconds. Return the sorted list of delays

    Args:
        n (int): The number of coroutines to run.
        max_delay(int): The maximum value (in seconds) for the random delay

        Returns:
            list[float]: A list of delays in ascending order.
    """
    delay = [wait_random(max_delay) for _ in range(n)]

    # gather results from the  coroutines
    completed_delays = await asyncio.gather(*delay)

    #create a new list to hold the  sorted delays
    sorted_delays = []

    # insert delays in sorted order
    for delay in completed_delays:
        index = 0;
        while index < len(sorted_delays) and sorted_delays[index] < delay:
            index += 1
        sorted_delays.insert(index, delay)
    
    return sorted_delays