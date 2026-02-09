n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

rows = []
row_indices = [dict() for _ in range(n)]
for i in range(n):
    current_row = []
    for j in range(m):
        if grid[i][j] != '.':
            current_row.append((i, j))
    current_row.sort(key=lambda x: x[1])
    rows.append(current_row)
    for idx, (x, y) in enumerate(current_row):
        row_indices[x][y] = idx

cols = []
col_indices = [dict() for _ in range(m)]
for j in range(m):
    current_col = []