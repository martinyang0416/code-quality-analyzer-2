from collections import deque

def minFlips(mat):
    m, n = len(mat), len(mat[0])
    target = tuple(tuple(0 for _ in row) for row in mat)
    initial = tuple(tuple(row) for row in mat)
    if initial == target:
        return 0
    
    visited = set()
    visited.add(initial)
    q = deque([(initial, 0)])
    
    while q:
        current, steps = q.popleft()
        for i in range(m):
            for j in range(n):
                new_mat = [list(row) for row in current]
                new_