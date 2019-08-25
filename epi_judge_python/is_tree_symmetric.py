from test_framework import generic_test


def is_symmetric(tree):
    def check_symmetry(left, right):
        if not left and not right:
            return True

        if left and right and left.data == right.data:
            return check_symmetry(left.left, right.right) and check_symmetry(right.left, left.right)

        return False

    return not tree or check_symmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
