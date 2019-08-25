from test_framework import generic_test

import operator
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def find_kth(comp):
        def partition_around_pivot(pivot_idx, left, right):
            pivot_value = A[pivot_idx]
            # Pivot is moved to the end
            A[right], A[pivot_idx] = A[pivot_idx], A[right]
            new_pivot_idx = left

            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[new_pivot_idx], A[right] = A[right], A[new_pivot_idx]
                
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            pivot = random.randint(left, right)
            new_pivot = partition_around_pivot(pivot, left, right)

            if new_pivot == k - 1:
                return A[new_pivot]
            elif new_pivot > k - 1:
                right = new_pivot - 1
            else:
                left = new_pivot + 1

    return find_kth(operator.gt)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
