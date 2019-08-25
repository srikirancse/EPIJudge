from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_postorder_inorder(postorder, inorder):
    indorder_data_idx_map = {data: i for i, data in enumerate(inorder)}

    def construct_binary_tree(postorder_start, postorder_end, inorder_start, inorder_end):
        if postorder_start <= postorder_end or inorder_end <= inorder_start:
            return None

        root = postorder[postorder_start]
        root_inorder_idx = indorder_data_idx_map[root]
        len_right_sub_tree = inorder_end - root_inorder_idx + 1

        return BinaryTreeNode(
            root,
            construct_binary_tree(postorder_start - len_right_sub_tree,
                                  postorder_end, inorder_start, root_inorder_idx),
            construct_binary_tree(
                postorder_start - 1, postorder_end, root_inorder_idx + 1, inorder_end)
        )

    return construct_binary_tree(len(inorder) - 1, - 1, 0, len(postorder))


binary_tree_from_postorder_inorder(['F', 'A', 'E', 'B', 'I', 'G', 'D', 'C', 'H'], [
                                   'F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G'])


def binary_tree_from_preorder_inorder(preorder, inorder):
    inorder_data_idx_map = {data: i for i, data in enumerate(inorder)}

    def construct_binary_tree(preorder_start, preorder_stop, inorder_start, inorder_stop):
        if preorder_stop <= preorder_start or inorder_stop <= inorder_start:
            return None

        preorder_cur = preorder[preorder_start]
        inorder_cur_idx = inorder_data_idx_map[preorder_cur]
        left_sub_tree_length = inorder_cur_idx - inorder_start + 1

        node = BinaryTreeNode(preorder_cur)
        node.left = construct_binary_tree(
            preorder_start + 1, preorder_stop, inorder_start, inorder_cur_idx)
        node.right = construct_binary_tree(
            preorder_start + left_sub_tree_length, preorder_stop, inorder_cur_idx + 1, inorder_stop)

        return node

    return construct_binary_tree(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
