from test_framework import generic_test
import bintrees
import math

class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

def generate_first_k_a_b_sqrt2(k):
    bfs_bst = bintrees.RBTree([(Number(0, 0), None)])
    result = []

    while len(result) < k:
        min_number = bfs_bst.pop_min()[0]
        result.append(min_number.val)
        bfs_bst.insert((Number(min_number.a + 1, min_number.b)), None)
        bfs_bst.insert((Number(min_number.a, min_number.b + 1)), None)
    return result

print(generate_first_k_a_b_sqrt2(3))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
