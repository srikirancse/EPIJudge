from test_framework import generic_test

from collections import Counter


def find_all_substrings(s, words):
    words_freq = Counter(words)
    word_len = len(words[0])

    def word_in_dict(start):
        cur_words_feq = Counter()
        for i in range(start, start + len(words) * word_len, word_len):
            word = s[i : i + word_len]
            cur_words_feq[word] += 1
            word_freq = words_freq[word]
            if word_freq == 0 or cur_words_feq[word] > word_freq:
                return False

        return True

    return [i for i in range(len(s) - word_len * len(words) + 1) if word_in_dict(i)]

print(find_all_substrings('srikiran', ['sri', 'kir']))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
