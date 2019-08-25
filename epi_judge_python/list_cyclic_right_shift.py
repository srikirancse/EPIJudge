from test_framework import generic_test
from insert_in_list import array_to_linked_list


# def cyclically_right_shift_list(L, k):
#     if not L or k == 0:
#         return L

#     it, list_len, tail = L, 0, None

#     while it:
#         list_len += 1
#         if not it.next:
#             tail = it
#         it = it.next

#     k %= list_len

#     if k == 0:
#         return L

#     new_head_idx = list_len - k

#     it = L
#     for _ in range(1, new_head_idx):
#         it = it.next

#     new_head, it.next, tail.next = it.next, None, L

#     return new_head


def cyclically_right_shift_list(L, k):
    if not L or k == 0:
        return L

    list_iter, tail, n = L, None, 0
    while list_iter:
        n += 1
        if not list_iter.next:
            tail = list_iter
        list_iter = list_iter.next

    k %= n
    if k == 0:
        return L

    list_iter = L

    for _ in range(1, n - k):
        list_iter = list_iter.next

    new_first_head = list_iter.next
    new_last_node = list_iter
    new_last_node.next = None
    tail.next = L

    return new_first_head


print(cyclically_right_shift_list(array_to_linked_list(
    [2, 3, 5, 6, 10, 9, 1, 11, 4, 8, 7]), 9))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
