import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
# def reverse_words(s):
    # s.reverse()
    # p1, p2 = 0, 0

    # def reverse_word(p1, p2):
    #     while p1 < p2:
    #         s[p1], s[p2] = s[p2], s[p1]
    #         p1, p2 = p1 + 1, p2 - 1

    # while p1 < len(s):
    #     p2 = s.find(b' ', p1)
    #     if p2 < 0: 
    #         break
    #     reverse_word(p1, p2 - 1)
    #     p1 = p2 + 1

    # reverse_word(p1, len(s) - 1)

    # return s


def reverse_words(s):
    s.reverse()
    p1, p2 = 0, 0

    def reverse_word(p1, p2):
        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1, p2 = p1 + 1, p2 - 1

    while p1 < len(s):
        p2 = s.find(b' ', p1)
        if p2 < 0:
            break

        reverse_word(p1, p2 - 1)
        p1 = p2 + 1

    reverse_word(p1, len(s) - 1)

    return s

        


print(reverse_words(bytearray('ZeLFvx9v 8CC51 ', 'utf-8')))

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
