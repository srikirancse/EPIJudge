from test_framework import generic_test
import itertools


def find_maximum_subarray(nums):
    cur_sum = max_sum = 0
    for i in range(len(nums)):
        cur_sum = max(nums[i], cur_sum + nums[i])
        max_sum = max(max_sum, cur_sum)

    return max_sum


print(find_maximum_subarray([-1]))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
