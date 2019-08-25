from test_framework import generic_test


def can_reach_end(A):
    farthest_reach_so_far, end = 0, len(A) - 1
    i = 0

    while i <= farthest_reach_so_far and i <= end:
        farthest_reach_so_far = max(farthest_reach_so_far, A[i] + i)
        i += 1

    
    return farthest_reach_so_far >= end


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
