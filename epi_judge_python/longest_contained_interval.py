from test_framework import generic_test


def longest_contained_range(A):
    a_set = set(A)
    max_length = 0

    while a_set:
        a = a_set.pop()
        cur_length = 1

        lower_bound = a - 1
        while lower_bound in a_set:
            a_set.remove(lower_bound)
            lower_bound -= 1
            cur_length += 1
        
        upper_bound = a + 1
        while upper_bound in a_set:
            a_set.remove(upper_bound)
            upper_bound += 1
            cur_length += 1

        max_length = max(max_length, cur_length)

    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
