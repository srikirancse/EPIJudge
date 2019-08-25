from test_framework import generic_test
import bintrees


def find_closest_elements_in_sorted_arrays(sorted_arrays):
    a = bintrees.RBTree()
    closest_length_so_far = 0
    for i, sorted_array in sorted_arrays:
        it = iter(sorted_array)
        first_min = next(iter, None)
        if first_min is not None:
            a.insert((first_min, i), it)

    while True:
        min_value, min_idx = a.min_key()
        max_value = a.max_key()[0]

        closest_length_so_far = min(closest_length_so_far, max_value - min_value)

        min_iter = a.pop_min()[1]
        next_value = next(min_iter, None)
        if next_value is None:
            return closest_length_so_far
        a.insert((next_value, min_idx), min_iter)
        
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
