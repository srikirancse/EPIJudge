from test_framework import generic_test, test_utils
import heapq


def k_largest_in_binary_heap(A, k):
    candidate_max_heap = []
    result = []

    heapq.heappush(candidate_max_heap, (-A[0], 0))

    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])

        left_child = 2 * candidate_idx + 1
        if left_child < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_child], left_child))

        right_child = 2 * candidate_idx + 2
        if right_child < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_child], right_child))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
