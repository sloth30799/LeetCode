# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

def maxProfitII(prices: list[int]) -> float:
    totalProfit = 0
    minPrice = float('inf')
    maxProfit = 0

    for i, price in enumerate(prices):
        minPrice = min(price, minPrice)

        potentialProfit = price - minPrice

        maxProfit = max(maxProfit, potentialProfit)

        if maxProfit == potentialProfit and i < len(prices) - 1:
            nextProfit = prices[i + 1] - minPrice

            if nextProfit > maxProfit:
                continue
            else:
                totalProfit += maxProfit
                minPrice = prices[i + 1]
                maxProfit = 0

    return totalProfit + maxProfit


prices = [7, 1, 5, 3, 6, 4]
print('max', maxProfitII(prices))
