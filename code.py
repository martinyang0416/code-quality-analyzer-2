import sys
from collections import deque

n, m, p = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))

sum_d = [0] * (n + 1)
for i in range(2, n + 1):
    sum_d[i] = sum_d[i-1] + d[i-2]

a = []
for _ in range(m):
    hi, ti = map(int, sys.stdin.readline().split())
    a.append(ti - sum_d[hi])

a.sort()
prefix = [0] * (m + 1)
for i in range(1, m + 1):
    prefix[i] = prefix[i-1] + a[i-1]

prev_dp = [float('inf')] * (m + 1)
prev_dp[0] = 0

for _ in range(p):
 