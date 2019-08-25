from test_framework import generic_test

def buy_and_sell_stock_once(prices):
    local_min, max_profit = float('inf'), 0.0
    for i in prices:
        local_min = min(local_min, i)
        max_profit = max(max_profit, i - local_min)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
