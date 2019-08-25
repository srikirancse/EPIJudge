from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    recent_occurrence = {}
    dup_free_start_idx = 0
    longest_subarray_length = 0

    for index, entry in enumerate(A):
        if entry in recent_occurrence and recent_occurrence[entry] >= dup_free_start_idx:
            longest_subarray_length = max(longest_subarray_length, index - dup_free_start_idx)
            dup_free_start_idx = recent_occurrence[entry] + 1
        recent_occurrence[entry] = index
    return max(longest_subarray_length, len(A) - dup_free_start_idx)


longest_subarray_with_distinct_entries([1, 2, 1, 3, 1, 2, 1])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
