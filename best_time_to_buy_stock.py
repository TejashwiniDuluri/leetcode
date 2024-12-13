
prices = [7, 1, 5, 3, 6, 4]

# prices = [7, 1, 3, 5, 6, 4]


def get_best_profit(prices):

    max_profit = 0
    curr_buy_stock = prices[0]

    for i in range(1, len(prices)):

        if prices[i] < curr_buy_stock:
            curr_buy_stock = prices[i]

        if prices[i] - curr_buy_stock > max_profit:
            max_profit = prices[i] - curr_buy_stock

    return max_profit


def get_get_multiple_profits(prices):

    tot_profits = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            tot_profits += prices[i] - prices[i-1]
    return tot_profits


print(get_get_multiple_profits(prices))


