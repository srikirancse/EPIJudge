from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    def compute_binomial_coefficient_helper(n, k):
        if n == k or k == 0:
            return 1

        if dp[n][k] == 0:
            without_last_element = compute_binomial_coefficient_helper(n - 1, k)
            with_last_element = compute_binomial_coefficient_helper(n - 1, k - 1)
            dp[n][k] = with_last_element + without_last_element

        return dp[n][k]

    return compute_binomial_coefficient_helper(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
