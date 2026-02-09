def minChanges(s, k):
    n = len(s)
    # Precompute the cost matrix
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            left, right = i, j
            current_cost = 0
            while left < right:
                if s[left] != s[right]:
                    current_cost += 1
                left += 1
                right -= 1
            cost[i][j] = current_cost
    
    # Initialize DP table
    dp = [[float('inf')] * (k + 1) for _ in ra