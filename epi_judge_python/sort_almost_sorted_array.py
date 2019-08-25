from test_framework import generic_test

import heapq
import itertools


def sort_approximately_sorted_array(sequence, k):
    min_heap = []

    # Push the first k elements into the heap
    min_heap = list(itertools.islice(sequence, k))
    heapq.heapify(min_heap)

    # Push and pop the remaining elements and add it to the result
    result = list(map(lambda x: heapq.heappushpop(min_heap, x), sequence))

    # Pop the remaining elements into the result
    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result


sort_approximately_sorted_array([3, -1, 2, 6, 4, 5, 8], 2)


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
