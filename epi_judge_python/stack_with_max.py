from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections


class Stack:
    MaxCache = collections.namedtuple('MaxCache', ('element', 'max'))

    def __init__(self):
        self._max_cached_elements = []

    def push(self, x):
        self._max_cached_elements.append(
            self.MaxCache(x, x if self.empty() else max(x, self.max())))

    def pop(self):
        if self.empty():
            raise IndexError('pop(): Empty stack')

        return self._max_cached_elements.pop().element

    def empty(self):
        return len(self._max_cached_elements) == 0

    def max(self):
        return self._max_cached_elements[-1].max


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
