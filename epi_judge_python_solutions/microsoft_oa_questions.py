import collections
import functools
import heapq
import string
import random
from statistics import median

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


# print(max_cites_roads([1, 2, 4, 5], [2, 3, 5, 6], 6))


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


# print(unique_paths([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def smallest_string(S):
    i = 0
    while i < len(S) - 1:
        if S[i] > S[i + 1]:
            break

        i += 1

    return S[:i] + S[i + 1:]


# print(smallest_string('aaaaaab'))

# Time Complexity Analysis:
#   The time complexity is O(n) where n is the length of the string as the dominated operatiion is reading all the characters in the string in one pass

# Space Complexity Analysis:
#     In the worst case scenario the algorithm needs to declare a Hash map and a hash set with maximum  26 characters when the string contains all the 26 alphabets since S can contain only lower case letters.


def max_strings_with_unique(A):
    def string_has_unique_characters(dict):
        return all(map(lambda x: x <= 1, collections.Counter(dict).values()))

    dp = [A[i] if string_has_unique_characters(
        A[i]) else '' for i in range(len(A))]
    result = max(map(lambda x: len(x), dp))

    for i in range(len(A)):
        if string_has_unique_characters(A[i]):
            for j in range(i):
                if string_has_unique_characters(dp[j]) and string_has_unique_characters(A[i] + A[j]):
                    new_candidate = A[i] + dp[j] if string_has_unique_characters(
                        A[i] + dp[j]) else A[i] + A[j]
                    if len(new_candidate) > len(dp[i]):
                        dp[i] = new_candidate
                        result = max(result, len(dp[i]))

    return result


def maxLength(A):
    dp = [set()]
    for a in A:
        if len(set(a)) != len(a):
            continue
        a = set(a)
        for c in dp[:]:
            if a & c:
                continue
            dp.append(a | c)
    return max(len(a) for a in dp)


# print(max_strings_with_unique(['co', 'dil', 'ity']))
# print(max_strings_with_unique(["abc", "ade", "akl"]))
# print(max_strings_with_unique(["abc", "kkk", "def", "csv"]))
# print(max_strings_with_unique(["abcd", "ab", "cd", "ef"]))
# print(max_strings_with_unique(["abcd", "ab", "cd", "ef"]))
# print(max_strings_with_unique(['ab', 'cd', 'ce', 'dm']))
# print(max_strings_with_unique(['eva', 'jqw', 'tyn', 'jan']))
# print(max_strings_with_unique(["abcdefghijklmnopqrstuvwxyz"]))
# print(max_strings_with_unique(["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"]))
print(max_strings_with_unique(["dnshjtyweqga", "oruikdwylqcxzsjfe", "yv", "mgvpaczjebwyidoh", "ajhszfbwuyxivlend", "sezydofiwpabkxj", "fnueg",
                               "d", "yruhmnfgk", "inlk", "ckjlfiugnzmhsxdy", "iupsvagkcn", "inmrvwyuajzopdsk", "qwmsxzyilkrjoc", "aemrkputxiqoldby", "pytlbaigkd"]))
print(maxLength(["dnshjtyweqga", "oruikdwylqcxzsjfe", "yv", "mgvpaczjebwyidoh", "ajhszfbwuyxivlend", "sezydofiwpabkxj", "fnueg",
                 "d", "yruhmnfgk", "inlk", "ckjlfiugnzmhsxdy", "iupsvagkcn", "inmrvwyuajzopdsk", "qwmsxzyilkrjoc", "aemrkputxiqoldby", "pytlbaigkd"]))


