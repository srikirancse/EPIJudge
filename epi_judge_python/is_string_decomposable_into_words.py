import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    end_word_distance = [-1] * len(domain)

    for i in range(len(domain)):
        if domain[:i + 1] in dictionary:
            end_word_distance[i] = i + 1
        else:
            for j in range(i):
                if end_word_distance[j] != -1 and domain[j + 1 : i + 1] in dictionary:
                    end_word_distance[i] = i - j
                    break

    decompositions = []
    if end_word_distance[-1] != -1:
        idx = len(domain) - 1
        while idx >= 0:
            decompositions.append(domain[idx + 1 - end_word_distance[idx] : idx + 1])
            idx -= end_word_distance[idx]
        decompositions = decompositions[::-1]
    return decompositions


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
