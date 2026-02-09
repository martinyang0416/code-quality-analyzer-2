n, a, b, c = map(int, input().split())
total = 0
max_z = min(c, (2 * n) // 4)
for z in range(max_z + 1):
    rem = 2 * n - 4 * z
    delta = rem - a
    y_min = max(0, (delta + 1) // 2)
    y_max = min(b, rem // 2)
    if y_min > y_max:
        continue
    total += y_max - y_min + 1
print(total)