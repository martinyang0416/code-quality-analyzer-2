t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(0)
        continue
    a = 0
    while n % 2 == 0:
        a += 1
        n = n // 2
    b = 0
    while n % 3 == 0:
        b += 1
        n = n // 3
    if n != 1:
        print(-1)
    else:
        if a > b:
            print(-1)
        else:
            print(2 * b - a)