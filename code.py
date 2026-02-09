m = int(input())
r = list(map(int, input().split()))
used = set()
perm = [None] * m

for i in range(m):
    x = r[i]
    if x <= m and x not in used:
        perm[i] = x
        used.add(x)

# Collect remaining numbers
remain = []
for num in range(1, m + 1):
    if num not in used:
        remain.append(num)

# Assign remaining numbers to None positions
k = 0
for i in range(m):
    if perm[i] is None:
        perm[i] = remain[k]
        k += 1

print(' '.join(map(str, perm)))