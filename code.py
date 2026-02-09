n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

flowers = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'f':
            flowers.append((i, j))

if not flowers:
    for row in grid:
        print(''.join(row))
    exit()

min_r = min(i for i, j in flowers)
max_r = max(i for i, j in flowers)
min_c = min(j for i, j in flowers)
max_c = max(j for i, j in flowers)

single = (min_r == max_r) and (min_c == max_c)

if single:
    top = min_r - 1