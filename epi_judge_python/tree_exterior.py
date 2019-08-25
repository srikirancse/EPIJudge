import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree):
    if not tree:
        return []

    def is_leaf_node(tree):
        return not tree.left and not tree.right

    def left_exterior(tree, is_boundary):
        if not tree:
            return []

        return ([tree] if is_boundary or is_leaf_node(tree) else []) + left_exterior(tree.left, is_boundary) + left_exterior(tree.right, is_boundary and not tree.left)

    def right_exterior(tree, is_boundary):
        if not tree:
            return []

        return right_exterior(tree.left, is_boundary and not tree.right) + right_exterior(tree.right, is_boundary) + ([tree] if is_boundary or is_leaf_node(tree) else [])

    return [tree] + left_exterior(tree.left, is_boundary=True) + right_exterior(tree.right, is_boundary=True)


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
