from test_framework import generic_test


def inorder_traversal(tree):
    result = []

    while tree.left:
        tree = tree.left

    while tree:
        result.append(tree.data)
        tree = next_inorder_successor(tree)

    return result


def next_inorder_successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left

        return node

    else:
        while node.parent and node is node.parent.right:
            node = node.parent

        return node.parent
         


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
