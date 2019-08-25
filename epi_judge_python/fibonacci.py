from test_framework import generic_test


def fibonacci(n):
    f1, f2 = 0, 1
    for _ in range(n):
        f = f1 + f2
        f2, f1 = f1, f
    return f1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))
