from test_framework import generic_test
import collections
import string


# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate', 'distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)
    while q:
        cur = q.popleft()
        if cur.candidate == t:
            return cur.distance

        for i in range(len(cur.candidate)):
            for c in string.ascii_lowercase:
                candidate = cur.candidate[:i] + c + cur.candidate[i + 1:]
                if candidate in D:
                    D.remove(candidate)
                    q.append(StringWithDistance(candidate, cur.distance + 1))

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
