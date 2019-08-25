import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from is_list_cyclic import has_cycle
from do_terminated_lists_overlap import overlapping_no_cycle_lists
from list_node import ListNode


def overlapping_lists(l0, l1):
    # Store the first node of the cycle
    root0, root1 = has_cycle(l0), has_cycle(l1)

    # Find the length of a list
    def list_len(node1, node2):
        count = 0
        while node1 is not node2:
            node1 = node1.next
            count += 1

        return count

    # Only one list has cycles means both never overlap
    if (root0 and not root1) or (root1 and not root0):
        return None

    # Both don't have cycles - we can reuse the non overlapping cycles code
    if not root0 and not root1:
        return overlapping_no_cycle_lists(l0, l1)

    # Both the cycles have loop

    # Both cycles are different
    if root0 is not root1:
        return None

    # Check if the first overlapping node appears before the cycle
    len0 = list_len(l0, root0)
    len1 = list_len(l1, root1)

    if len0 > len1:
        l0, l1 = l1, l0
        root0, root1 = root1, root0

    for _ in range(abs(len0 - len1)):
        l1 = l1.next

    while l0 is not l1 or l0 is not root0 or l1 is not root1:
        l0 = l0.next
        l1 = l1.next

    return l0 if l0 is l1 else root0


# def overlapping_lists(l0, l1):
#     # Store the first cycle node on both the lists
#     cycle0, cycle1 = has_cycle(l0), has_cycle(l1)

#     def non_cyclic_len(l, c):
#         count = 0
#         while l is not c:
#             l = l.next
#             count += 1

#         return count

#     # If only one cycle has the loop then we don't have any common node that is reachable
#     if (cycle0 and not cycle1) or (not cycle0 and cycle1):
#         return None

#     # If there are no cycles then we can reuse the no cycle code
#     if not cycle0 and not cycle1:
#         return overlapping_no_cycle_lists(l0, l1)

#     # Both cycles are different also makes it impossible to reach to the common node
#     if cycle0 is not cycle1:
#         return None

#     # Now we know that both have same cycles

#     # Now we find the length of the list to get to the cycle node
#     len0, len1 = non_cyclic_len(l0, cycle0), non_cyclic_len(l1, cycle1)

#     if len0 > len1:
#         l1, l0 = l0, l1
#         cycle1, cycle0 = cycle0, cycle1

#     for _ in range((abs(len1 - len0))):
#         l1 = l1.next

#     while l1 is not l0 or l0 is not cycle0 or l1 is not cycle1:
#         l0 = l0.next
#         l1 = l1.next

#     return l0 if l0 is l1 else cycle0


overlapping_lists(ListNode(0), ListNode(1))


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
