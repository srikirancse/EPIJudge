from test_framework import generic_test


# def next_permutation(perm):
#     first_un_ordered_index = None

#     for i in reversed(range(1, len(perm))):
#         if perm[i - 1] < perm[i]: 
#             first_un_ordered_index = i - 1
#             break

#     if first_un_ordered_index == None: return []

#     for i in reversed(range(first_un_ordered_index + 1, len(perm))):
#         if perm[i] > perm[first_un_ordered_index]:
#             perm[i], perm[first_un_ordered_index] = perm[first_un_ordered_index], perm[i]
#             break
    
#     perm[first_un_ordered_index + 1:] = reversed(perm[first_un_ordered_index + 1:])

#     return perm


def next_permutation(perm):
    first_un_ordered_index = None

    for i in reversed(range(1, len(perm))):
        if perm[i - 1] < perm[i]:
            first_un_ordered_index = i - 1
            break

    if first_un_ordered_index == None:
        return []

    for i in reversed(range(first_un_ordered_index + 1, len(perm))):
        if perm[i] > perm[first_un_ordered_index]:
            perm[i], perm[first_un_ordered_index] = perm[first_un_ordered_index], perm[i]
            break

    perm[first_un_ordered_index + 1:] = reversed(perm[first_un_ordered_index + 1:])

    return perm

    



next_permutation([1, 3, 2])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
