import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

import random

def random_subset(n, k):
    res = {}
    for i in range(k):
        r = (random.randint(i, n - 1))
        new_i_value = res.get(r, r)
        new_r_value = res.get(i, i)
        res[i] = new_i_value
        res[r] = new_r_value
    return [res[i] for i in range(k)]

print(random_subset(8, 4))

# def random_sampling(k ,A):
#     for i in range(k):
#         r = random.randint(i, len(A) - 1)
#         A[i], A[r] = A[r], A[i]

#     return A


def random_sampling(k ,A):
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[r], A[i] = A[i], A[r]

    return A

print(random_subset(8, 4))

@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0)
             for result in results], total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("random_subset.py", 'random_subset.tsv',
                                       random_subset_wrapper))
