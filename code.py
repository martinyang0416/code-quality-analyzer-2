n, m, k, h = map(int, input().split())
s = [int(input()) for _ in range(n)]
swaps = []
for _ in range(m):
    a, b = map(int, input().split())
    swaps.append(a)

# Compute the permutation T after applying all swaps
T = list(range(n))
for a in swaps:
    i = a - 1
    if i >= 0 and i + 1 < n:
        T[i], T[i+1] = T[i+1], T[i]

# Compute sum_base
sum_base = sum(s[T[x]] for x in range(k))

min_sum = sum_base

for j in range(m):
    a = swaps[j]
    i = a - 1
    if i < 0 or i + 1 >= n:
        