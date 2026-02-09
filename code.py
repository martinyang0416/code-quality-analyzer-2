n, m = map(int, input().split())
degrees = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    degrees[u] += 1
    degrees[v] += 1

min_modifications = float('inf')

for h in range(1, n + 1):
    c = degrees[h]
    mod = (n - 1) + m - 2 * c
    if mod < min_modifications:
        min_modifications = mod

print(min_modifications)