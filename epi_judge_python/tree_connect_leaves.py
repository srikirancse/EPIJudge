import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from binary_tree_node import BinaryTreeNode


def reconstruct_binary_tree(preorder):
    def construct_binary_tree(preorder_iter):
        root = next(preorder_iter, None)
        if not root:
            return None
        node = BinaryTreeNode(root)
        node.left = construct_binary_tree(preorder_iter)
        node.right = construct_binary_tree(preorder_iter)

        return node

    return construct_binary_tree(iter(preorder))


def create_list_of_leaves(tree):
    if not tree:
        return []

    if not tree.left and not tree.right:
        return [tree]

    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)


class Solution:
    def subtreeWithAllDeepest(self, root):
        self.max_depth = -1
        self.result = None

        def subtreeWithAllDeepestHelper(root, depth):
            if not root:
                return -1
            left_depth = subtreeWithAllDeepestHelper(root.left, depth + 1)
            right_depth = subtreeWithAllDeepestHelper(root.right, depth + 1)

            max_depth = max(left_depth, right_depth)

            if max_depth >= self.max_depth:
                self.max_depth = max_depth
                self.result = root

            return depth

        subtreeWithAllDeepestHelper(root, 0)
        return self.result


solution = Solution()

print(solution.subtreeWithAllDeepest(reconstruct_binary_tree(
    [1, 1, None, 2, None, None, 3, None, None])))


@enable_executor_hook
def create_list_of_leaves_wrapper(executor, tree):
    result = executor.run(functools.partial(create_list_of_leaves, tree))

    if any(x is None for x in result):
        raise TestFailure("Result list can't contain None")
    return [x.data for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_connect_leaves.py",
                                       "tree_connect_leaves.tsv",
                                       create_list_of_leaves_wrapper))
