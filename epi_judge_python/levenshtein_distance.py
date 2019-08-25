from test_framework import generic_test


def levenshtein_distance(A, B):
    distance_between_prefexes = [[-1] * len(B) for _ in A]

    def compute_distace_between_prefexes(A_idx, B_idx):
        if A_idx < 0:
            return B_idx + 1
        if B_idx < 0:
            return A_idx + 1

        if distance_between_prefexes[A_idx][B_idx] == -1:
            if A[A_idx] == B[B_idx]:
                distance_between_prefexes[A_idx][B_idx] = compute_distace_between_prefexes(A_idx - 1, B_idx - 1)

            else:
                substitute_last = compute_distace_between_prefexes(A_idx - 1, B_idx - 1)
                add_last = compute_distace_between_prefexes(A_idx - 1, B_idx)
                delete_last = compute_distace_between_prefexes(A_idx, B_idx - 1)

                distance_between_prefexes[A_idx][B_idx] = min(substitute_last, add_last, delete_last) + 1

        return distance_between_prefexes[A_idx][B_idx]
    return compute_distace_between_prefexes(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
