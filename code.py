import bisect

def lenLongestFibSubseq(A):
    n = len(A)
    max_len = 0
    dp = [[2] * n for _ in range(n)]
    index = {x: i for i, x in enumerate(A)}
    
    for k in range(n):
        for j in range(k):
            target = A[k] - A[j]
            if target in index and index[target] < j:
                i = index[target]
                dp[j][k] = dp[i][j] + 1
                if dp[j][k] > max_len:
                    max_len = dp[j][k]
    return max_len if max_len >= 3 else 0