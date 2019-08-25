from test_framework import generic_test
import itertools

from sorted_arrays_merge import merge_sorted_arrays


def sort_k_increasing_decreasing_array(A):
    sorted_arrays = []
    INC, DEC = range(2)
    sub_array_type = INC
    start_idx = 0

    for i in range(1, len(A) + 1):
        if i == len(A) or (sub_array_type == INC and A[i] < A[i - 1]) or (sub_array_type == DEC and A[i] > A[i - 1]):
            sorted_arrays.append(
                A[start_idx: i][::-1 if sub_array_type == DEC else 1])
            start_idx = i
            sub_array_type = INC if sub_array_type == DEC else DEC

    return merge_sorted_arrays(sorted_arrays)


def find_the_max_rank(routes, cities):


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
