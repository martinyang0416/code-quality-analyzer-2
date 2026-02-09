t = int(input())
for _ in range(t):
    n, c, m = map(int, input().split())
    initial = n // c
    total = initial
    wrappers = initial
    while wrappers >= m:
        exchange = wrappers // m
        total += exchange
        wrappers = wrappers % m + exchange
    print(total)