import functools
import collections

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
    LCA_Status = collections.namedtuple(
        'LCA_Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(tree):
        if not tree:
            return LCA_Status(0, None)

        left_status = lca_helper(tree.left)
        right_status = lca_helper(tree.right)

        if left_status.num_target_nodes == 2:
            return left_status

        if right_status.num_target_nodes == 2:
            return right_status

        new_num_tree_nodes = right_status.num_target_nodes + \
            left_status.num_target_nodes + [node1, node0].count(tree)

        return LCA_Status(new_num_tree_nodes, tree if new_num_tree_nodes == 2 else None)

    return lca_helper(tree).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
