from random import randint
from heapq import heapreplace, heapify
import array_gen as ag
import time


def test_heapreplace():
    for size in ag.list_sizes:
        l_unsorted = ag.generate_list(ag.Ordering.Unsorted, size)
        l_sorted = ag.generate_list(ag.Ordering.Sorted, size)
        l_revsorted = ag.generate_list(ag.Ordering.RevSorted, size)

        heapify(l_unsorted)
        heapify(l_sorted)
        heapify(l_revsorted)

        value = randint(0, size)

        start_time_un = time.perf_counter()
        heapreplace(l_unsorted, value)
        end_time_un = time.perf_counter()
        elapsed_un = end_time_un - start_time_un

        start_time = time.perf_counter()
        heapreplace(l_sorted, value)
        end_time = time.perf_counter()
        elapsed = end_time - start_time

        start_time_rev = time.perf_counter()
        heapreplace(l_revsorted, value)
        end_time_rev = time.perf_counter()
        elapsed_rev = end_time_rev - start_time_rev

        print(f"Time of {elapsed_un} for unsorted size {size}")
        print(f"Time of {elapsed} for sorted size {size}")
        print(f"Time of {elapsed_rev} for revsorted size {size}")
