import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure  # keep
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_sequentially_covering_subset(paragraph, keywords):
    keyword_sequence = { v: k for k, v in enumerate(keywords) }
    subarray_length = [float('inf')] * len(keywords)
    last_occurrence = [-1] * len(keywords)
    shortest_distance = float('inf')
    result = Subarray(-1, -1)

    for index, word in enumerate(paragraph):
        if word in keyword_sequence:
            keyword_idx = keyword_sequence[word]
            if keyword_idx == 0:
                subarray_length[0] = 1

            elif subarray_length[keyword_idx - 1] != float('inf'):
                new_distance = (index - last_occurrence[keyword_idx - 1]) + subarray_length[keyword_idx - 1]
                subarray_length[keyword_idx] = new_distance

            last_occurrence[keyword_idx] = index

            if keyword_idx == len(keywords) - 1 and subarray_length[-1] < shortest_distance:
                # If the new distance is greater less than the old distance then we need to update it.
                shortest_distance = subarray_length[-1]
                result = Subarray(index - shortest_distance + 1, index)


    return result

print(find_smallest_sequentially_covering_subset(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "2", "4", "6", "1", "0", "1", "0", "1", "0", "3", "2", "1", "0"], ["0", "2", "9", "4", "6"]))


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
