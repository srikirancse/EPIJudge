from test_framework import generic_test


def evaluate(expression):
    DELIMITER = ','
    stack = []

    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y
    }

    for token in expression.split(DELIMITER):
        if token in OPERATORS:
            stack.append(OPERATORS[token](stack.pop(), stack.pop()))

        else:
            stack.append(int(token))

    return stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
