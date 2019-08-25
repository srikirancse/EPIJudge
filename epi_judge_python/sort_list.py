from test_framework import generic_test
from list_node import ListNode
from sorted_lists_merge import merge_two_sorted_lists


def stable_sort_list(L):
    if not L or not L.next:
        return L

    pre_slow, slow, fast = None, L, L

    while fast and fast.next:
        pre_slow, slow, fast = slow, slow.next, fast.next.next

    pre_slow.next = None

    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))

def insertion_sort(head):
    dummy_head = ListNode(0)
    dummy_head.next = head

    while head and head.next:
        if head.val > head.next.val:
            # We encountered a node which is smaller than the last element of the sorted sublist
            pre, target = dummy_head, head.next

            while target.val > pre.next.val:
                pre = pre.next

            temp, pre.next, head.next = pre.next, target, target.next

            target.next = temp

        else:
            head = head.next

    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
