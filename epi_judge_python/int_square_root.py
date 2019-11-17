from test_framework import generic_test


def square_root(k):
    start, end = 0, k

    while start <= end:
        mid = (start + end) // 2
        candidate = mid * mid

        if candidate > k:
            end = mid - 1

        else:
            start = mid + 1

    return start - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
