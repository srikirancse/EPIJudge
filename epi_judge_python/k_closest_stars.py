import functools
import math
import heapq

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars, k):
    max_heap = []
    for star in stars:
        if len(max_heap) == k + 1:
            heapq.heappushpop(max_heap, (-star.distance, star))
        else:
            heapq.heappush(max_heap, (-star.distance, star))
    return [s[1] for s in heapq.nlargest(k, max_heap)]


# def find_closest_k_nums(nums, k):
#     max_heap = []
#     map(lambda x: heapq.heappushpop(max_heap, -x)
#         if len(max_heap) == k + 1 else heapq.heappush(max_heap, -x), nums)
#     return [-s for s in heapq.nlargest(k, max_heap)]

def find_closest_k_nums(nums, k):
    max_heap = []
    list(map(lambda x: heapq.heappushpop(max_heap, -x)
             if len(max_heap) == k + 1 else heapq.heappush(max_heap, -x), nums))
    return [-s for s in heapq.nlargest(k, max_heap)]

# def find_closest_k_nums(nums, k):
#     max_heap = []
#     for num in nums:
#         if len(max_heap) == k + 1:
#             heapq.heappushpop(max_heap, -num)
#         else:
#             heapq.heappush(max_heap, -num), nums
#     return [-s for s in heapq.nlargest(k, max_heap)]


print(find_closest_k_nums([1, 5, 6, 3, 8, 9, 10], 4))


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(
        functools.partial(find_closest_k_stars, iter(stars), k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("k_closest_stars.py",
                                       "k_closest_stars.tsv",
                                       find_closest_k_stars_wrapper, comp))
