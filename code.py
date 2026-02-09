n = int(input())
total = 0
for d in range(2, n + 1):
    x = 2
    while True:
        m = d * x
        if m > n:
            break
        total += 4 * x
        x += 1
print(total)