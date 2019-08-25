from test_framework import generic_test
import functools

def rabin_karp(t, s):
    BASE = 26

    potential_needle = functools.reduce(lambda x, y: (x * BASE) + ord(y), t[:len(s)], 0)
    needle = functools.reduce(lambda x, y: (x * BASE) + ord(y), s, 0)
    power = BASE**max(len(s) - 1, 0)

    for i in range(len(s), len(t)):
        if potential_needle == needle and t[i - len(s) : i] == s:
            return i - len(s)

        # Compute the new potential needle using rolling hash function
        potential_needle -= ord(t[i - len(s)]) * power
        potential_needle = (potential_needle * BASE) + ord(t[i])

    if potential_needle == needle and t[len(t) - len(s):] == s:
        return len(t) - len(s)

    return - 1


print(rabin_karp('abecdabc', 'abc'))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
