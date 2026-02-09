def maxSizeSlices(slices):
    def linear_max(arr, k):
        m = len(arr)
        if m < k * 2 - 1:
            return -float('inf')
        dp = [[-float('inf')] * (k + 1) for _ in range(m)]
        dp[0][0] = 0
        if k >= 1:
            dp[0][1] = arr[0]
        for i in range(1, m):
            for j in range(k + 1):
                # Not take current element
                if dp[i - 1][j] > dp[i][j]:
                    dp[i][j] = dp[i - 1][j]
                # Take current element
 