n, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

count = 0
for i in range(n):
    left = i + 1
    right = n - 1
    res = -1
    target = a[i] + K
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > a[i] and a[mid] <= target:
            res = mid
            right = mid - 1
        elif a[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if res != -1:
        count += 1

print(n - count)