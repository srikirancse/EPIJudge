from test_framework import generic_test
import math


def square_root(x):
    start, end = (1.0, x) if x > 1.0 else (x, 1.0)

    while not math.isclose(start, end):
        mid = (start + end) / 2

        candidate = mid * mid

        if candidate > x:
            end = mid

        else:
            start = mid

    return start


def maxAreaOfIsland(grid):
    def dfs_area(i, j):
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid)) or grid[i][j] != 1:
            return 0

        grid[i][j] = -1

        return 1 + sum([dfs_area(i, j + 1), dfs_area(i + 1, j), dfs_area(i - 1, j), dfs_area(i, j - 1)])

    return max([dfs_area(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 1])


maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
