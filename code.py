n, m, k = map(int, input().split())
s = list(map(int, input().split()))
a = list(map(int, input().split()))

blocked_ptr = 0
available = []
for x in range(n):
    if blocked_ptr < m and x == s[blocked_ptr]:
        blocked_ptr += 1
    else:
        available.append(x)

if not available:
    print(-1)
else:
    min_cost = float('inf')
    import bisect
    for l in range(1, k+1):
        current = 0
        cnt = 0
        possible = True
        prev_current = -1
        while current < n:
    