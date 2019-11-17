from test_framework import generic_test


def longest_contained_range(A):
    unprocessed_entries = set(A)
    result = 0

    while unprocessed_entries:
        a = unprocessed_entries.pop()
        local_max = 1
        # Lower bound
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            local_max += 1
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1
        
        # Upper bound
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            local_max += 1
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        result = max(result, local_max)

    return result




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
