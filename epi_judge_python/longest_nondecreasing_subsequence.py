from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    dp = [1] * len(A)
    for i in range(1, len(A)):
        dp[i] = max(1 + max((dp[j] for j in range(i) if A[i] >= A[j]), default=0), dp[i])
    return max(dp)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
