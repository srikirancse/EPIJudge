import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    len0, l0_iter, len1, l1_iter = 0, l0, 0, l1

    while l0_iter or l1_iter:
        if l0_iter:
            len0 += 1
            l0_iter = l0_iter.next

        if l1_iter:
            len1 += 1
            l1_iter = l1_iter.next

    if len0 > len1:
        l0, l1 = l1, l0

    for _ in range(abs(len1 - len0)):
        l1 = l1.next

    while l1 and l0:
        if l1 is l0:
            return l1
        l1, l0 = l1.next, l0.next

    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
