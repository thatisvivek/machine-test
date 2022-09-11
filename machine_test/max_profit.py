def solution_one(prices: list[int | float]) -> int | float:
    max_profit = 0
    for d1 in range(len(prices) - 1):
        for d2 in range(d1 + 1, len(prices)):
            curr_profit = prices[d2] - prices[d1]
            if curr_profit > max_profit:
                max_profit = curr_profit

    return max_profit


def solution_two(prices: list[int | float]) -> int | float:
    max_profit = 0
    min_price = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price

        curr_profit = price - min_price

        if curr_profit > max_profit:
            max_profit = curr_profit
    return max_profit
