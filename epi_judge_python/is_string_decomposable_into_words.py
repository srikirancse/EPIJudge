import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    dp = [-1] * len(domain)
    for i in range(len(domain)):
        if domain[:i + 1] in dictionary:
            dp[i] = i + 1

        if dp[i] == -1:
            for j in range(i):
                if dp[j] != -1 and domain[j + 1:i + 1] in dictionary:
                    dp[i] = i - j

    if dp[-1] == -1:
        return []
        
    i = len(domain) - 1
    res = []
    while i >= 0:
        res.append(domain[i - dp[i] + 1:i + 1])
        i -= dp[i]

    return res[::-1]


# print(decompose_into_dictionary_words('bedbathandbeyond', set(['bed', 'bath', 'beyond', 'bat', 'hand', 'and'])))
# print(decompose_into_dictionary_words('rawabawrawr', set(["raw", "abr", "bara", "rawa", "wr"])))


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
