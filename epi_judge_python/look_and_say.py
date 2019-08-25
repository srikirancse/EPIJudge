from test_framework import generic_test

def look_and_say(n):
    if n < 1:
        return []

    result = '1'

    for _ in range(1, n):
        prev_str = str(result)
        new_word, j = [], 0

        while j < len(prev_str):
            count = 1
            while j + 1 < len(prev_str) and prev_str[j] == prev_str[j + 1]:
                count += 1
                j += 1

            new_word.append(str(count) + prev_str[j])
            j += 1
        result = ''.join(new_word)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
