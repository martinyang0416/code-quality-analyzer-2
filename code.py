class Solution:
    def minDeletionSize(self, A):
        n = len(A[0])
        m = len(A)
        dp = [1] * n
        for j in range(n):
            for i in range(j):
                valid = True
                for r in range(m):
                    if A[r][i] > A[r][j]:
                        valid = False
                        break
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)
        return n - max(dp)