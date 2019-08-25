import collections
import functools
import heapq
import string
import random

# Question 1. Number of roads connecting maximum cities


class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.visited = False


def make_graph_from_edges(edges, num_nodes):
    graph = [GraphVertex(i) for i in range(1, num_nodes + 1)]
    for (fro, to) in edges:
        graph[fro - 1].edges.append(graph[to - 1])
        graph[to - 1].edges.append(graph[fro - 1])

    return graph


def max_cites_roads(A, B, n):
    graph = make_graph_from_edges(zip(A, B), n)

    def component_degree_sum(vertex):
        if vertex.visited:
            return 0
        vertex.visited = True

        return len(vertex.edges) + sum(component_degree_sum(child) for child in vertex.edges)

    return max(component_degree_sum(vertex) for vertex in graph if not vertex.visited) // 2


# Question 2. Max deletions required to obtain a string with unique occurrences of all strings
def deletions_to_unique_occurrences(s):
    frequency = collections.Counter(s).values()
    result, uniq_freq = 0, set()
    for f in frequency:
        while f > 0 and f in uniq_freq:
            f -= 1
            result += 1

        if f > 0:
            uniq_freq.add(f)

    return result

# Question 3: Max deletions required to obtain a string with no triplets


def deletions_to_no_triplets(s):
    result, i = 0, 1
    while i < len(s):
        count = 1
        while i < len(s) and s[i - 1] == s[i]:
            count += 1
            if count % 3 == 0:
                result += 1
            i += 1
        i += 1
    return result


# Question 4: Return the maximum sum of two numbers digits add up to same number
def maximum_sum_of_same_digit_sum(A):
    digit_sum_map = {}
    for num in A:
        # Computing the sum of digits of the number
        sum_of_digits = functools.reduce(
            lambda x, y: int(x) + int(y), str(num))
        # Updating the obtained sum to the hash map and also pushing the corresponding number to the min heap
        if sum_of_digits not in digit_sum_map or len(digit_sum_map[sum_of_digits]) < 2:
            # Push the numbers to the heap until the numbers which form a sum are exactly 2
            heapq.heappush(digit_sum_map.setdefault(
                sum_of_digits, []), num)

        else:
            # Once the numbers reach 2 pus and pop the numbers to maintain the count to 2
            heapq.heappushpop(digit_sum_map[sum_of_digits], num)

    # Return the maximum sum of all the the 2 largest numbers that forms a particular sum
    return max(map(lambda nums: functools.reduce(lambda x, y: x + y, nums) if len(nums) == 2 else -1, digit_sum_map.values()))


# print(maximum_sum_of_same_digit_sum([51, 71, 17, 42, 33, 44, 24, 62]))
# print(maximum_sum_of_same_digit_sum([51, 71, 17, 42]))
# print(maximum_sum_of_same_digit_sum([42, 33, 60]))
# print(maximum_sum_of_same_digit_sum([51, 32, 43]))


# Question 5: Replace ? with a character that is different from it's adjacent characters
def replace_question_marks(s):
    i, res = 0, []
    while i < len(s):
        if s[i] == '?':
            replacement_char = random.choice(string.ascii_lowercase)
            while (i > 0 and s[i - 1] == replacement_char) or (i < len(s) - 1 and s[i + 1] == replacement_char):
                replacement_char = random.choice(string.ascii_lowercase)
            res.append(replacement_char)

        else:
            res.append(s[i])

        i += 1

    return ''.join(res)


# print(replace_question_marks('a?b?c?d?g'))
# print(replace_question_marks('ab?ac?'))
# print(replace_question_marks('??rd?e?wg??'))
# print(replace_question_marks('???????'))


# Question 6. Minimum number of operations required to make all the towers of equal height
def equalize_tower_height(A):
    operations, tower_count = 0, collections.Counter(A)
    max_heap = [-a for a in tower_count.keys()]
    heapq.heapify(max_heap)

    prev_top = -heapq.heappop(max_heap)
    while max_heap:
        cur_top = -heapq.heappop(max_heap)
        operations += tower_count[prev_top]
        tower_count[cur_top] += tower_count[prev_top]
        prev_top = cur_top

    return operations


# print(equalize_tower_height([3, 5, 3, 5, 2, 5]))


# Question 7.Print Unique paths
def unique_paths(A):
    res = []

    def dfs(i, j, path):
        if i >= len(A) or j >= len(A[i]):
            return

        path.append(A[i][j])

        if i == len(A) - 1 and j == len(A[i]) - 1:
            res.append(path[:])

        dfs(i, j + 1, path)
        dfs(i + 1, j, path)

        del path[-1]

    dfs(0, 0, [])
    return res


print(unique_paths([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
