from test_framework import generic_test


# def apply_permutation(perm, A):
#     for i in range(len(A)):
#         pointer = i

#         while perm[pointer] >= 0:
#             A[i], A[perm[pointer]] = A[perm[pointer]], A[i]
#             temp = perm[pointer]
#             perm[pointer] -= len(A)
#             pointer = temp

#     return A


def apply_permutation(perm, A):
    for i in range(len(A)):
        cur = i

        while perm[cur] > 0:
            A[i], A[perm[cur]] = A[perm[cur]], A[i]
            temp = perm[cur]
            perm[cur] -= len(A)
            cur = temp
        
    return A
            




print(apply_permutation([2, 0 , 1, 3], ['a', 'b', 'c', 'd']))


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
