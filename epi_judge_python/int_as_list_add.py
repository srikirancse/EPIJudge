from test_framework import generic_test
from list_node import ListNode
from insert_in_list import array_to_linked_list


# def add_two_numbers(L1, L2):
#     dummy_head = res_iter = ListNode(0)
#     carry = 0

#     while L1 or L2 or carry:
#         sum_digit = 0
#         if L1:
#             sum_digit += L1.data
#             L1 = L1.next
#         if L2:
#             sum_digit += L2.data
#             L2 = L2.next

#         if carry:
#             sum_digit += carry

#         res_iter.next = ListNode(sum_digit % 10)
#         res_iter = res_iter.next
#         carry = sum_digit // 10

#     while carry == 1:
#         res_iter.next = ListNode(1)

#     res_iter.next = None

#     return dummy_head.next


# print(add_two_numbers(array_to_linked_list(
#     [6, 7, 1, 9, 9]), array_to_linked_list([3, 3, 1, 7, 4, 4, 5, 3, 0, 5, 6, 5, 1, 7, 0, 1, 8, 5])))


def add_two_numbers(L1, L2):
    carry = 0

    len1, tail1, len2, tail2 = len_of_list(L1)[0], len_of_list(
        L1)[1], len_of_list(L2)[0], len_of_list(L2)[1]

    if len1 > len2:
        L1, L2 = L2, L1
        tail1, tail2 = tail2, tail1

    L2_iter = L2

    while L1 or L2_iter or carry:
        if not L1 and not L2_iter and carry:
            tail2.next = ListNode(1)
            carry = 0
            continue

        sum_digit = carry + (L1.data if L1 else 0) + \
            (L2_iter.data if L2_iter else 0)

        carry = sum_digit // 10
        sum_digit %= 10

        if L2_iter:
            L2_iter.data = sum_digit

        L1, L2_iter = L1.next if L1 else None, L2_iter.next if L2_iter else None

    return L2


def len_of_list(L):
    tail = None
    count = 0
    while L:
        count += 1
        if not L.next:
            tail = L
        L = L.next

    return [count, tail]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
