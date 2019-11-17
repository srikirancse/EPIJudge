from test_framework import generic_test
from bisect import bisect_left


def intersect_two_sorted_arrays(A, B):
    a_i, b_i = 0, 0
    result = []

    while a_i < len(A) and b_i < len(B):
        if A[a_i] < B[b_i]:
            a_i += 1

        elif B[b_i] < A[a_i]:
            b_i += 1

        else:
            if (a_i == 0 or A[a_i] != A[a_i - 1]):
                result.append(A[a_i])

            a_i += 1
            b_i += 1

    return result

        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
