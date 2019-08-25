from test_framework import generic_test
import collections


def binary_tree_depth_order(tree):
    result = []

    if not tree:
        return result

    queue = [tree]

    while queue:
        result.append([cur.data for cur in queue])
        queue = [child for cur in queue for child in (
            cur.left, cur.right) if child]

    return [list(reversed(r)) for r in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
