n, m = map(int, input().split())
t = min(n, m)
# Initialize grid with 1-based indices
grid = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, m + 1):
        grid[i][j] = row[j - 1]

# Initialize prefix sum array
prefix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        distance = (i + j - 2) * grid[i][j]
        prefix[i][j] = distance + prefix[i-1][j] + prefix[i]