from test_framework import generic_test


def inorder_traversal(tree):
    result, prev = [], None

    while tree:
        prev = tree
        tree = tree.left

    tree = prev

    while tree:
        result.append(tree.data)
        tree = inorder_successor(tree)

    return result


def inorder_successor(tree):
    if tree.right:
        tree = tree.right

        while tree.left:
            tree = tree.left

        return tree

    while tree.parent and tree.parent.right is tree:
        tree = tree.parent

    return tree.parent


if __name__ == '__main__':

    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
