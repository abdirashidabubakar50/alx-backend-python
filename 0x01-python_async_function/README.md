Async IO in Python

Async IO is abit lesser know than it's tried-and-true cousins., multiprocessing and threading.

Parallelism consists of performing multiple operations at the same time. Multiprocessing - is a means to effect parallelism, and it entails spreading tasks over a computer's central processing units. Multiprocessing is well-suited for cpu-bound tasks:

Concurrency - is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner.

Threading - is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading. Threading is better for IO-bound tasks. To recap the above, concurrency encompasses both multiprocessing(ideal for cpu-bound tasks) and threading. Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency.