def days_of_week(day, k):
    days_map = {'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4, 'sat': 5,
                'sun': 6, 0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', 4: 'fri', 5: 'sat', 6: 'sun'}

    return days_map[(days_map[day] + k) % 7]


# print(days_of_week('wed', 2))  # => 'fri'
# print(days_of_week('sat', 23))  # => 'mon'

def insert_five(num):
    num_str = str(num) if num >= 0 else str(-num)
    i = 0

    if num >= 0:
        while i < len(num_str) and num_str[i] >= '5':
            i += 1
    else:
        while i < len(num_str) and num_str[i] <= '5':
            i += 1

    max_string = (num_str[:i] + '5' + num_str[i:])

    return max_string if num >= 0 else '-' + max_string

# print(insert_five(268))
# print(insert_five(670))
# print(insert_five(0))
# print(insert_five(-999))
# print(insert_five(-191))
# print(insert_five(666))
# print(insert_five(945))
# print(insert_five(439))
# print(insert_five(-945))
# print(insert_five(-439))


from itertools import groupby

def longest_alternating_substring(str):
    temp, res = 0, 0

    for c, g in groupby(str):
        L = len(list(g))
        res = max(res, temp + min(L, 2))
        temp = temp + L if L < 3 else 2

    return res

# print(longest_alternating_substring('baaabbabbb'))
# print(longest_alternating_substring('babba'))
# print(longest_alternating_substring('abaaaa'))

def min_moves_to_unique(str):
    return sum(len(list(g)) // 3 for _, g in groupby(str))


def min_swaps_palindrome(s):
    def is_palindrome(s):
        return sum(v % 2 for v in collections.Counter(s).values()) < 2

    if is_palindrome(s):
        i, j = 0, len(s) - 1
        swaps_count = 0
        while i < j:
            if s[i] != s[j]:
                swaps_count += 1

            i += 1
            j -= 1

        return swaps_count

    return -1


# print(min_swaps_palindrome('mamad'))
# print(min_swaps_palindrome('asflkj'))
# print(min_swaps_palindrome('aabb'))
# print(min_swaps_palindrome('ntiin'))

def lexicographically_smallest(s):
    i = 0
    while i < len(s) - 1:
        if s[i] > s[i + 1]:
            break

        i += 1

    return s[:i] + s[i + 1:]

# print(lexicographically_smallest('abczd'))
# print(lexicographically_smallest('acb'))
# print(lexicographically_smallest('hot'))
# print(lexicographically_smallest('codility'))
# print(lexicographically_smallest('aaaa'))


def range_coverage(A, K):
    n = len(A)
    for i in range(n - 1):
        if (A[i] > A[i + 1] or A[i] + 1 < A[i + 1]):
            return False
    if (A[0] != 1 and A[n - 1] != K):
        return False
    else:
        return True

# print(solution([1, 1, 2, 3, 3, 4, 5], 3))
# print(solution([1, 1, 2, 3, 3, 2, 3], 3))

# def min_swaps_to_palindrome(S):
#     def is_palindrome(s):
#         return sum(v % 2 for v in collections.Counter(s).values()) < 2

#     if not is_palindrome(S):
#         return -1


    

# print(min_swaps_to_palindrome('mamad'))


def missing_elements(A, n):
    missed_count = n - len(A)
    aux_array = [0] * missed_count

    for a in A:
        abs_a = abs(a)
        if abs_a < len(A):
            A[abs_a] *= -1

        else:
            aux_array[abs_a % (len(A))] = -1

    return [i for i, a in enumerate(A) if a > 0] + [i + len(A) for i, a in enumerate(aux_array) if a != -1]


# print(missing_elements([1, 4, 5, 2, 8], 9))


def radix_sort(num):
    for i in range(31):
        onebucket = []
        zerobucket = []
        needle = 1 << i
        for j in range(len(num)):
            if num[j] & needle != 0:
                onebucket.append(num[j])
            else:
                zerobucket.append(num[j])
        num = []
        num += zerobucket
        num += onebucket
    return num


# print(radix_sort([983, 837, 284, 543, 653]))

class StringCodec:
    def serialize(self, S):
        return ''.join(map(lambda x: str(len(x)) + '~' + x, S))

    def deserialize(self, s):
        i, res = 0, []
        while i < len(s):
            j = s.find('~', i)
            i = j + 1 + int(s[i:j])
            res.append(s[j + 1:i])
        return res


# string_codec = StringCodec()
# print(string_codec.deserialize(string_codec.serialize(
#     ["63/Rc", "h", "BmI3FS~J9#vmk", "7uBZ?7*/", "24h+X", "O "])))


def swaps_to_move_reds(A):
    if len([i for i, c in enumerate(A) if c == 'R']) == 0:
        return 0

    middle_red_idx = int(median([i for i, c in enumerate(A) if c == 'R']))
    return sum([(A[i:middle_red_idx] if i < middle_red_idx else A[middle_red_idx + 1:i]).count('W')
                for i, c in enumerate(A) if c == 'R' and i != middle_red_idx])


# print(swaps_to_move_reds((['W'] * 2) + (['R']) + (['W'] * 3) + ['R', 'W', 'R']))
# print(swaps_to_move_reds((['R'] * 3) + (['W'] * 3) + (['R'])))
# print(swaps_to_move_reds((['W']) + (['R'] * 2) + (['W'] * 2) + (['R'])))
# print(swaps_to_move_reds((['W'] * 3)))


def sum_to_zero(n):
    res = []

    if n % 2:
        # Odd number should have a 0
        res.append(0)

    for i in range(1, n//2 + 1):
        res += [i, -i]

    return res


# print([(len(sum_to_zero(n)) == n, sum(sum_to_zero(n)) == 0)
#        for n in range(1, 100)]) # All trues
