MOD = 10**9 + 7
MAX_N = 10**6

# Precompute dp array
dp = [0] * (MAX_N + 1)
dp[0] = 1
if MAX_N >= 1:
    dp[1] = 1

for i in range(2, MAX_N + 1):
    dp[i] = (dp[i-1] + (i-1) * dp[i-2]) % MOD

# Read input and process test cases
import sys
input = sys.stdin.read().split()
T = int(input[0])
for i in range(1, T+1):
    N = int(input[i])
    print(dp[N])