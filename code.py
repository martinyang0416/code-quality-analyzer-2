from typing import List

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        if n == 0:
            return 0
        prev_row = A[0].copy()
        for i in range(1, n):
            current_row = []
            for j in range(n):
                possible = []
                if j > 0:
                    possible.append(prev_row[j-1])
                possible.append(prev_row[j])
                if j < n - 1:
                    possible.append(p