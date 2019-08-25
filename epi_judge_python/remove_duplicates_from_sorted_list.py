from test_framework import generic_test
from list_node import ListNode
from insert_in_list import array_to_linked_list


def remove_duplicates(L):
    dummy_head = ListNode(0, L)

    while L:
        next_distinct = L.next

        while next_distinct and L.data == next_distinct.data:
            next_distinct = next_distinct.next

        L.next = next_distinct
        L = next_distinct

    return dummy_head.next


print(remove_duplicates(array_to_linked_list(
    [-8, -8, -7, -5, -5, -4, 1, 2, 2, 2, 2, 4, 5, 5, 7, 7])))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
