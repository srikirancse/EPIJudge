import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def replace_and_remove(size, s):
    read_index, write_index, a_count = 0, 0, 0

    # get rid of b's
    while read_index < size:
        if s[read_index] != 'b':
            s[write_index] = s[read_index]
            write_index += 1

        if s[read_index] == 'a':
            a_count += 1
        
        read_index += 1

    read_index = write_index - 1
    write_index = read_index + a_count
    final_size = write_index + 1

    # Replace a's with dd from backwards
    while read_index >= 0:
        if s[read_index] == 'a':
            s[write_index - 1 : write_index + 1] = 'dd'
            write_index -= 2

        else:
            s[write_index] = s[read_index]
            write_index -= 1

        read_index -= 1

    return final_size


print(replace_and_remove(24, ["b", "d", "c", "a", "b", "a", "d", "b", "d", "b", "b", "a", "d", "c", "c", "a", "d", "a", "d", "d", "d", "b", "c", "c", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]))


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
