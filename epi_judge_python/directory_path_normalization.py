from test_framework import generic_test


def shortest_equivalent_path(path):
    if not path:
        raise ValueError('Empty String is not a valid path')

    stack = []

    if path[0] == '/':
        stack.append('/')

    for token in (token for token in path.split('/') if token not in ['', '.']):
        if token == '..':
            if not stack or stack[-1] == '..':
                stack.append(token)

            else:
                if stack[-1] == '/':
                    raise ValueError('Path Error')
                stack.pop()

        else:
            stack.append(token)

    result = '/'.join(stack)
    return result[result.startswith('//'):]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
