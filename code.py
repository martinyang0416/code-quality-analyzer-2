k, m = map(int, input().split())
for i in range(k):
    start = i * m + 1
    toys = list(range(start, start + m))
    print(' '.join(map(str, toys)))