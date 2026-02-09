def mctFromLeafValues(arr):
    n = len(arr)
    max_table = [[0] * n for _ in range(n)]
    for i in range(n):
        max_table[i][i] = arr[i]
        for j in range(i + 1, n):
            max_table[i][j] = max(max_table[i][j - 1], arr[j])
    
    dp = [[0] * n for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[