import sys

n = int(sys.stdin.readline())
dp = [-float('inf')] * 10
dp[0] = 0

for _ in range(n):
    k = int(sys.stdin.readline())
    cards = []
    for __ in range(k):
        c, d = map(int, sys.stdin.readline().split())
        cards.append((c, d))
    
    c1, c2, c3 = [], [], []
    for c, d in cards:
        if c == 1:
            c1.append(d)
        elif c == 2:
            c2.append(d)
        elif c == 3:
            c3.append(d)
    c1.sort(reverse=True)
    c2.sort(reverse=True)
  