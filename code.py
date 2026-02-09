n, k = map(int, input().split())

max_m = 0
low = 0
high = k

while low <= high:
    mid = (low + high) // 2
    t = n - 1  # number of terms to sum
    s = 0
    current = mid // 2
    steps = t
    while steps > 0 and current > 0:
        s += current
        current = current // 2
        steps -= 1
    total = mid + s
    if total <= k:
        max_m = mid
        low = mid + 1
    else:
        high = mid - 1

print(max_m)