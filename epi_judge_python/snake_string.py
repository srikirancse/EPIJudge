from test_framework import generic_test


# def snake_string(s):
#     result = []

#     for i in range(1, len(s), 4):
#         result.append(s[i])
#     for i in range(0, len(s), 2):
#         result.append(s[i])
#     for i in range(3, len(s), 4):
#         result.append(s[i])
#     return ''.join(result)


def snake_string(s):
    result = []
    for i in range(1, len(s), 4):
        result.append(s[i])
    for i in range(0, len(s), 2):
        result.append(s[i])
    for i in range(3, len(s), 4):
        result.append(s[i])

    return ''.join(result)


print(snake_string('Hello World!'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("snake_string.py", 'snake_string.tsv',
                                       snake_string))
