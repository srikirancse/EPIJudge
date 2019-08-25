from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step):
    def compute_number_of_ways_to_top(top, maximum_step):
        if top <= 1:
            return 1
        if dp[top] == 0:
            dp[top] = sum(compute_number_of_ways_to_top(top - i, maximum_step) for i in range(1, min(maximum_step, top) + 1))
        return dp[top]
    dp = [0] * (top + 1)

    return compute_number_of_ways_to_top(top, maximum_step)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
