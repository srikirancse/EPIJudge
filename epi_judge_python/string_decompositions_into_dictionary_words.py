from test_framework import generic_test

import collections


def find_all_substrings(s, words):
    def match_all_words_in_dict(start):
        cur_word_to_freq = collections.Counter()
        for i in range(start, start + word_length, word_length):
            cur_word = s[i:i + word_length]
            cur_word_to_freq[cur_word] += 1
            if word_to_freq[cur_word] == 0:
                return False
            if cur_word_to_freq[cur_word] > word_to_freq[cur_word]:
                return False
        return True

    word_length = len(words[0])
    word_to_freq = collections.Counter(words)
    return [
        i for i in range(len(s) - word_length * len(words) + 1) if match_all_words_in_dict(i)
    ]


print(find_all_substrings('srikiran', ['sri', 'kir']))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
