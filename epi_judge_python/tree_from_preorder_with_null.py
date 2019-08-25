import functools


from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder):
    def construct_binary_tree(preorder_iter):
        root = next(preorder_iter)

        if not root:
            return None

        node = BinaryTreeNode(root)
        node.left = construct_binary_tree(preorder_iter)
        node.right = construct_binary_tree(preorder_iter)

        return node

    return construct_binary_tree(iter(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
