from test_framework import generic_test
from list_node import ListNode


def even_odd_merge(L):
    if not L or not L.next:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    nodes, turn = [even_dummy_head, odd_dummy_head], 0

    while L:
        nodes[turn].next = L
        L = L.next
        nodes[turn] = nodes[turn].next
        turn ^= 1

    nodes[1].next = None
    nodes[0].next = odd_dummy_head.next

    return even_dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
