import bisect

n, m = map(int, input().split())

prefix = [0]
for _ in range(n):
    p, _ = map(int, input().split())
    prefix.append(prefix[-1] + p)

queries = list(map(int, input().split()))
for x in queries:
    pos = bisect.bisect_left(prefix, x)
    if pos >= len(prefix):
        print(n)
    else:
        print(pos)