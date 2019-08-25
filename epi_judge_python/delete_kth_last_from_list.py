from test_framework import generic_test
from list_node import ListNode
from insert_in_list import array_to_linked_list


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)

    first = L

    for _ in range(k):
        first = first.next

    second = dummy_head

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy_head.next


remove_kth_last(array_to_linked_list([1, 2]), 2)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
