from test_framework import generic_test

import heapq


def merge_sorted_arrays(sorted_arrays):
    sorted_arrays_iters = [iter(i) for i in sorted_arrays]
    min_heap = [(next(it, None), i)
                for i, it in enumerate(sorted_arrays_iters)]
    heapq.heapify(min_heap)

    result = []

    while min_heap:
        smallest_entry, smallest_i = heapq.heappop(min_heap)
        result.append(smallest_entry)
        next_element = next(sorted_arrays_iters[smallest_i], None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_i))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
