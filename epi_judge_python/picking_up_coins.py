from test_framework import generic_test


def maximum_revenue(coins):
    def compute_max_revenue_for_range(a, b):
        if a > b:
            return 0

        if max_revenue_for_range[a][b] == 0:
            picking_a = coins[a] + min(compute_max_revenue_for_range(a + 2, b), compute_max_revenue_for_range(a + 1, b - 1))
            picking_b = coins[b] + min(compute_max_revenue_for_range(a + 1, b - 1), compute_max_revenue_for_range(a, b - 2))
            max_revenue_for_range[a][b] = max(picking_a, picking_b)

        return max_revenue_for_range[a][b]

    max_revenue_for_range = [[0] * len(coins) for _ in coins]
    return compute_max_revenue_for_range(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
