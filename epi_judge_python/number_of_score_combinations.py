from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    dp = [[1] + [0] * final_score for _ in range(len(individual_play_scores))]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = dp[i - 1][j] if i >= 0 else 0
            with_this_play = dp[i][j - individual_play_scores[i]
                                   ] if j >= individual_play_scores[i] else 0
            dp[i][j] = with_this_play + without_this_play

    return dp[-1][-1]


num_combinations_for_final_score(12, [2, 3, 7])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
