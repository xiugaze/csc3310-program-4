from random import randint
from heapq import heapreplace, heapify
import array_gen as ag
import time


def test_heapreplace():
    for size in ag.list_sizes:
        l = ag.generate_list(ag.Ordering.Sorted, size)
        heapify(l)
        value = randint(0, size)
        start_time = time.perf_counter()
        heapreplace(l, value)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"Time of {elapsed} for size {size}")
