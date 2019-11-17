from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    last_occurrence_map = {}
    start_index = 0
    longest_distance = 0

    for i, word in enumerate(A):
        if word in last_occurrence_map and last_occurrence_map[word] >= start_index:
            longest_distance = max(longest_distance, i - start_index)
            start_index = last_occurrence_map[word] + 1

        last_occurrence_map[word] = i
        
    return max(longest_distance, len(A) - start_index)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
