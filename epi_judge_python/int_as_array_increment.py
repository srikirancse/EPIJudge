from test_framework import generic_test


def plus_one(A):
    pointer = len(A) - 1
    carry = 1
    while carry and pointer >= 0:
        cur = A[pointer]
        A[pointer] = (cur + carry) % 10
        carry = (cur + carry) // 10
        pointer -= 1

    if carry:
        A.insert(0, 1)

    return A

        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
