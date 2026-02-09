def new21Game(N, K, W):
    if K == 0:
        return 1.0
    dp = [0.0] * K
    current_sum = 0.0
    for s in range(K-1, -1, -1):
        d_min = K - s
        d_max = min(W, N - s)
        count1 = max(0, d_max - d_min + 1) if d_max >= d_min else 0
        dp[s] = (current_sum + count1) / W
        if s + W <= K - 1:
            current_sum += dp[s] - dp[s + W]
        else:
            current_sum += dp[s]
    return dp[0]