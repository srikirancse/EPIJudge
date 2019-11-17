from test_framework import generic_test

def find_nearest_repetition(paragraph):
    last_occurrence_map, nearest_repeated_distance = {}, float('inf')
    for idx, word in enumerate(paragraph):
        if word in last_occurrence_map:
            nearest_repeated_distance = min(nearest_repeated_distance, idx - last_occurrence_map[word])
        last_occurrence_map[word] = idx
    return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
