import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

total = 0
for i in range(n):
    target = a[i] + k
    j = bisect.bisect_left(a, target, i + 1, n)
    total += n - j

print(total)