from collections import defaultdict

m = int(input())
a = []
for _ in range(m):
    s = input().strip()
    row = [int(c) for c in s]
    a.append(row)

max_mask = 1 << m
dp = [[defaultdict(int) for _ in range(m)] for __ in range(max_mask)]

for u in range(m):
    mask = 1 << u
    dp[mask][u][0] = 1

masks_by_k = [[] for _ in range(m + 1)]
for mask in range(max_mask):
    k = bin(mask).count('1')
    if 0 < k <= m:
        masks_by_k[k].append(mask)

for k in range(1, m + 1):
    for mask in ma