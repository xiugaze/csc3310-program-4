from array_gen import *
import numpy as np
from scipy.stats import linregress
import heapq

list_sizes = [100, 1000, 2500, 10000, 20000, 30000, 50000, 100000, 1000000, 10000000, 100000000] 
sorted_times = []
rev_times = []
rand_times = []

if __name__ == "__main__":
    for size in list_sizes:
        l = generate_list(Ordering.Sorted, size)
        sorted_times.append(benchmark(heapq.heapify, l))
    for size in list_sizes:
        l = generate_list(Ordering.Unsorted, size)
        rand_times.append(benchmark(heapq.heapify, l))
    for size in list_sizes:
        l = generate_list(Ordering.RevSorted, size)
        rev_times.append(benchmark(heapq.heapify, l))

    m, b, _, _, _ = linregress(np.log(list_sizes), np.log(sorted_times))
    print(f"Sorted case m: {m}, b: {b}")
    m, b, _, _, _ = linregress(np.log(list_sizes), np.log(rev_times))
    print(f"Unsorted case m: {m}, b: {b}")
    m, b, _, _, _ = linregress(np.log(list_sizes), np.log(rand_times))
    print(f"Random case m: {m}, b: {b}")

