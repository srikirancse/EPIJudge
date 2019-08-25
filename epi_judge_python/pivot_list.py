import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from list_node import ListNode


def list_pivoting(l, x):
    before_dummy, equal_dummy, after_dummy = ListNode(
        0), ListNode(0), ListNode(0)
    before_iter, equal_iter, after_iter = before_dummy, equal_dummy, after_dummy

    while l:
        if l.data < x:
            before_iter.next = l
            before_iter = before_iter.next

        elif l.data == x:
            equal_iter.next = l
            equal_iter = equal_iter.next

        else:
            after_iter.next = l
            after_iter = after_iter.next

        l = l.next

    after_iter.next = None
    equal_iter.next = after_dummy.next
    before_iter.next = equal_dummy.next

    return before_dummy.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
