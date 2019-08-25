from test_framework import generic_test


def is_palindrome(s):
    forward, backward = 0, len(s) - 1

    while forward < backward:
        while not s[forward].isalnum() and forward < backward:
            forward += 1

        while not s[backward].isalnum() and forward < backward:
            backward -= 1

        if s[forward].lower() != s[backward].lower():
            return False

        forward += 1
        backward -= 1

    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
