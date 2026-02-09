t = int(input())
for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    min_subs = float('inf')
    for i in range(n - d + 1):
        window = a[i:i+d]
        current = len(set(window))
        if current < min_subs:
            min_subs = current
    print(min_subs)