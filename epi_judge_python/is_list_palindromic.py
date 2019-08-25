from test_framework import generic_test
from list_node import ListNode


# def is_linked_list_a_palindrome(L):
#     slow = fast = L

#     while fast and fast.next:
#         slow, fast = slow.next, fast.next.next

#     first_half_head, second_half_head = L, reverse_linked_list(slow)

#     while first_half_head is not slow:
#         if first_half_head.data != second_half_head.data:
#             return False

#         first_half_head, second_half_head = first_half_head.next, second_half_head.next

#     return True


# def reverse_linked_list(head):
#     prev, cur = None, head

#     while cur:
#         nxt = cur.next
#         cur.next = prev
#         prev = cur
#         cur = nxt

#     return prev


def is_linked_list_a_palindrome(L):
    # Find the second half
    slow, fast = L, L

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Slow.next is the second half
    first_half, second_half = L, reverse_linked_list(slow)

    while first_half is not slow:
        if first_half.data != second_half.data:
            return False

        first_half, second_half = first_half.next, second_half.next

    return True


def reverse_linked_list(L):
    dummy_head = ListNode(0, L)

    while L and L.next:
        temp = L.next
        L.next = temp.next
        temp.next = dummy_head.next
        dummy_head.next = temp

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
