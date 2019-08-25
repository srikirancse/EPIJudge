import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    def optimum_subject_to_capacity_helper(item, capacity):
        if item < 0:
            return 0

        if dp[item][capacity] == -1:
            value_with_this_item = 0 if items[item].weight > capacity else optimum_subject_to_capacity_helper(item - 1, capacity - items[item].weight) + items[item].value
            value_without_this_item = optimum_subject_to_capacity_helper(item - 1, capacity)

            dp[item][capacity] = max(value_with_this_item, value_without_this_item)

        return dp[item][capacity]

    dp = [[-1] * (capacity + 1) for _ in items]
    return optimum_subject_to_capacity_helper(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
