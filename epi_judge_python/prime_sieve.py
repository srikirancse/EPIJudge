from test_framework import generic_test


# Given n, return all primes up to and including n.
# def generate_primes(n):
#     is_prime = [False, False] + [True] * (n - 1)
#     result = []
#     for i in range(2, n + 1):
#         if is_prime[i]:
#             result.append(i)
#             for j in range(i, n + 1, i):
#                is_prime[j] = False
#     return result


def generate_primes(n):
    is_prime = [False, False] + [True] * (n - 1)
    result = []
    for i in range(2, n + 1):
        if is_prime[i]:
            result.append(i)
            for j in range(i, n + 1, i):
                is_prime[j] = False
    return result





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
