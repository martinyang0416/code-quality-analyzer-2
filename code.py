n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    b, e, t = map(int, input().split())
    length = e - b
    for k in range(length):
        a[b + k], a[t + k] = a[t + k], a[b + k]
print(' '.join(map(str, a)))