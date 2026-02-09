n, m = map(int, input().split())
INF = float('-inf')
adj = [[INF] * n for _ in range(n)]

for _ in range(m):
    i, j, c_ij, c_ji = map(int, input().split())
    i -= 1
    j -= 1
    adj[i][j] = c_ij
    adj[j][i] = c_ji

# Check for 2-length cycles
for i in range(n):
    for j in range(n):
        if i != j and adj[i][j] != INF and adj[j][i] != INF:
            if adj[i][j] + adj[j][i] > 0:
                print(2)
                exit()

prev = [row[:] for row in adj]

for k in range(2, n + 1