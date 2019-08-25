from test_framework import generic_test
from test_framework.test_failure import TestFailure

# def int_to_string(x):
#     result = []
#     is_negative = False 
#     if (x < 0):
#         x = -x
#         is_negative = True
    
#     while True:
#         result.append(chr(ord('0') + (x % 10)))
#         x //= 10
#         if x == 0:
#             break
    
#     return ('-' if is_negative else '') + ''.join(reversed(result))

def int_to_string(x):
    result = []
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True

    while True:
        result.append(str(x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(result))


import string

def string_to_int(s):
    result = 0
    reminder = 1

    if s[0] == '-':
        reminder = -1

    s = s[s[0] == '-':]

    for i in range(len(s)):
        result = (result * 10) + int(s[i])

    return result * reminder


print(string_to_int("-345"))

def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
