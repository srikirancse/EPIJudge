from test_framework import generic_test
from list_node import ListNode
from insert_in_list import insert_after

def merge_two_sorted_lists(L1, L2):
    res = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        
        else:
            tail.next = L2
            L2 = L2.next

        tail = tail.next

    tail.next = L1 or L2
    return res.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
