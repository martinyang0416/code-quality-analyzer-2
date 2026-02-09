from collections import deque

class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        size = 3 * n
        expanded = [[0] * size for _ in range(size)]
        
        for i in range(n):
            for j in range(n):
                c = grid[i][j]
                if c == '/':
                    for x in range(3):
                        for y in range(3):
                            if x + y == 2:
                                expanded[3*i + x][3*j + y] = 1
    