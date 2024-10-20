#!/usr/bin/env python3
"""
This script defines a function that measures the runtime for wait_n and
returns total_time / n
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for running wait_n(n, max_delay)
    and returns the average time per coroutine

    Args:
        n: The number of coroutines to run
        max_delay: the maximum delay for each coroutine

    Returns:
        float: The average time per coroutine
    """
    start_time = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.perf_counter()

    total_time = end_time - start_time

    return total_time / n
