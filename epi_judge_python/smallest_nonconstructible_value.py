from test_framework import generic_test


def smallest_nonconstructible_value(A):
    A.sort()
    accumulated_sum = 0
    for a in A:
        if a > accumulated_sum + 1:
            break

        accumulated_sum += a

    return accumulated_sum + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
