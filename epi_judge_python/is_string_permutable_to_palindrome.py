from test_framework import generic_test
import collections


# def can_form_palindrome(s):
#     return sum(v % 2 for v in collections.Counter(s).values) <= 1


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    # Write your code here
    q, res = collections.deque([root]), [root.info]

    while not all(v is None for v in q):
        for _ in range(len(q)):
            cur = q.popleft()
            q.append(cur.left) if cur else q.append(None)
            q.append(cur.right) if cur else q.append(None)
        if q[0] is not None:
            res.append(q[0].info)
        if q[-1] is not None:
            res.append(q[-1].info)

    return res


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(topView(tree.root))


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main(
#             "is_string_permutable_to_palindrome.py",
#             'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
