from test_framework import generic_test


def number_of_ways(n, m):
    number_of_ways = [[0] * m for _ in range(n)]
    def number_of_ways_helper(n, m):
        if n < 0 or m < 0:
            return 0
        if n == m == 0:
            return 1
        
        if number_of_ways[n][m] == 0:
            number_of_ways[n][m] = number_of_ways_helper(n - 1, m) + number_of_ways_helper(n, m - 1)

        return number_of_ways[n][m]
    
    return number_of_ways_helper(n - 1, m - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
