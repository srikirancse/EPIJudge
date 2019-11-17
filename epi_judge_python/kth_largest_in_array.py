from test_framework import generic_test

import operator
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def find_kth(comp):
        def partition_around_pivot(pivot, start, end):
            pivot_element, new_pivot = A[pivot], start
            A[end], A[pivot] = A[pivot], A[end]

            for i in range(start, end):
                if comp(A[i], pivot_element):
                    A[new_pivot], A[i] = A[i], A[new_pivot]
                    new_pivot += 1

            A[new_pivot], A[end] = A[end], A[new_pivot]
            return new_pivot

        start, end = 0, len(A) - 1
        while start <= end:
            pivot = random.randint(start, end)
            new_pivot = partition_around_pivot(pivot, start, end)

            if new_pivot == k - 1:
                return A[new_pivot]

            elif new_pivot > k - 1:
                end = new_pivot - 1
            else:
                start = new_pivot + 1

    return find_kth(operator.gt)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
