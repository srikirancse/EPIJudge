from test_framework import generic_test


def find_nearest_repetition(paragraph):
    min_pair_distance = float('inf') # Setting it to a maximum value
    latest_occurrence_table = {}
    for index, word in enumerate(paragraph):
        if word in latest_occurrence_table:
            min_pair_distance = min(index - latest_occurrence_table[word], min_pair_distance)
        latest_occurrence_table[word] = index


    return min_pair_distance if min_pair_distance != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
