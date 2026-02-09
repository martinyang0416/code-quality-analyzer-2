from collections import deque

n, m, k = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# Find all empty cells and the starting cell
start = None
empty = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            empty.append((i, j))
            if start is None:
                start = (i, j)

# BFS to build the spanning tree and children structure
children = {}
visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()
i0, j0 = 