from test_framework import generic_test


def is_well_formed(s):
    LOOKUP = {'{': '}', '(': ')', '[': ']'}
    stack = []
    for c in s:
        if c in LOOKUP:
            stack.append(c)

        elif not stack or LOOKUP[stack.pop()] != c:
            return False

    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
