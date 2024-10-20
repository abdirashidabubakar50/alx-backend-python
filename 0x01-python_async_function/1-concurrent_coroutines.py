wait_random = __import__('0-basic_async_syntax').wait_random


import asyncio

async def wait_n(n: int, max_delay: int):
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