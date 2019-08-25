from test_framework import generic_test
from list_node import ListNode
from insert_in_list import array_to_linked_list


def reverse_sublist(L, start, finish):
    pre_head = tail = ListNode(0, L)

    # Search for the start node
    for _ in range(1, start):
        tail = tail.next

    # Now the tail points to the node before the start node

    sublist_tail = tail.next  # Sublist tail starts with the start node

    for _ in range(finish - start):
        temp = sublist_tail.next
        sublist_tail.next = temp.next
        temp.next = tail.next
        tail.next = temp

    return pre_head.next


print(reverse_sublist(array_to_linked_list([1, 2, 3, 4, 5, 6, 7]), 3, 6))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
