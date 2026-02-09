MOD = 10**9 + 7
m_max = 200000

# Precompute the DP table
dp = [[0] * (m_max + 1) for _ in range(10)]
for d in range(10):
    dp[d][0] = 1  # Base case: 0 operations

for k in range(1, m_max + 1):
    for d in range(10):
        if d + 1 < 10:
            dp[d][k] = dp[d+1][k-1] % MOD
        else:
            dp[d][k] = (dp[0][k-1] + dp[1][k-1]) % MOD

import sys
input = sys.stdin.read().split()
t = int(input[0])
index = 1

for _ in range(t):
    n = input[index]
    m = int(input[index + 1])
 