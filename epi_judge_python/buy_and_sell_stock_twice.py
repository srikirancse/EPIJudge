# from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    if len(prices) == 0: 
        return 0

    profit1 = 0
    profit2 = 0
    transactions = 0

    cur_profit = 0
    cur_min = prices[0]
    for i in range(len(prices)):
        if i == len(prices) - 1 or prices[i] > prices[i + 1]:
            if prices[i] - cur_min >= cur_profit:
                cur_profit = prices[i] - cur_min

                if cur_profit > 0:
                    if transactions == 0:
                        profit1 = max(cur_profit, profit1)
                    elif transactions == 1 or i == len(prices) - 1:
                        profit2 = max(cur_profit, profit2)
                    else:
                        profit_offset1 = cur_profit - profit1
                        profit_offset2 = cur_profit - profit2
                        if profit_offset1 > 0 and profit_offset2 > 0:
                            if profit_offset1 > profit_offset2:
                                profit1 = cur_profit
                            else:
                                profit2 = cur_profit
                        elif profit_offset1 > 0:
                            profit1 = cur_profit
                        elif profit_offset2 > 0:
                            profit2 = cur_profit
                    transactions += 1

        else:
            cur_min = min(prices[i], cur_min)
    
    return profit1 + profit2

print(buy_and_sell_stock_twice([2,1,2,0,1]))

# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main("buy_and_sell_stock_twice.py",
#                                        "buy_and_sell_stock_twice.tsv",
#                                        buy_and_sell_stock_twice))
