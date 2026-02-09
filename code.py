def maxProfit(prices):
    if not prices:
        return 0
    s0 = 0
    s1 = -prices[0]
    s2 = float('-inf')
    for price in prices[1:]:
        new_s0 = max(s0, s2)
        new_s1 = max(s1, s0 - price)
        new_s2 = s1 + price
        s0, s1, s2 = new_s0, new_s1, new_s2
    return max(s0, s2)