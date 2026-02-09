Q = int(input())
for _ in range(Q):
    n = int(input())
    seen = set()
    steps = 0
    current = n
    while True:
        if current < 10:
            print(steps)
            break
        if current in seen:
            print(-1)
            break
        seen.add(current)
        s = str(current)
        max_prod = 0
        for i in range(1, len(s)):
            left = int(s[:i])
            right = int(s[i:])
            prod = left * right
            if prod > max_prod:
            