from test_framework import generic_test
import string

def convert_base(num_as_string, b1, b2):
    base_to_integer = base_to_int(num_as_string[num_as_string[0] == '-':], b1)
    is_negative = num_as_string[0] == '-'
    return ('-' if is_negative else '') + int_to_base(base_to_integer, b2)

def base_to_int(num_as_string, base):
    num_as_int = 0
    for i in num_as_string:
        num_as_int = (num_as_int * base) + string.hexdigits.index(i.lower())

    return num_as_int

def int_to_base(num_as_int, base):
    num_as_str = []
    while True:
        num_as_str.append(string.hexdigits[num_as_int % base].upper())
        num_as_int //= base
        if num_as_int == 0:
            break

    return ''.join(reversed(num_as_str))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
