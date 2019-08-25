from test_framework import generic_test
import collections


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))
    bfs_q = collections.deque([QueueEntry(tree, low_range, high_range)])

    while bfs_q:
        current = bfs_q.popleft()
        if current.node:
            if current.node.data < current.lower or current.node.data > current.upper:
                return False
            
            bfs_q.extend([
                QueueEntry(current.node.left, current.lower, current.node.data),
                QueueEntry(current.node.right, current.node.data, current.upper)
            ])

    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
