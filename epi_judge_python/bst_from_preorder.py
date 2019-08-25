from test_framework import generic_test
from bst_node import BstNode


def rebuild_bst_from_preorder_easy(preorder_sequence):
    if not preorder_sequence:
        return None

    transition_pont = next((i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]), len(preorder_sequence))

    return BstNode(preorder_sequence[0], rebuild_bst_from_preorder(preorder_sequence[1:transition_pont]), 
                    rebuild_bst_from_preorder(preorder_sequence[transition_pont:]))

def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None

    def rebuild_bst_from_preorder_helper(lower, upper):
        if current_node[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[current_node[0]]

        if not lower <= root <= upper:
            return None

        current_node[0] += 1

        left_child = rebuild_bst_from_preorder_helper(lower, root)
        right_child = rebuild_bst_from_preorder_helper(root, upper)

        return BstNode(root, left_child, right_child)

    current_node = [0]

    return rebuild_bst_from_preorder_helper(float('-inf'), float('inf'))

rebuild_bst_from_preorder([3, 2, 1, 5, 4, 6])

        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
