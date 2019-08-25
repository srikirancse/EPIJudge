from test_framework import generic_test


def smallest_nonconstructible_value(A):
    smallest_nonconstructible_value = 0

    for a in sorted(A):
        if smallest_nonconstructible_value + 1 < a:
            break
        smallest_nonconstructible_value += a
    return smallest_nonconstructible_value + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
