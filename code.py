class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols < 3 or rows < 3:
            return 0
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                sub = [
                    grid[i][j:j+3],
                    grid[i+1][j:j+3],
                    grid[i+2][j:j+3]
                ]
                if sub[1