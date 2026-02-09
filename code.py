n, k, s = map(int, input().split())
a = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + a[i]

left = k + 1
right = n
ans = -1

while left <= right:
    mid = (left + right) // 2
    if mid > n:
        valid = False
    else:
        valid = any((prefix[i + mid] - prefix[i] > s) for i in range(n - mid + 1))
    
    if valid:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans if ans != -1 else -1)