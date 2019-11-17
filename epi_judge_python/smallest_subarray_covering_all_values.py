import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure  # keep
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph, keywords):
    key_word_sequence = {v: k for k, v in enumerate(keywords)}
    last_occurrence = [-1] * len(keywords)
    smallest_distance = [float('inf')] * len(keywords)
    smallest_length = float('inf')
    result = Subarray(-1, -1)

    for i, word in enumerate(paragraph):
        if word in key_word_sequence:
            keyword_idx = key_word_sequence[word]
            if keyword_idx == 0:
                smallest_distance[0] = 1

            elif smallest_distance[keyword_idx - 1] != float('inf'):
                smallest_distance[keyword_idx] = (
                    i - last_occurrence[keyword_idx - 1]) + smallest_distance[keyword_idx - 1]
            last_occurrence[keyword_idx] = i

            if keyword_idx == len(key_word_sequence) - 1 and smallest_distance[-1] < smallest_length:
                smallest_length = smallest_distance[-1]
                result = Subarray(i - smallest_length + 1, i)

    return result


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
