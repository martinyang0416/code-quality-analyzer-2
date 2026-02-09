a1, a2, a3 = map(int, input().split())
n = a3 + 1

if n == 1:
    print(a1)
elif n == 2:
    print(a2)
else:
    prev_prev = a1
    prev = a2
    for i in range(3, n + 1):
        current = prev_prev + prev
        prev_prev, prev = prev, current
    print(prev)