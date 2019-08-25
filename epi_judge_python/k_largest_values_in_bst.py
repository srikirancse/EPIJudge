from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    k_largest_elements = []

    def find_k_largest_in_bst_helper(tree):
        if tree.right:
            find_k_largest_in_bst_helper(tree.right)
        if len(k_largest_elements) < k:
            k_largest_elements.append(tree.data)
        if tree.left:
            find_k_largest_in_bst_helper(tree.left)

    find_k_largest_in_bst_helper(tree)
    return k_largest_elements


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
