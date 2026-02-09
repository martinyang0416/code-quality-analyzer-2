from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dp = {0: 1000}  # Represents {stocks: max_money}

for price in a:
    new_dp = defaultdict(int)
    for s_prev, m_prev in dp.items():
        # Do nothing
        if new_dp[s_prev] < m_prev:
            new_dp[s_prev] = m_prev
        # Sell all
        new_m_sell = m_prev + s_prev * price
        if new_dp[0] < new_m_sell:
            new_dp[0] = new_m_sell
        # Buy as much as possible
        max_bu