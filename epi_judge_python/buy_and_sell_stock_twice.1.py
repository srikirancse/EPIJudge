from test_framework import generic_test


# def buy_and_sell_stock_twice(prices):
#     results = []
#     result = 0

#     cur_profit = 0
#     cur_min = prices[0]
#     for i in prices:
#         cur_min = min(i, cur_min)
#         cur_profit = max(i - cur_min, cur_profit)
#         results.append(cur_profit)

#     reverse_index = len(prices) - 1
#     cur_profit = 0
#     cur_max = prices[reverse_index]
#     for i in reversed(prices):
#         cur_max = max(i, cur_max)
#         cur_profit = max(cur_max - i, cur_profit)
#         result = max(result, cur_profit + results[reverse_index])
#         reverse_index -= 1
    
#     return result

def buy_and_sell_stock_twice(prices):
    forward_results = buy_and_sell_stock_once_list(prices)

    max_profit, max_rev_profit, max_price_so_far, rev_index = forward_results[-1], 0.0, float('-inf'), len(prices) - 1

    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_rev_profit = max(max_rev_profit, max_price_so_far - price)
        max_profit = max(forward_results[i - 1] + max_rev_profit, max_profit)

    return max_profit


def buy_and_sell_stock_once_list(prices):
    result, max_profit, min_price_so_far = [], 0.0, float('inf')

    for i in prices:
        min_price_so_far = min(min_price_so_far, i)
        max_profit = max(max_profit, i - min_price_so_far)
        result.append(max_profit)

    return result

print(buy_and_sell_stock_twice([0.1, 0.2]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
