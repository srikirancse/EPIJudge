from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree):
    BinaryTreeStatusWithHeight = collections.namedtuple(
        'BinaryTreeStatusWithHeight', ('status', 'height'))

    if not tree:
        return True

    def is_balanced_binary_tree_helper(tree):
        if not tree:
            return BinaryTreeStatusWithHeight(True, 0)

        left_status = is_balanced_binary_tree_helper(tree.left)
        right_status = is_balanced_binary_tree_helper(tree.right)

        is_balanced = left_status.status and right_status.status
        height_diff = abs(left_status.height - right_status.height)
        new_height = 1 + max(left_status.height, right_status.height)

        if height_diff > 1:
            return BinaryTreeStatusWithHeight(False, 0)

        return BinaryTreeStatusWithHeight(is_balanced, new_height)

    return is_balanced_binary_tree_helper(tree).status


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
